import os
basedir = os.path.abspath(os.path.dirname(__file__))

# this class will store configuration variables
class Config(object):
	SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'
	SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
		'sqlite:///' + os.path.join(basedir, 'app.db')
	SQALCHEMY_TRACK_MODIFICATIONS = False