from solid import *
from solid.utils import *

def rain_guard(width, height, thickness, border_width, gap_size, slat_thickness):

	hole_height = height-2*border_width
	hole_width = width-2*border_width -2*slat_thickness
	num_slats = hole_height// (gap_size + slat_thickness)
	hole_height = num_slats * (gap_size + slat_thickness) - slat_thickness

	outer_shield = cube((width, thickness, height), center=True)
	hole = cube((hole_width, thickness+2*slat_thickness, hole_height), center=True)
	border = outer_shield-hole

	top_slat_point = (hole_height)/2
	slat_width = hole_width + 2*slat_thickness
	slat_length = sqrt(2)*gap_size + slat_thickness/sqrt(2)

	slat = rotate(a=(-135, 0, 0))(linear_extrude(slat_length)(square(size=(slat_width, slat_thickness/sqrt(2)), center=True)))
	slat = translate((0,thickness/2 - slat_thickness/4,top_slat_point))(slat)

	construct = border
	for i in range(num_slats):
		construct += translate((0,0, -i*(gap_size+slat_thickness)))(slat)

	return construct


draw = rain_guard(100,50,5,5,5,2)
scad_render_to_file(draw, file_header='$fa = 0.1;\n$fs = 0.1;\n$fn = 0;', filepath='solidpython.scad')