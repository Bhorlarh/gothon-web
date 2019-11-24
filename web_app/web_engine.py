from . import app, main, db
from gothonweb import planisphere
from flask_login import login_required
from flask import session, redirect, url_for, request, render_template
from .models import User
from .parser import *


@app.route("/play")
@login_required
def play():
	# this is used to "setup" the session with starting values
	user = User.query.get(int(session["user_id"]))

	session['game'] = {}
	session['game']['options'] = []

	session['room_name'] = planisphere.START
	session['score'] = 0
	session['game']['highscore'] = user.highscore
	session['old'] = True

	return redirect(url_for("game"))

@app.route("/game", methods=['GET', 'POST'])
@login_required
def game():
	room_name = session.get('room_name')
	if request.method == "GET":

		# check if user was redirected from "play" option in profile
		if room_name:
			room = planisphere.load_room(room_name)

			if room.name in ["Death", "The End"] and (session['game']['highscore'] < session['score']):
				user = User.query.get(int(session["user_id"]))
				user.highscore = session['score']
				db.session.commit()

			if not session['old']:
				session['score'] += 1000
				session['old'] = True

			user_id = session["user_id"]
			user = User.query.get(int(user_id))

			return render_template("show_room.html", room=room, options=session['game']['options'])
		else:
			return redirect(url_for("play"))
	else:
		action = request.form.get('action')
		options = []

		if room_name and action:
			room = planisphere.load_room(room_name)
			next_room = scan(action, room)

			# show available options at current room to user
			if "help" in action.lower():
				for i in room.paths:
					options.append(i)
				session['game']['options'] = options

			if not next_room:
				session['room_name'] = planisphere.name_room(room)
				session['old'] = True
			else:
				session['room_name'] = planisphere.name_room(next_room)
				session['old'] = False
				session['game']['options'] = []
		return redirect(url_for("game"))

@app.route("/end", methods=['GET', 'POST'])
def end():
	# Ends the current game session
	session['game']['options'] = []

	session['room_name'] = None
	session['old'] = True

	return redirect(url_for("profile"))
