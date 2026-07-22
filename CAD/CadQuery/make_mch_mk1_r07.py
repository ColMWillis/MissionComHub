import cadquery as cq
from cadquery import exporters
from pathlib import Path
import trimesh, shutil, json

REV = 'R0.7'
OUT = Path(__file__).resolve().parent / 'MissionComHub_MkI_Enclosure_R0.7'
OUT.mkdir(parents=True, exist_ok=True)

# ---------------- USER / DESIGN PARAMETERS (mm) ----------------
# Compact enclosure target
L = 140.0                 # X, long dimension
W = 90.0                  # Y, front-to-back
H = 52.0                  # Z, body height
WALL = 3.0
BOTTOM = 3.2
CORNER_R = 6.0
LID_T = 4.0
LIP_DEPTH = 3.5
FIT = 0.35

# User-supplied component sizes, converted from inches
SWITCH_W = 1.5 * 25.4     # 38.10
SWITCH_H = 0.8 * 25.4     # 20.32
METER_W = 1.8 * 25.4      # 45.72
METER_H = 1.1 * 25.4      # 27.94
PD_BOARD_W = 0.7 * 25.4   # 17.78
PD_BOARD_L = 1.7 * 25.4   # 43.18
PD_SOLDER_EXT = 0.1*25.4  # 2.54 extra opposite USB connector

# Printing clearances; adjust after coupon tests
SWITCH_CUT_W = SWITCH_W + 0.45
SWITCH_CUT_H = SWITCH_H + 0.45
# R0.5 fit correction: R0.4 height was correct, but width was slightly tight.
# Restore 1.0 mm total width (0.5 mm per side); retain R0.4's height.
METER_R05_WIDTH_REDUCTION = 1.0
METER_R05_HEIGHT_REDUCTION = 2.0
METER_CUT_W = METER_W + 0.45 - METER_R05_WIDTH_REDUCTION
METER_CUT_H = METER_H + 0.45 - METER_R05_HEIGHT_REDUCTION
# AAOTOKK B08HS6X44P panel mount, based on the supplied dimension image.
USB_FLANGE_W = 33.0
USB_FLANGE_H = 25.0
USB_FLANGE_CLEARANCE = 0.40
USB_RECESS_DEPTH = 0.80
USB_SCREW_CTC = 25.0
USB_SCREW_D = 2.8
USB_CUT_W = 11.0          # 10 x 5 mm connector body plus FDM clearance
USB_CUT_H = 6.0

# Measured bonded 20 AWG Peplink cable: 3.81 x 2.03 mm.
PEPLINK_CABLE_W = 3.81
PEPLINK_CABLE_H = 2.03
# R0.6 physical coupon result: the smallest R0.5 body opening was correct.
PEPLINK_SLOT_W = 4.10
PEPLINK_SLOT_H = 2.40
# The strain-relief channel was too tight; add 0.5 mm overall in both axes.
PEPLINK_CHANNEL_W = 4.55
PEPLINK_CHANNEL_H = 2.70

# Blue Sea Systems 5045 documented footprint.
FUSE_BLOCK_W = 92.5
FUSE_BLOCK_D = 43.8
FUSE_MOUNT_CTC = 65.1
FUSE_MOUNT_PILOT_D = 3.6
FUSE_CENTER_X = 8.0
FUSE_CENTER_Y = -18.0

# Unfused RVBOATPAT-style bus bar, based on the supplied dimension image.
# Mounting centers are provisional until the physical part arrives.
BUS_COVER_L = 5.4 * 25.4       # 137.16
BUS_BASE_L = 4.7 * 25.4        # 119.38
BUS_W = 1.5 * 25.4             # 38.10
BUS_H = 0.9 * 25.4             # 22.86
BUS_MOUNT_RECESS_D = 0.4 * 25.4
BUS_MOUNT_CTC_NOMINAL = 106.5  # estimated from supplied product image
BUS_MOUNT_SLOT_L = 8.0
BUS_MOUNT_SLOT_W = 5.8

# ---------------- HELPERS ----------------
def rounded_box(l, w, h, r, z0=0):
    obj = cq.Workplane('XY').box(l, w, h, centered=(True, True, False)).translate((0,0,z0))
    try:
        obj = obj.edges('|Z').fillet(r)
    except Exception:
        pass
    return obj

