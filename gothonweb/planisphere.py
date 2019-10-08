class Room(object):

	def __init__(self, name, description):
		self.name = name
		self.description = description
		self.paths = {}

	def go(self, direction):
		return self.paths.get(direction, None)

	def add_paths(self, paths):
		self.paths.update(paths)

central_corridor = Room("Central Corridor",
"""
The Gothons of Planet Percal #25 have invaded your ship and 
killed your entire crew. You are the last surviving member 
and your mission is to get the neutron destruct bomb from
the Weapon Armoury, place it on the bridge, and blow the ship
up after getting into a pod.

You're running down the central corridor to the Weapons Armoury.
A Gothon jumps out, red scaly skin, dark grimy teeth, and evil
clown costume flowing around his hate filled body. He's blocking
the Armoury and about to pull a weapon to blast you. What do you 
do?
""")

laser_weapon_armory = Room("Laser Weapon Armory", 
"""
Lucky for you they made you learn Gothon in the academy. You
tell him the one Gothon joke you know: Lbhe zbgure vf fb sng,
jura fur fvgf nebha fur fvgf nebhaq gur ubhfr. The Gothon stops
not to laugh, then bursts out laughing and while he's laughing 
you run up and shoot him in the head putting him down, then jump
through to the Weapon Armory door.

You do a dive roll into the Weapon Armory, crouch and scan for
more Gothons that might be hiding. It's dead quiet, too quiet,
you stand up and run to the far side of the room and find the
neutron bomb in its container. There's a keypad lock on the box
and you enter the code to get the bomb out. If you get the code
wrong 10 times, the lock closes forever and you can't get the
bomb. What is the code?
""")

the_bridge = Room("The Bridge", 
"""
The container clicks open and the seal breaks, gas out. You
grab the neutron bomb and run fast as you can to the bridge
where you must place bomb on the right spot.

You burst onto the Bridge with the neutron destroyer under your
arm and surprise 5 Gothons who are here, take control of the
ship. Each of them has an even funnier clown costume than the
last. They haven't pulled their weapons out yet, as they see
the active bomb in your arm and don't want to set it off.
What do you do?
""")

escape_pod = Room("Escape Pod", 
"""
You point your blaster at the bomb under your arm and the Gothons
put their hands up and start to sweat. You inch backward to the
door, open it, and then carefully place the bomb on the floor,
pointing your blaster at it. You then jump back through the door,
punch the close button and blast the lock so the Gothons can't
get off this time.

You rush through the ship desperately trying to make it to the
escape pod before the whole ship explodes. It seems like hardly
any Gothons are on the ship, so your run is clear of interference.
You get to the chamber with the escape pods, and now need to pick
one to take all of them could be damaged but you don't have time.
There's 5 pods, which do you take?
""")

the_end_winner = Room("The End",
"""
You jump into pod 2 and hit the eject button. The pod easily
slides out into space heading to the planet below. As it flies
to the planet, you look back and see your ship implode then 
explode like a bright star, taking out the Gothon ship at the
same time. You won!
"""
)

the_end_loser = Room("The End", 
"""
You jump into a random pod and hit the eject button. The pod
escapes out into the void of space, then implodes as the hull
ruptures, crushing your body into jam jelly.
"""
)

escape_pod.add_paths({
	'2': the_end_winner,
	'*': the_end_loser
})

generic_death = Room("Death", "You died.")

bridge_death = Room("Death", """
In a panic you throw the bomb at the group of Gothons and make
a leap for the door. Right as you drop it a Gothon shoots you
right in the back killing you. As you die you see another Gothon
frantically try to disarm the bomb. You die knowing they will
probably blow up when it goes off.
""")


the_bridge.add_paths({
	'throw the bomb': bridge_death,
	'slowly place the bomb': escape_pod
})

armory_death = Room("Death", """
The lock buzzes one last time and then you hear a sickening melting
sound as the mechanism is fused together. You decide to sit there,
and finally the Gothons blow up the ship from their ship and you
die.
""")

laser_weapon_armory.add_paths({
	'0132': the_bridge,
	'*': armory_death
})

shoot_death = Room("Death", """
Quick on the draw you yank out your blaster and fire it at the
Gothon. His clown costume is flowing and moving around his body,
which throws off your aim. Your laser hits his costume but misses
him entirely. This completely ruins his brand new costume his mother
bought him, which makes him fly into an insane rage and blast you
repeatedly in the face until you are dead. Then he eats you.
""")

dodge_death = Room("Death", """
Like a world class boxer you dodge, weave, slip and slide right as
the Gothon's blaster cranks a laser past your head. In the middle
of your artful dodge your foot slips and you bang your head on the
metal wall and pass out. You wake up shortly after only to die as 
the Gothon stomps on your head and eats you.
""")


central_corridor.add_paths({
	'shoot': shoot_death,
	'dodge': dodge_death,
	'tell a joke': laser_weapon_armory
})

START = 'central_corridor'

allowed = (central_corridor, dodge_death, shoot_death,
				laser_weapon_armory, armory_death, bridge_death,
				the_bridge, laser_weapon_armory, escape_pod,
				the_end_loser, the_end_winner, generic_death)

_Trap_Room_ = Room("Cage", """
Congrats on finding this, I hope you're pleased with yourself. You
wanted to hack me and I got you instead. Enjoy!
""")
				
def load_room(name):
	"""
	There is a potential security problem here.
	Who gets to set name? Can that expose a variable?
	"""
	if globals().get(name) in allowed:
		return globals().get(name)
	else:
		return _Trap_Room_
	
def name_room(room):
	"""
	Same possible security problem. Can you trust room?
	What's a better solution than this globals lookup?
	"""
	if room in allowed:
		for key, value in globals().items():
			if value == room:		
				return key
	else:
		return _Trap_Room_