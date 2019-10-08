from . import app, db
from flask import render_template, redirect, url_for, request, session
from werkzeug.security import generate_password_hash, check_password_hash
from .models import User
from flask_login import login_user, logout_user, login_required


@app.route('/')
def index():
	return render_template('home.html')

@app.route('/profile')
@login_required
def profile():
	user_id = session["user_id"]
	user = User.query.get(int(user_id))
	return render_template('profile.html', name=user.name, hscore=user.highscore)


@app.route('/login', methods=['GET', 'POST'])
def login():
	if request.method == 'POST':
		name = request.form.get('name')
		email = request.form.get('email')
		password = request.form.get('password')
		remember = True if request.form.get('remember') else False
		
		user = User.query.filter_by(name=name).first()
		
		if not user or not check_password_hash(user.password, password):
			return redirect(url_for('login'))
		
		login_user(user, remember=remember)
		return redirect(url_for('profile'))
	else:
		return render_template('login.html')
	
@app.route('/signup', methods=['GET', 'POST'])
def signup():
	if request.method == 'POST':
		email = request.form.get('email')
		name = request.form.get('name')
		password = request.form.get('password')
		
		user = User.query.filter_by(email=email).first()
		
		if user:
			return redirect(url_for('signup'))
		
		new_user = User(email=email, name=name, password=generate_password_hash(password, method='sha256'))

		db.session.add(new_user)
		db.session.commit()
		
		return redirect(url_for('login'))
	else:
		return render_template('signup.html')


@app.route('/logout')
@login_required
def logout():
	logout_user()
	return render_template('home.html')
	
	
@app.route('/reset')
@login_required
def reset():
	user = User.query.get(int(session["user_id"]))
	user.highscore = 0
	db.session.commit()

	return render_template('profile.html', name=user.name, hscore=user.highscore)