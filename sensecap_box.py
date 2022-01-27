from vent import *

box_width = 70
box_height = 180
box_length = 180
box_shell_thickness = 5
airial_offset = box_length/2 - 45
airial_diameter = 12
airial_cone_diameter = min(airial_diameter * 3, box_width)
airial_cone_height = airial_cone_diameter/2

#Create the box
box = cube((box_length,box_width,box_height), center=True)
box_inside =cube((box_length - 2 * box_shell_thickness, box_width, box_height), center=True)
box_inside = translate((0, 0, -box_shell_thickness))(box_inside)
outer_box = box - box_inside

#Insert the vents
vent = vent_grid(box_length, box_height, box_shell_thickness, 10, 3, 2, 20)
vent1 = translate((0,box_width/2,0))(vent)
vent2 = translate((0,-box_width/2,0))(rotate(a=(0,0,180))(vent))
vents = vent1 + vent2

#Add the airial cone and hole
outer_cone = cylinder(h=airial_cone_height, d1=airial_cone_diameter, d2=0)
inner_cone = translate((0,0,-box_shell_thickness))(cylinder(h=airial_cone_height, d1=airial_cone_diameter, d2=0))
airial_cone = outer_cone - inner_cone
airial_cone = translate((airial_offset,0,box_height/2))(airial_cone)

box_with_vents = outer_box + vents
total_box = box_with_vents + airial_cone
large_airial_hole = cylinder(h=box_shell_thickness,d=airial_cone_diameter-box_shell_thickness)
large_airial_hole = translate((airial_offset,0,box_height/2-box_shell_thickness))(large_airial_hole)
small_airial_hole = cylinder(d=airial_diameter, h=airial_cone_height+2*box_shell_thickness)
small_airial_hole = translate((airial_offset,0,box_height/2-box_shell_thickness))(small_airial_hole)

draw = total_box - (large_airial_hole + small_airial_hole)
scad_render_to_file(draw, file_header='$fa = 0.1;\n$fs = 0.1;\n$fn = 0;', filepath='sensecap_box.scad')