def rounded_rect_prism_xy(w, h, depth, radius=1.0, z0=0):
    wp = cq.Workplane('XY').rect(w-2*radius, h).extrude(depth).translate((0,0,z0))
    wp = wp.union(cq.Workplane('XY').rect(w, h-2*radius).extrude(depth).translate((0,0,z0)))
    for x in (-w/2+radius, w/2-radius):
        for y in (-h/2+radius, h/2-radius):
            wp = wp.union(cq.Workplane('XY').center(x,y).circle(radius).extrude(depth).translate((0,0,z0)))
    return wp

def panel_cut_xz(x, z, width, height, y, depth=8, radius=1.0):
    # rounded rectangle cut oriented through Y wall
    shape = cq.Workplane('XZ').center(x,z).rect(width-2*radius,height).extrude(depth,both=True)
    shape = shape.union(cq.Workplane('XZ').center(x,z).rect(width,height-2*radius).extrude(depth,both=True))
    for xx in (-width/2+radius,width/2-radius):
        for zz in (-height/2+radius,height/2-radius):
            shape = shape.union(cq.Workplane('XZ').center(x+xx,z+zz).circle(radius).extrude(depth,both=True))
    return shape.translate((0,y,0))

def panel_pocket_xz(x, z, width, height, y, depth, radius=1.5):
    """Cut an inward pocket from the +Y I/O face."""
    shape = cq.Workplane('XZ', origin=(0, y + 0.02, 0)).center(x, z).rect(
        width - 2 * radius, height
    ).extrude(depth)
    shape = shape.union(
        cq.Workplane('XZ', origin=(0, y + 0.02, 0)).center(x, z).rect(
            width, height - 2 * radius
        ).extrude(depth)
    )
    for xx in (-width / 2 + radius, width / 2 - radius):
        for zz in (-height / 2 + radius, height / 2 - radius):
            shape = shape.union(
                cq.Workplane('XZ', origin=(0, y + 0.02, 0))
                .center(x + xx, z + zz).circle(radius).extrude(depth)
            )
    return shape

def aaotokk_panel_cut(body_obj, x, z, y):
    """Connector aperture, screw holes, and shallow flush-flange recess."""
    body_obj = body_obj.cut(panel_cut_xz(x, z, USB_CUT_W, USB_CUT_H, y, radius=2.6))
    for dx in (-USB_SCREW_CTC / 2, USB_SCREW_CTC / 2):
        hole = cq.Workplane('XZ').center(x + dx, z).circle(USB_SCREW_D / 2).extrude(8, both=True).translate((0, y, 0))
        body_obj = body_obj.cut(hole)
    pocket_w = USB_FLANGE_W + USB_FLANGE_CLEARANCE
    pocket_h = USB_FLANGE_H + USB_FLANGE_CLEARANCE
    return body_obj.cut(panel_pocket_xz(x, z, pocket_w, pocket_h, y, USB_RECESS_DEPTH, radius=2.0))

def tie_down_tab(x, y, rotation=0):
    tab = cq.Workplane('XY').center(x, y).rect(10, 5).extrude(4).translate((0, 0, BOTTOM))
    slot = cq.Workplane('YZ').center(y, BOTTOM + 2.0).rect(2.4, 6.0).extrude(8, both=True).translate((x, 0, 0))
    tab = tab.cut(slot)
    if rotation:
        tab = tab.rotate((0, 0, 0), (0, 0, 1), rotation)
    return tab

# ---------------- BODY ----------------
outer = rounded_box(L,W,H,CORNER_R)
inner = rounded_box(L-2*WALL,W-2*WALL,H-BOTTOM+0.5,max(1.2,CORNER_R-WALL),z0=BOTTOM)
body = outer.cut(inner)

control_y = -W/2
io_y = W/2
panel_z = 26.0

# Control face: voltmeter and switch, opposite I/O
meter_x = -29.0
switch_x = 30.0
body = body.cut(panel_cut_xz(meter_x,panel_z,METER_CUT_W,METER_CUT_H,control_y,radius=1.5))
body = body.cut(panel_cut_xz(switch_x,panel_z,SWITCH_CUT_W,SWITCH_CUT_H,control_y,radius=1.2))

