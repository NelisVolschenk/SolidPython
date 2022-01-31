// Generated by SolidPython 1.1.1 on 2022-01-31 11:42:31
$fa = 2;
$fs = 0.1;
$fn = 0;


difference() {
	translate(v = [0, -55.0000000000, 0]) {
		union() {
			difference() {
				cube(center = true, size = [70, 50.0000000000, 30]);
				translate(v = [0, -25.0000000000, -15.0000000000]) {
					cylinder(d = 50, h = 30);
				}
				difference() {
					translate(v = [0, -2.5000000000, 0]) {
						cube(center = true, size = [70, 45.0000000000, 10]);
					}
					translate(v = [0, -15.0000000000, 0]) {
						union() {
							translate(v = [0, -12.5000000000, 0]) {
								cube(center = true, size = [50, 25.0000000000, 10]);
							}
							translate(v = [0, 0, -5.0000000000]) {
								cylinder(d = 50, h = 10);
							}
						}
					}
				}
			}
			translate(v = [0, 22.5000000000, 0]) {
				cube(center = true, size = [100, 5, 60]);
			}
		}
	}
	union() {
		translate(v = [45.0000000000, 0, 25.0000000000]) {
			translate(v = [0, -30.0000000000, 0]) {
				rotate(a = [90, 0, 0]) {
					translate(v = [0, 0, -5.0000000000]) {
						cylinder(d = 4, h = 10);
					}
				}
			}
		}
		translate(v = [-45.0000000000, 0, 25.0000000000]) {
			translate(v = [0, -30.0000000000, 0]) {
				rotate(a = [90, 0, 0]) {
					translate(v = [0, 0, -5.0000000000]) {
						cylinder(d = 4, h = 10);
					}
				}
			}
		}
		translate(v = [-45.0000000000, 0, -25.0000000000]) {
			translate(v = [0, -30.0000000000, 0]) {
				rotate(a = [90, 0, 0]) {
					translate(v = [0, 0, -5.0000000000]) {
						cylinder(d = 4, h = 10);
					}
				}
			}
		}
		translate(v = [45.0000000000, 0, -25.0000000000]) {
			translate(v = [0, -30.0000000000, 0]) {
				rotate(a = [90, 0, 0]) {
					translate(v = [0, 0, -5.0000000000]) {
						cylinder(d = 4, h = 10);
					}
				}
			}
		}
	}
}
/***********************************************
*********      SolidPython code:      **********
************************************************
 
from vent import *

box_width = 60
box_height = 148
box_length = 174
box_shell_thickness = 5

bolt_size = 4
bolt_outer_radius = 10/2

bracket_thickness = box_shell_thickness
sensecap_width = 40 + 1  # +1 for easy fitting
top_bracket_offset = 32 + box_shell_thickness
top_bracket_clamp_height = 8
top_bracket_clamp_width = (box_width - sensecap_width) / 2
top_bracket_height = top_bracket_offset + top_bracket_clamp_height
top_bracket_spacing = 132
sensecap_length = 154 + 1  # +1 for easy fitting
top_bracket_side_width = (box_length - sensecap_length) / 2
top_bracket_top_length = (box_length - top_bracket_spacing)/2
bottom_bracket_clamp_length = 15
bottom_bracket_length = top_bracket_side_width + bottom_bracket_clamp_length
bottom_bracket_offset = 118

airial_offset_x = 50
airial_offset_y = 3
airial_diameter = 13
airial_cone_diameter = min(airial_diameter * 3, box_width)
airial_cone_height = airial_cone_diameter/2

mounting_bracket_plate_thickness = 5
mounting_bracket_plate_extra = 10
mounting_bracket_pole_diameter = 50
mounting_bracket_section_thickness = 10
mounting_bracket_length = mounting_bracket_pole_diameter / 2 + 2 * mounting_bracket_section_thickness + mounting_bracket_plate_thickness
mounting_bracket_width = mounting_bracket_pole_diameter + 2 * mounting_bracket_section_thickness
mounting_bracket_height = 3 * mounting_bracket_section_thickness
mounting_bracket_plate_height = 60 #mounting_bracket_height + 2*mounting_bracket_plate_extra +10 @ 50mm pole diameter
mounting_bracket_plate_width = 100 #mounting_bracket_width + 2*mounting_bracket_plate_extra +10 @ 50mm pole diameter
mounting_bracket_support_width = 20

#Create the box
box = cube((box_length,box_width,box_height), center=True)
box_inside =cube((box_length - 2 * box_shell_thickness, box_width, box_height), center=True)
box_inside = translate((0, 0, -box_shell_thickness))(box_inside)
outer_box = box - box_inside

#Create the vents
vent = vent_grid(box_length, box_height, box_shell_thickness, 10, 3, 2, 20)
vent1 = translate((0,(box_width-box_shell_thickness)/2,0))(vent)
vent2 = translate((0,-(box_width-box_shell_thickness)/2,0))(rotate(a=(0,0,180))(vent))
vents = vent1 + vent2

#Create the top brackets
bracket_side = cube((bracket_thickness, top_bracket_clamp_width, top_bracket_height), center=True)
translate_x = (top_bracket_spacing+bracket_thickness)/2
translate_y = (sensecap_width + top_bracket_clamp_width) / 2
translate_z = (box_height - top_bracket_height)/2
bracket_side1 = translate((translate_x,translate_y,translate_z))(bracket_side)
bracket_side2 = translate((translate_x,-translate_y,translate_z))(bracket_side)
bracket_side3 = cube((top_bracket_side_width, bracket_thickness, top_bracket_height), center=True)
bracket_side3 = translate(((box_length-top_bracket_side_width)/2,0,translate_z))(bracket_side3)
bracket_top = cube((bracket_thickness, box_width, top_bracket_offset), center=True)
bracket_top = translate((translate_x,0,(box_height - top_bracket_offset)/2))(bracket_top)
bracket_top_2 = cube((top_bracket_top_length, bracket_thickness, top_bracket_offset), center=True)
bracket_top_2 = translate(((box_length-top_bracket_top_length)/2,0,(box_height - top_bracket_offset)/2))(bracket_top_2)
bracket_1 = bracket_side1 + bracket_side2 + bracket_side3 + bracket_top + bracket_top_2
bracket_2 = rotate(a=(0,0,180))(bracket_1)

#Create the bottom brackets
bracket_clamp = cube((bottom_bracket_length, top_bracket_clamp_width, bracket_thickness), center=True)
translate_x = (box_length - bottom_bracket_length)/2
translate_y = (box_width - top_bracket_clamp_width)/2
translate_z = (box_height - bracket_thickness)/2 - bottom_bracket_offset
bracket_clamp1 = translate((translate_x,translate_y,translate_z))(bracket_clamp)
bracket_clamp2 = translate((translate_x,-translate_y,translate_z))(bracket_clamp)
bracket_bridge = cube((top_bracket_side_width, box_width, bracket_thickness), center=True)
bracket_bridge = translate(((box_length-top_bracket_side_width)/2,0,translate_z))(bracket_bridge)
bottom_bracket1 = bracket_clamp1 + bracket_clamp2 + bracket_bridge
bottom_bracket2 = rotate(a=(0,0,180))(bottom_bracket1)

#Add the brackets to the box
box_with_vents = outer_box + vents + bracket_1 + bracket_2 + bottom_bracket1 + bottom_bracket2

#Remove the large airial hole from the box
large_airial_hole = cylinder(h=airial_cone_height,d1=airial_cone_diameter,d2=0)
large_airial_hole = translate((airial_offset_x, airial_offset_y, box_height / 2 - box_shell_thickness))(large_airial_hole)
box_with_vents -=  large_airial_hole

#Create the airial cone
outer_cone = cylinder(h=airial_cone_height, d1=airial_cone_diameter, d2=0)
inner_cone = translate((0,0,-box_shell_thickness))(cylinder(h=airial_cone_height, d1=airial_cone_diameter, d2=0))
small_airial_hole = cylinder(d=airial_diameter, h=airial_cone_height+2*box_shell_thickness)
airial_cone = outer_cone - inner_cone - small_airial_hole
airial_cone = translate((airial_offset_x, airial_offset_y, box_height / 2))(airial_cone)

#Create the mounting bracket
mounting_bracket = cube((mounting_bracket_width, mounting_bracket_length, mounting_bracket_height), center=True)
pipe_hole = translate((0,-mounting_bracket_length/2,-mounting_bracket_height/2))(cylinder(d=mounting_bracket_pole_diameter,h=mounting_bracket_height))
middle_cube = cube((mounting_bracket_width, mounting_bracket_length-mounting_bracket_plate_thickness, mounting_bracket_section_thickness), center=True)
middle_cube = translate((0,-mounting_bracket_plate_thickness/2,0))(middle_cube)
middle_hole = cube((mounting_bracket_pole_diameter, mounting_bracket_pole_diameter/2, mounting_bracket_section_thickness), center=True)
middle_hole = translate((0,-mounting_bracket_pole_diameter/4,0))(middle_hole)
middle_hole += translate((0,0,-mounting_bracket_section_thickness/2))(cylinder(d=mounting_bracket_pole_diameter,h=mounting_bracket_section_thickness))
middle_hole = translate((0,-mounting_bracket_length/2 + mounting_bracket_section_thickness,0))(middle_hole)
mounting_plate = cube((mounting_bracket_plate_width, mounting_bracket_plate_thickness, mounting_bracket_plate_height), center=True)
# Add the mounting plate to the box
box_with_vents += translate((0,-(box_width-mounting_bracket_plate_thickness)/2,0))(mounting_plate)
# Add supports for the mounting plate
supp1 = cube((mounting_bracket_support_width, box_shell_thickness, box_height), center=True)
supp2 = cube((box_length, box_shell_thickness, mounting_bracket_support_width), center=True)
supps = supp1 +supp2
supps = translate((0,-(box_width-box_shell_thickness)/2,0))(supps)
box_with_vents += supps
# Create the holes for the mounting bracket
bracket_hole = down((box_shell_thickness+mounting_bracket_plate_thickness)/2)(cylinder(d=bolt_size,h=box_shell_thickness+mounting_bracket_plate_thickness))
bracket_hole = rotate(a=(90,0,0))(bracket_hole)
bracket_hole = translate((0,-box_width/2,0))(bracket_hole)
bracket_hole1 = translate(((mounting_bracket_plate_width / 2 - bolt_outer_radius), 0, (mounting_bracket_plate_height / 2 - bolt_outer_radius)))(bracket_hole)
bracket_hole2 = translate((-(mounting_bracket_plate_width / 2 - bolt_outer_radius), 0, (mounting_bracket_plate_height / 2 - bolt_outer_radius)))(bracket_hole)
bracket_hole3 = translate((-(mounting_bracket_plate_width / 2 - bolt_outer_radius), 0, -(mounting_bracket_plate_height / 2 - bolt_outer_radius)))(bracket_hole)
bracket_hole4 = translate(((mounting_bracket_plate_width / 2 - bolt_outer_radius), 0, -(mounting_bracket_plate_height / 2 - bolt_outer_radius)))(bracket_hole)
bracket_holes = bracket_hole1 + bracket_hole2 + bracket_hole3 + bracket_hole4

mounting_plate = translate((0,(mounting_bracket_length - mounting_bracket_plate_thickness)/2,0))(mounting_plate)
mounting_bracket = mounting_bracket - pipe_hole - (middle_cube-middle_hole) + mounting_plate
mounting_bracket = translate((0,-(mounting_bracket_length+box_width)/2,0))(mounting_bracket)

#Add the holes to the mounting bracket and the backplate
mounting_bracket -= bracket_holes
box_with_vents -= bracket_holes

# Create the bottom plate
bottom_plate = horizontal_vent(box_length, box_width, box_shell_thickness, 10, 3, 2)
bottom_plate = translate((0,0,-box_height/2 - box_shell_thickness/2))(bottom_plate)
bottom_plate_mounting_point = cube((bolt_outer_radius*2,bolt_outer_radius*2,box_shell_thickness),center=True)
bottom_plate_mounting_point -= translate((0,0,-box_shell_thickness/2))(cylinder(d=bolt_size,h=box_shell_thickness))
mnt1 = translate(((box_length/2+bolt_outer_radius),(box_width/2-bolt_outer_radius),-(box_height + box_shell_thickness)/2))(bottom_plate_mounting_point)
mnt2 = translate(((box_length/2+bolt_outer_radius),-(box_width/2-bolt_outer_radius),-(box_height + box_shell_thickness)/2))(bottom_plate_mounting_point)
mnt3 = translate((-(box_length/2+bolt_outer_radius),-(box_width/2-bolt_outer_radius),-(box_height + box_shell_thickness)/2))(bottom_plate_mounting_point)
mnt4 = translate((-(box_length/2+bolt_outer_radius),(box_width/2-bolt_outer_radius),-(box_height + box_shell_thickness)/2))(bottom_plate_mounting_point)
mounts = mnt1 + mnt2 + mnt3 + mnt4
bottom_plate += mounts

# Also add the mounts to the box
box_with_vents += translate((0,0,box_shell_thickness))(mounts)

test = box_with_vents
# For printing -  This will ensure sufficient quality for printing
#$fs = 0.1  filament size/2
#$fa = 1

quality_directive = '$fa = 2;\n$fs = 0.1;\n$fn = 0;'
scad_render_to_file(box_with_vents, file_header=quality_directive, filepath='renders/sensecap_box.scad')
scad_render_to_file(airial_cone, file_header=quality_directive, filepath='renders/sensecap_cone.scad')
scad_render_to_file(mounting_bracket, file_header=quality_directive, filepath='renders/sensecap_mounting_bracket.scad')

scad_render_to_file(test, file_header=quality_directive, filepath='renders/sensecap_test.scad') 
 
************************************************/