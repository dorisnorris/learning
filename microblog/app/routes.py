from flask import render_template
from app import app
import forms.LoginForm as LoginForm


@app.route('/login')
def login():
	form = LoginForm()
	return render_template('login.html', title='Sign In', form=form)