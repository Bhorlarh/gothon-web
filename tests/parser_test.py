from web_app.parser import *
from nose.tools import *
from gothonweb.planisphere import *


def get_path_tests():
	f_data = "shoot"
	test_next = get_room(f_data, central_corridor)
	correct_next = central_corridor.go("shoot")
	assert_equal(correct_next, test_next)
	
	f_data = "dodge"
	test_next = get_room(f_data, central_corridor)
	correct_next = central_corridor.go("dodge")
	assert_equal(correct_next, test_next)
	
	f_data = "tell everyone a funny joke"
	test_next = get_room(f_data, central_corridor)
	correct_next = central_corridor.go("tell a joke")
	assert_equal(correct_next, test_next)
	
	f_data = "teLl everyone a funny joke teLl every"
	test_next = get_room(f_data, the_bridge)
	correct_next = the_bridge.go("tell a joke")
	assert_equal(correct_next, test_next)
	
def check_guess_tests():
	f_data = "0132"
	test_next = check_guess(f_data, laser_weapon_armory)
	correct_next = laser_weapon_armory.go("0132")
	assert_equal(correct_next, test_next)
	
	f_data = "12343 332 232444"
	test_next = check_guess(f_data, laser_weapon_armory)
	correct_next = laser_weapon_armory.go('*')
	assert_equal(correct_next, test_next)