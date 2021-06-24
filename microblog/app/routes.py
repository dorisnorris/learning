from flask import render_template
from app import app

@app.route('/')
@app.route('/index')
def index():
	user = {'username': 'Doris'}
	posts = [
		{
			'author': {'username': 'John'},
			'body': 'Beautiful day in Santa Cruz!'
		},
		{
			'author': {'username': 'Susan'},
			'body': 'The Avengers movie was so cool!'
		},
		{
			'author': {'username': 'Daniel'},
			'body': 'Venus was super bright last night! Did anyone else see it?'
		}
	]
	return render_template('index.html', title='Home', user=user, posts=posts)

	