from solid import *
from solid.utils import *

def rain_guard(width, height, thickness, border_width, gap_size, slat_thickness):

	hole_height = height-2*border_width
	hole_width = width-2*border_width -2*slat_thickness
	num_slats = (hole_height - thickness) // (gap_size + slat_thickness)
	hole_height = num_slats * (gap_size + slat_thickness) - slat_thickness/2

	outer_shield = cube((width, thickness, height), center=True)
	hole = cube((hole_width, thickness+2*slat_thickness, hole_height), center=True)
	border = outer_shield-hole

	top_slat_point = (hole_height)/2
	slat_width = hole_width + 2*slat_thickness
	slat_length = sqrt(2)*gap_size + slat_thickness/sqrt(2)

	slat = rotate(a=(-135, 0, 0))(linear_extrude(slat_length)(square(size=(slat_width, slat_thickness/sqrt(2)), center=True)))
	slat = translate((0,-slat_thickness/4,-slat_thickness/4))(slat)
	cube_width = (slat_length)/sqrt(2)-slat_thickness/2
	cube_height =(slat_length)/sqrt(2)+slat_thickness/2
	slat *= translate((0,cube_width/2,-cube_height/2))(cube((slat_width,cube_width, cube_height), center=True))
	slat = translate((0,-thickness/2,top_slat_point))(slat)

	top_slat_point = (hole_height)/2
	slat_width = hole_width + 2*slat_thickness
	slat_length = sqrt(2)*gap_size + slat_thickness/sqrt(2)

	slat = rotate(a=(-135, 0, 0))(linear_extrude(slat_length)(square(size=(slat_width, slat_thickness/sqrt(2)), center=True)))
	slat = translate((0,-slat_thickness/4,-slat_thickness/4))(slat)
	cube_width = (slat_length)/sqrt(2)-slat_thickness/2
	cube_height =(slat_length)/sqrt(2)+slat_thickness/2
	slat *= translate((0,cube_width/2,-cube_height/2))(cube((slat_width,cube_width, cube_height), center=True))
	slat = translate((0,-thickness/2,top_slat_point))(slat)


	construct = border
	for i in range(0,num_slats):
		construct += translate((0,0, -i*(gap_size+slat_thickness)))(slat)

	# sidebar = cube((slat_thickness, slat_length/sqrt(2), hole_height), True)
	# sidebar = translate((0,(slat_length/sqrt(2)+thickness)/2,0))(sidebar)
	#
	# triangle_thickness = slat_thickness
	# triangle_safety = 2
	# triangle_top = hole_height/2 + slat_thickness/4
	# triangle_bottom = triangle_top - slat_length/sqrt(2)
	# triangle_y_inner = thickness/2
	# triangle_y_outer = triangle_y_inner + slat_length/sqrt(2)
	#
	# print(f'triangle height = {triangle_top-triangle_bottom}')
	# print(f'triangle width = {triangle_y_outer - triangle_y_inner}')
	# tripoints = [(triangle_thickness+triangle_safety,triangle_y_inner-triangle_safety,triangle_top+triangle_safety),
	# 			 (triangle_thickness+triangle_safety,triangle_y_outer+triangle_safety,triangle_top+triangle_safety),
	# 			 (triangle_thickness+triangle_safety,triangle_y_outer+triangle_safety,triangle_bottom-triangle_safety),
	# 			 (-triangle_thickness-triangle_safety, triangle_y_inner - triangle_safety, triangle_top + triangle_safety),
	# 			 (-triangle_thickness-triangle_safety, triangle_y_outer + triangle_safety, triangle_top + triangle_safety),
	# 			 (-triangle_thickness-triangle_safety, triangle_y_outer + triangle_safety, triangle_bottom - triangle_safety)]
	# trifaces = [(0,1,2),
	# 			 (0,3,4,1),
	# 			 (1,4,5,2),
	# 			 (2,5,3,0),
	# 			 (5,4,3)]
	# tri = polyhedron(tripoints,trifaces,convexity=10)
	# sidebar1 = translate((hole_width/2 + slat_thickness/2,0,0))(sidebar - tri)
	return construct


draw = rain_guard(100,50,5,5,5,2)
scad_render_to_file(draw, file_header='$fa = 0.1;\n$fs = 0.1;\n$fn = 0;', filepath='solidpython.scad')