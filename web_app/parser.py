nouns = ['bomb', 'joke']
verb = ['shoot', 'dodge', 'tell', 'throw', 'slowly']
stop = ['a', 'the', 'place']
numbers = ['0132', '2']

	
def get_room(action, c_room):
	list_rooms = list(c_room.paths.keys())
	action = action.lower().split(" ")
	
	# checking each path in room
	for i in list_rooms:
		path = i.split(" ")
		v_counter = 0
		
		# comparing each item in path list 
		for j in path:
			
			# comparing with every item in action
			for s in action:
			
				# when items match, remove item from action list
				if j == s:
					v_counter += 1
					break
		
	
		if v_counter == len(path):
			return c_room.go(i)
	
	return None
	
def check_guess(action, c_room):
	list_guesses = list(c_room.paths.keys())
	action = action.split(" ")
	
	for i in action:
		if i in numbers:
			return c_room.go(i)
	
	return c_room.go('*')
	
def scan(action, c_room):
	action = action.lower()
	guess_no = ["Laser Weapon Armory", "Escape Pod"]
	if c_room.name in guess_no:
		return check_guess(action, c_room)

	return get_room(action, c_room)
	