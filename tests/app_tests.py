from nose.tools import *
from web_app import app
from gothonweb.planisphere import *

app.config['TESTING'] = True
web = app.test_client()

def test_index():
	rv = web.get('/game')
	assert_in(b"Looks like you bit the dust", rv.data)
	
	rv = web.get('/', follow_redirects=True)
	inv_data = {"action": "0312"}
	rv = web.post('/game', data=inv_data, follow_redirects=True)
	assert_in(b'Central Corridor', rv.data)
	
	f_data = {"action": "tell a joke"}
	rv = web.post('/game', data=f_data, follow_redirects=True)
	assert_in(b'Laser Weapon Armory', rv.data)
	
	s_data = {"action": "0132"}
	rv = web.post('/game', data=s_data, follow_redirects=True)
	assert_in(b'The Bridge', rv.data)
	
	t_data = {"action": "slowly place the bomb"}
	rv = web.post('/game', data=t_data, follow_redirects=True)
	assert_in(b'Escape Pod', rv.data)
	
	frt_data = {"action": "*"}
	rv = web.post('/game', data=frt_data, follow_redirects=True)
	assert_in(b'jam jelly', rv.data)
	