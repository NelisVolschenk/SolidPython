from solid import *
from solid.utils import *

def rain_guard(width, height, thickness, border_width, vent_height, slat_height):

	hole_height = height-2*border_width
	hole_width = width - 2 * border_width - 2 * slat_height
	num_vents = (hole_height - thickness) // (vent_height + slat_height)
	hole_height = num_vents * (vent_height + slat_height) - slat_height / 2
	print(num_vents)

	outer_shield = cube((width, thickness, height), center=True)

	vent_width = hole_width
	vent_length = sqrt(2) * thickness + vent_height/sqrt(2)
	top_vent_point = (hole_height) / 2 - (vent_height*3/4)

	vent = rotate(a=(-45, 0, 0))(cube((vent_width, vent_length, vent_height/sqrt(2)), center=True))
	vent = translate((0,0,top_vent_point))(vent)

	construct = outer_shield
	for i in range(0,num_vents):
		construct -= translate((0,0, -i*(vent_height+slat_height)))(vent)

	return construct


draw = rain_guard(100,50,5,5,5,2)
scad_render_to_file(draw, file_header='$fa = 0.1;\n$fs = 0.1;\n$fn = 0;', filepath='solidpython.scad')