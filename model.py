from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

db = SQLAlchemy()

#######################################
# Model Definitions

# class Users(db.Model):
# 	"""Users Table"""

# 	__tablename__ = "users"

# 	id = db.Column(db.Integer, primary_key=True, autoincrement=True)
# 	username = db.Column(db.String(16), nullable=False, unique=True)
# 	password = db.Column(db.String(16), nullable=False, default='password')
# 	achievement_id = db.Column(db.Integer, db.ForeignKey('CreatedAchievements.achievement_id'))

# 	created_a = db.relationship('CreatedAchievements')

# 	def __init__(self, id, username, password, achievement_id):
# 		self.id = id
# 		self.username = username
# 		self.password = password
# 		self.achievement_id = achievement_id

# 	def __repr__(self):
# 		return "<Username id=%d name=%s>" % (self.id, self.username)



class CreatedAchievements(db.Model):
	"""Created achievements table"""

	__tablename__ = "created_achievements"

	achievement_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
	achievement_name = db.Column(db.String(30), nullable=False, unique=True)
	weekdays = db.Column(db.String, nullable=False)
	recurrence = db.Column(db.String, nullable=False)

	# def __init__(self, achievement_name, weekdays, recurrence):
	# 	self.achievement_id = achievement_id
	# 	self.achievement_name = achievement_name
	# 	self.weekdays = weekdays
	# 	self.recurrence = recurrence

	def __repr__(self):
		return "<This is the user's achievement %s>" % (self.achievement_id)


def achievement_info():
	"""add data to database"""

	CreatedAchievements.query.delete()

	NewA = CreatedAchievements(achievement_name='achievement_name', 
							weekdays='weekdays',
							recurrence='recurrence')

	db.session.all([NewA])
	db.session.commit()


# class InspirationAchievements(db.Model):
# 	"""Inspirational Achievements"""

# 	__tablename__ = "Inspirational"

# 	inspiration_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
# 	inspiration_name = db.Column(db.String(30), nullable=False, unique=True)

# 	def __init__(self, inspiration_id, inspiration_name)
# 		self.inspiration_id = inspiration_id
# 		self.inspiration_name = inspiration_name

# 	def __repr__(self):
# 		return "<Great, you created an app %s>" % (self.inspiration_name)


# Helper functions

def connect_to_db(app):
    """Connect to database"""

    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///achievements'
    app.config['SQLALCHEMY_ECHO'] = True
    # app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.app = app
    db.init_app(app)

connect_to_db(app)

db.create_all()