# I/O face: two measured AAOTOKK panel mounts and the bonded Peplink cable.
usb_in_x = -43.0
usb_out_x = 0.0
peplink_x = 48.0
for x in (usb_in_x, usb_out_x):
    body = aaotokk_panel_cut(body, x, panel_z, io_y)
peplink_z = BOTTOM + 2.4
body = body.cut(panel_cut_xz(peplink_x, peplink_z, PEPLINK_SLOT_W, PEPLINK_SLOT_H, io_y, radius=1.25))

# Universal electronics cradles near the I/O face. They are rotated along X to
# leave the documented Blue Sea 5045 footprint clear on the control side.
board_total_l = PD_BOARD_L + PD_SOLDER_EXT + 2.0
for x in (-39.0, 15.0):
    shelf_y = 30.5
    shelf = cq.Workplane('XY').center(x,shelf_y).rect(board_total_l,PD_BOARD_W+5.0).extrude(2.2).translate((0,0,BOTTOM))
    body = body.union(shelf)
    for dy in (-PD_BOARD_W/2-1.5, PD_BOARD_W/2+1.5):
        rail = cq.Workplane('XY').center(x,shelf_y+dy).rect(board_total_l,2.0).extrude(5.0).translate((0,0,BOTTOM+2.2))
        body = body.union(rail)
    for xx in (-board_total_l/4, board_total_l/4):
        slot = cq.Workplane('XY').center(x+xx,shelf_y).rect(2.8,PD_BOARD_W+1.0).extrude(6).translate((0,0,BOTTOM-0.5))
        body = body.cut(slot)

# Reduced strain-relief saddle and M3 anchor pair for the bonded 20 AWG cable.
strain_y = io_y - 13.0
saddle = cq.Workplane('XY').center(peplink_x,strain_y).rect(18,10).extrude(2.2).translate((0,0,BOTTOM))
saddle_channel = panel_cut_xz(peplink_x, BOTTOM+1.65, PEPLINK_CHANNEL_W, PEPLINK_CHANNEL_H/2, strain_y, depth=7, radius=0.5)
body = body.union(saddle).cut(saddle_channel)
for dx in (-5.8,5.8):
    anchor = cq.Workplane('XY').center(peplink_x+dx,strain_y).circle(3.4).extrude(5.0).translate((0,0,BOTTOM))
    hole = cq.Workplane('XY').center(peplink_x+dx,strain_y).circle(1.55).extrude(4.5).translate((0,0,BOTTOM+1.0))
    body = body.union(anchor).cut(hole)

# Blue Sea 5045 two-point mounting bosses (65.1 mm centers).
for dx in (-FUSE_MOUNT_CTC/2, FUSE_MOUNT_CTC/2):
    fx = FUSE_CENTER_X + dx
    boss = cq.Workplane('XY').center(fx,FUSE_CENTER_Y).circle(5.0).extrude(6.0).translate((0,0,BOTTOM))
    pilot = cq.Workplane('XY').center(fx,FUSE_CENTER_Y).circle(FUSE_MOUNT_PILOT_D/2).extrude(6.5).translate((0,0,BOTTOM+0.5))
    body = body.union(boss).cut(pilot)

# Raised routing rails and serviceable zip-tie tabs keep wiring off fuse terminals.
for rx in (-52.0, 57.0):
    rail = cq.Workplane('XY').center(rx,0).rect(1.8,42).extrude(3.0).translate((0,0,BOTTOM))
    body = body.union(rail)
for tx,ty,rot in [(-56,13,0), (55,14,0), (-55,-30,0), (55,-30,0)]:
    body = body.union(tie_down_tab(tx,ty,rot))

# Engraved I/O labels on the exterior face. The +Y face is viewed opposite
# the XZ workplane normal, so mirror the text geometry about its own center.
try:
    for label,x in [('BATTERY',usb_in_x),('STARLINK',usb_out_x),('PEPLINK',peplink_x)]:
        label_z = 9.5 if label != 'PEPLINK' else 12.0
        txt = cq.Workplane('XZ', origin=(0, io_y+0.02, 0)).text(
            label, 4.2, 0.65, font='DejaVu Sans', halign='center', valign='center'
        ).mirror('YZ').translate((x,0,label_z))
        body = body.cut(txt)
