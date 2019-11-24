from flask import Flask, session, redirect, url_for, escape, request, render_template
from flask_sqlalchemy import SQLAlchemy
from gothonweb import planisphere
from flask_login import LoginManager

db = SQLAlchemy()
app = Flask(__name__)

from web_app import main, app, web_engine

def main():
	app.config['SECRET_KEY'] = 'A0Zr98j/1234f3gpl[.;[ca3yX R~XHH!jmN]LWciudv=c-ls-c0sjX/,?RT'
	app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite'

	db.init_app(app)

	login_manager = LoginManager()
	login_manager.login_view = 'login'
	login_manager.init_app(app)

	from .models import User

	@login_manager.user_loader
	def load_user(user_id):
		return User.query.get(int(user_id))

	return app

main()
