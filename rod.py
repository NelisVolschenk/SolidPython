from solid import *
from solid.utils import *

def cross_rod(rod_length, rod_thickness, outer_radius, inner_radius):

	small_thickness = rod_thickness/3

	small_cross = square(size=(rod_thickness - 2*outer_radius, small_thickness - 2*outer_radius), center=True) + \
		square(size=(small_thickness - 2*outer_radius, rod_thickness - 2*outer_radius), center=True)
	rounded_cross = minkowski()(small_cross, circle(r=outer_radius))
	btm_left = translate((-small_thickness/2 - inner_radius,-small_thickness/2 - inner_radius,0))\
		(arc_inverted(rad=inner_radius, start_degrees=0, end_degrees=90))
	top_left = translate((-small_thickness/2 - inner_radius, small_thickness/2 + inner_radius,0))\
		(arc_inverted(rad=inner_radius, start_degrees=270, end_degrees=360))
	top_right = translate((small_thickness/2 + inner_radius, small_thickness/2 + inner_radius,0))\
		(arc_inverted(rad=inner_radius, start_degrees=180, end_degrees=270))
	btm_right = translate((small_thickness/2 + inner_radius,-small_thickness/2 - inner_radius,0))\
		(arc_inverted(rad=inner_radius, start_degrees=90, end_degrees=180))

	final_cross = linear_extrude(rod_length)(rounded_cross + btm_left + top_left + top_right + btm_right)


	return final_cross