except Exception as e:
    print('I/O label warning:', e)

# Control-face labels are viewed along the XZ workplane normal and therefore
# do not need the corrective mirror used on the +Y I/O face.
try:
    for label,x in [('VOLTAGE',meter_x),('POWER',switch_x)]:
        txt = cq.Workplane('XZ', origin=(0, control_y+0.02, 0)).text(
            label, 4.2, 0.65, font='DejaVu Sans', halign='center', valign='center'
        ).translate((x,0,7.5))
        body = body.cut(txt)
except Exception as e:
    print('Control label warning:', e)

# Corner bosses for M3 lid screws
boss_positions=[(-61,-36),(61,-36),(-61,36),(61,36)]
for x,y in boss_positions:
    boss=cq.Workplane('XY').center(x,y).circle(4.8).extrude(H-3)
    bore=cq.Workplane('XY').center(x,y).circle(2.05).extrude(8).translate((0,0,H-8))
    body=body.union(boss).cut(bore)

# Vent slots on short sides, high and away from cable exits
for xside in (-1,1):
    x=xside*L/2
    for y in (-18,0,18):
        vent=cq.Workplane('YZ').center(y,40).rect(12,3.0).extrude(WALL+3,both=True).translate((x,0,0))
        body=body.cut(vent)

# ---------------- LID ----------------
lid=rounded_box(L,W,LID_T,CORNER_R)
for x,y in boss_positions:
    lid=lid.cut(cq.Workplane('XY').center(x,y).circle(1.7).extrude(LID_T+2))

# Underside locating lip. R0.2's lip outer edge exceeded the body opening;
# R0.4 retains the corrected R0.3 lip keyed to the opening with FIT clearance.
LIP_OUTER_L = L - 2*WALL - 2*FIT
LIP_OUTER_W = W - 2*WALL - 2*FIT
LIP_RING_T = 2.0
lip_outer=rounded_box(LIP_OUTER_L,LIP_OUTER_W,LIP_DEPTH,max(1,CORNER_R-WALL-FIT),z0=-LIP_DEPTH)
lip_inner=rounded_box(LIP_OUTER_L-2*LIP_RING_T,W-2*WALL-2*FIT-2*LIP_RING_T,LIP_DEPTH+0.4,max(1,CORNER_R-WALL-FIT-LIP_RING_T),z0=-LIP_DEPTH-0.2)
lid=lid.union(lip_outer.cut(lip_inner))

# Keep the locating lip clear of the enclosure's corner bosses, and re-cut the
# screw bores after the lip union so the holes remain continuous.
for x,y in boss_positions:
    boss_clearance = cq.Workplane('XY').center(x,y).circle(5.15).extrude(LIP_DEPTH+0.3).translate((0,0,-LIP_DEPTH-0.1))
    through_bore = cq.Workplane('XY').center(x,y).circle(1.7).extrude(LID_T+LIP_DEPTH+2).translate((0,0,-LIP_DEPTH-1))
    lid = lid.cut(boss_clearance).cut(through_bore)

# Raised branding, same style/content
font='DejaVu Sans'
try:
    t1=cq.Workplane('XY').workplane(offset=LID_T).center(0,16).text('Mission Communications Hub',8.5,0.8,font=font,halign='center',valign='center')
    t2=cq.Workplane('XY').workplane(offset=LID_T).center(0,-1).text('Mk I',8.0,0.8,font=font,halign='center',valign='center')
    t3=cq.Workplane('XY').workplane(offset=LID_T).center(0,-18).text('GAWG CAP',7.0,0.8,font=font,halign='center',valign='center')
    lid=lid.union(t1).union(t2).union(t3)
except Exception as e:
    print('Text generation warning:',e)

# ---------------- STRAIN RELIEF CLAMP ----------------
# Compact bridge clamp with half-depth rounded channel; the matching saddle
# supplies the other half, preventing the printed clamp from crushing insulation.
clamp = cq.Workplane('XY').rect(18,10).extrude(3.6)
for x in (-5.8,5.8):
    clamp=clamp.cut(cq.Workplane('XY').center(x,0).circle(1.65).extrude(5))
