from solid import *
from solid.utils import *
from rod import cross_rod

def panel(width, height, border_thickness, thickness, rod_spacing, rod_outer_radius, rod_inner_radius):
	# Calculations
	workheight = 2*width + height
	rods_up = int((width + height/2)//rod_spacing) + 1
	rods_down = int((width + height/2)//rod_spacing) + 1


	# Calculate and generate the rods
	rod_length = workheight * sqrt(2)
	rod_up = rotate(a=(0,45,0))(cross_rod(rod_length,thickness,rod_outer_radius,rod_inner_radius))
	rod_down = rotate(a=(0, 135, 0))(cross_rod(rod_length, thickness, rod_outer_radius, rod_inner_radius))
	both_rods = left(width/2)(rod_up + rod_down)

	grid = both_rods
	elementlist = []
	# add the rods above
	for i in range(rods_up):
		# grid += up(i * rod_spacing)(both_rods)
		elementlist.append(up(i * rod_spacing)(both_rods))

	# add the rods below
	for i in range(rods_down):
		# grid += down(i * rod_spacing)(both_rods)
		elementlist.append(down(i * rod_spacing)(both_rods))

	grid = union()(tuple(elementlist))

	# Bound the grid to the panel size
	grid = grid * cube((width, thickness, height), center=True)

	# Calculate and generate the outside box
	border = cube((width, thickness, height), center=True) - cube((width-2*border_thickness,2*thickness,height-2*border_thickness), center=True)



	final_panel = grid + border
	return final_panel

draw = panel(300,200,15,5,25,.5,.5)

scad_render_to_file(draw, file_header = '$fa = 0.1;\n$fs = 0.1;\n$fn = 0;',filepath= 'solidpython.scad')
