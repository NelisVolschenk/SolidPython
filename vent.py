from solid import *
from solid.utils import *

def side_vent(width, height, thickness, border_width, vent_height, slat_height):

	hole_height = height-2*border_width
	num_vents = (hole_height - thickness) // (vent_height + slat_height)
	hole_height = num_vents * (vent_height + slat_height) - slat_height / 2
	print(f'There will be {num_vents} vents per column')

	outer_shield = cube((width, thickness, height), center=True)

	vent_width = width - 2 * border_width
	vent_length = sqrt(2) * thickness + vent_height/sqrt(2)
	top_vent_point = (hole_height) / 2 - (vent_height*3/4)

	vent = rotate(a=(-45, 0, 0))(cube((vent_width, vent_length, vent_height/sqrt(2)), center=True))
	vent = translate((0,0,top_vent_point))(vent)

	construct = outer_shield
	for i in range(0,num_vents):
		construct -= translate((0,0, -i*(vent_height+slat_height)))(vent)

	return construct

def vent_grid(width, height, thickness, border_width, vent_height, slat_height, max_vent_length):
	num_vent_columns = (width - 2 * border_width) // (max_vent_length + slat_height) + 1
	print(f'Number of vent columns is {num_vent_columns}')
	vent_length  = ((width - 2 * border_width) - (num_vent_columns-1)*slat_height) / num_vent_columns
	print(f'Vent length is {vent_length}')
	base = side_vent(width, height, thickness, border_width, vent_height, slat_height)
	column = cube((slat_height, thickness, height), center=True)
	column_offset = (width-2*border_width)/2 + slat_height/2 - (vent_length+slat_height)
	column = translate((column_offset,0,0))(column)
	grid = base
	for i in range(num_vent_columns-1):
		grid += translate((-i*(vent_length+slat_height),0,0))(column)
	return grid

def horizontal_vent(length, width, thickness, border_width, vent_size, slat_size):
	vent_width = width - 2*border_width
	num_vents = (length - 2*border_width)//(vent_size + slat_size)
	vent_area_length = num_vents * (vent_size + slat_size)
	plate = cube((length, width, thickness), center=True)
	vent = cube((vent_size, vent_width, thickness), center=True)
	vent = translate((-vent_area_length/2 + vent_size/2,0,0,))(vent)
	construct = plate
	for i in range(num_vents):
		construct -= translate((i*(vent_size + slat_size),0,0))(vent)
	return construct

if __name__ == "__main__":
	# draw = side_vent(100, 50, 5, 5, 3, 2)
	draw = vent_grid(60, 50, 5, 5, 3, 2,20)
	scad_render_to_file(draw, file_header='$fa = 0.1;\n$fs = 0.1;\n$fn = 0;', filepath='solidpython.scad')