channel = cq.Workplane('XZ').center(0,0.15).rect(PEPLINK_CHANNEL_W-1.0, PEPLINK_CHANNEL_H/2).extrude(12,both=True)
channel = channel.union(cq.Workplane('XZ').center(0,PEPLINK_CHANNEL_H/4+0.15).circle((PEPLINK_CHANNEL_W-1.0)/2).extrude(12,both=True))
clamp = clamp.cut(channel)

# ---------------- FIT COUPONS ----------------
control_coupon=rounded_box(105,42,3.2,3)
control_coupon=control_coupon.cut(cq.Workplane('XY').center(-27,0).rect(METER_CUT_W,METER_CUT_H).extrude(5))
control_coupon=control_coupon.cut(cq.Workplane('XY').center(28,0).rect(SWITCH_CUT_W,SWITCH_CUT_H).extrude(5))

usb_coupon = cq.Workplane('XZ', origin=(0,1.6,0)).rect(76,34).extrude(3.2)
usb_coupon = aaotokk_panel_cut(usb_coupon, 0, 0, 1.6)
# Lay the coupon flat for printing after cutting the actual vertical panel geometry.
usb_coupon = usb_coupon.rotate((0,0,0),(1,0,0),90).translate((0,17,1.6))

wire_coupon=rounded_box(60,25,3.2,3)
for i,(w,h) in enumerate([(4.10,2.40),(4.35,2.65),(4.60,2.90)]):
    x=-20+i*20
    wire_coupon=wire_coupon.cut(rounded_rect_prism_xy(w,h,5,min(2.2,h/2-0.1)).translate((x,0,0)))

# Blue Sea 5045 riser coupon: documented 65.1 mm centers and current body boss geometry.
fused_block_coupon = rounded_box(100,52,3.2,4)
for dx in (-FUSE_MOUNT_CTC/2, FUSE_MOUNT_CTC/2):
    boss = cq.Workplane('XY').center(dx,0).circle(5.0).extrude(6.0).translate((0,0,3.2))
    pilot = cq.Workplane('XY').center(dx,0).circle(FUSE_MOUNT_PILOT_D/2).extrude(7.0).translate((0,0,2.7))
    fused_block_coupon = fused_block_coupon.union(boss).cut(pilot)

# Provisional unfused-bus coupon. Its plate represents the supplied cover
# envelope plus 1 mm margin per end. Elongated slots span approximately
# 104.3-108.7 mm mounting centers pending physical verification.
unfused_block_coupon = rounded_box(BUS_COVER_L+2.0,BUS_W+6.0,3.2,4)
for dx in (-BUS_MOUNT_CTC_NOMINAL/2, BUS_MOUNT_CTC_NOMINAL/2):
    boss = rounded_rect_prism_xy(12.0,12.0,6.0,3.0,z0=3.2).translate((dx,0,0))
    slot = rounded_rect_prism_xy(BUS_MOUNT_SLOT_L,BUS_MOUNT_SLOT_W,7.0,BUS_MOUNT_SLOT_W/2,z0=2.7).translate((dx,0,0))
    unfused_block_coupon = unfused_block_coupon.union(boss).cut(slot)

parts={
 'MCH-MkI_body_R0.7':body,
 'MCH-MkI_lid_R0.7':lid,
 'MCH-MkI_peplink_strain_relief_R0.7':clamp,
 'MCH-MkI_control_fit_coupon_R0.7':control_coupon,
 'MCH-MkI_AAOTOKK_USB-C_fit_coupon_R0.7':usb_coupon,
 'MCH-MkI_wire_exit_fit_coupon_R0.7':wire_coupon,
 'MCH-MkI_BlueSea5045_fused_block_riser_coupon_R0.7':fused_block_coupon,
 'MCH-MkI_unfused_busbar_riser_coupon_R0.7':unfused_block_coupon,
}

manifest={
 'revision':'R0.7',
 'enclosure_mm':[L,W,H],
 'wall_mm':WALL,
 'lid': {
   'plate_thickness_mm':LID_T,
   'lip_depth_mm':LIP_DEPTH,
   'lip_outer_mm':[LIP_OUTER_L,LIP_OUTER_W],
   'lip_ring_thickness_mm':LIP_RING_T,
   'body_opening_mm':[L-2*WALL,W-2*WALL],
   'clearance_each_side_mm':FIT,
 },
 'switch_user_size_mm':[round(SWITCH_W,2),round(SWITCH_H,2)],
 'switch_cutout_mm':[round(SWITCH_CUT_W,2),round(SWITCH_CUT_H,2)],
 'voltmeter_user_size_mm':[round(METER_W,2),round(METER_H,2)],
 'voltmeter_cutout_mm':[round(METER_CUT_W,2),round(METER_CUT_H,2)],
 'voltmeter_reduction_from_r03_total_mm':[METER_R05_WIDTH_REDUCTION,METER_R05_HEIGHT_REDUCTION],
 'voltmeter_change_from_r04_mm':[1.0,0.0],
 'pd_board_mm':[round(PD_BOARD_W,2),round(PD_BOARD_L,2),round(PD_SOLDER_EXT,2)],
 'aaotokk_usb_c': {
   'flange_mm':[USB_FLANGE_W,USB_FLANGE_H],
   'flange_recess_mm':[USB_FLANGE_W+USB_FLANGE_CLEARANCE,USB_FLANGE_H+USB_FLANGE_CLEARANCE,USB_RECESS_DEPTH],
   'connector_cutout_mm':[USB_CUT_W,USB_CUT_H],
   'mount_hole_ctc_mm':USB_SCREW_CTC,
   'mount_hole_diameter_mm':USB_SCREW_D,
 },
 'blue_sea_5045': {
   'overall_mm':[FUSE_BLOCK_W,FUSE_BLOCK_D],
   'mounting_centers_mm':FUSE_MOUNT_CTC,
   'boss_center_mm':[FUSE_CENTER_X,FUSE_CENTER_Y],
   'pilot_diameter_mm':FUSE_MOUNT_PILOT_D,
 },
 'unfused_busbar_provisional': {
   'cover_envelope_mm':[round(BUS_COVER_L,2),round(BUS_W,2),round(BUS_H,2)],
   'base_length_mm':round(BUS_BASE_L,2),
   'mount_recess_diameter_mm':round(BUS_MOUNT_RECESS_D,2),
   'estimated_mount_centers_mm':BUS_MOUNT_CTC_NOMINAL,
   'coupon_slot_mm':[BUS_MOUNT_SLOT_L,BUS_MOUNT_SLOT_W],
   'status':'provisional_pending_physical_part',
 },
 'peplink_bonded_cable_mm':[PEPLINK_CABLE_W,PEPLINK_CABLE_H],
 'peplink_wire_exit_mm':[PEPLINK_SLOT_W,PEPLINK_SLOT_H],
 'peplink_strain_channel_mm':[PEPLINK_CHANNEL_W,PEPLINK_CHANNEL_H],
 'peplink_r06_strain_channel_increase_total_mm':[0.5,0.5],
}

for name,obj in parts.items():
    stl=OUT/f'{name}.stl'; step=OUT/f'{name}.step'
    exporters.export(obj,str(stl),tolerance=0.07,angularTolerance=0.12)
    exporters.export(obj,str(step))
    mesh=trimesh.load_mesh(stl,force='mesh')
    mesh.export(OUT/f'{name}.3mf')
    print(name,'faces',len(mesh.faces),'watertight',mesh.is_watertight,'extents',mesh.extents)

shutil.copy(Path(__file__).resolve(),OUT/'make_mch_mk1_r07.py')
(OUT/'dimensions.json').write_text(json.dumps(manifest,indent=2))

readme=f'''# Mission Communications Hub Mk I Enclosure R0.7

Compact refactor based on measured components.

## Overall size
- Body: {L:.0f} x {W:.0f} x {H:.0f} mm
- Wall: {WALL:.1f} mm
- Separate {LID_T:.1f} mm lid with locating lip and raised branding

## Control face
- Voltmeter opening: {METER_CUT_W:.2f} x {METER_CUT_H:.2f} mm
- Power switch opening: {SWITCH_CUT_W:.2f} x {SWITCH_CUT_H:.2f} mm

R0.7 preserves all physically verified R0.6 cutouts and corrects the exterior I/O label orientation. It adds VOLTAGE and POWER control-face labels plus separate fused and unfused power-block riser coupons.

## I/O face
- Two AAOTOKK panel mounts: {USB_FLANGE_W:.1f} x {USB_FLANGE_H:.1f} mm flange, {USB_SCREW_CTC:.1f} mm screw centers
- Connector opening: {USB_CUT_W:.1f} x {USB_CUT_H:.1f} mm; M2.5 clearance holes: {USB_SCREW_D:.1f} mm
- Flush flange pocket: {USB_FLANGE_W+USB_FLANGE_CLEARANCE:.1f} x {USB_FLANGE_H+USB_FLANGE_CLEARANCE:.1f} x {USB_RECESS_DEPTH:.1f} mm deep
- Peplink bonded-cable exit: {PEPLINK_SLOT_W:.2f} x {PEPLINK_SLOT_H:.2f} mm rounded slot
- Reduced two-screw strain-relief for the measured {PEPLINK_CABLE_W:.2f} x {PEPLINK_CABLE_H:.2f} mm bonded 20 AWG cable
- Strain-relief cable channel: {PEPLINK_CHANNEL_W:.2f} x {PEPLINK_CHANNEL_H:.2f} mm
- Correctly oriented engraved BATTERY, STARLINK, and PEPLINK labels
- Engraved VOLTAGE and POWER control-face labels

## Blue Sea 5045 mounting
- Documented body footprint reserved: {FUSE_BLOCK_W:.1f} x {FUSE_BLOCK_D:.1f} mm
- Two internal mounting bosses at {FUSE_MOUNT_CTC:.1f} mm centers
- {FUSE_MOUNT_PILOT_D:.1f} mm pilot holes; verify the chosen M4 fastening method before final assembly
- Full riser coupon included

## Unfused bus bar (provisional)
- Supplied cover envelope: {BUS_COVER_L:.2f} x {BUS_W:.2f} x {BUS_H:.2f} mm
- Supplied lower-base length: {BUS_BASE_L:.2f} mm
- Provisional coupon uses {BUS_MOUNT_SLOT_L:.1f} x {BUS_MOUNT_SLOT_W:.1f} mm elongated riser slots at nominal {BUS_MOUNT_CTC_NOMINAL:.1f} mm centers
- The cover is {BUS_COVER_L-(L-2*WALL):.2f} mm longer than the current {L-2*WALL:.1f} mm internal enclosure length, so the body does not yet include this block
- Do not freeze body bosses until the physical block verifies its footprint and mounting centers

## PD board accommodation
Two universal cradles are sized around a {PD_BOARD_W:.2f} x {PD_BOARD_L:.2f} mm board, with an additional {PD_SOLDER_EXT:.2f} mm solder-joint allowance. They are rotated along X to preserve the fuse-block footprint. Routing rails and four zip-tie tabs keep service loops away from fuse terminals.

## Print order
1. Print the control, USB-C, wire-exit, fused-block, and unfused-block coupons.
2. Test the switch, voltmeter, both AAOTOKK receptacles, and bonded Peplink cable.
3. Adjust the parameters at the top of `make_mch_mk1_r07.py` if necessary.
4. Print the body, lid and strain-relief clamp.

## Suggested print settings
- PETG-CF
- 0.4 mm hardened nozzle
- 0.20 mm layer height
- 4 perimeters
- 5 top/bottom layers
- 25-35% gyroid infill
- Body upright; lid branding upward
- Body: supports only where the slicer identifies control/I-O openings as necessary
- Lid: branding upward preserves the visible text; enable snug/organic supports beneath the broad center panel, or test a long-edge orientation with a brim

## Serviceability
- The R0.6 4 mm removable lid, corrected locating lip, M3 corner-boss pattern, and raised branding are preserved.
- All external component geometry has a fit coupon. Print coupons before the body.
- The AAOTOKK flange dimensions came from the supplied dimension image; verify screw spacing and recess fit on the coupon.
- The Blue Sea 5045 footprint is based on the manufacturer's documented 92.5 x 43.8 mm envelope and 65.1 mm mounting centers.

## Regenerating the files
Python 3.11 or newer is recommended. Install `cadquery` and `trimesh`, then run:

```text
python make_mch_mk1_r07.py
```

The generator writes a synchronized STEP, STL, and millimeter-unit 3MF for each part into a `MissionComHub_MkI_Enclosure_R0.7` folder beside the script.
'''
(OUT/'README.md').write_text(readme)
