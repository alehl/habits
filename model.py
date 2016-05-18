from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

db = SQLAlchemy()

#######################################
# Model Definitions

class User(db.Model):
	"""Users Table"""

	__tablename__ = "users"

	userid = db.Column(db.Integer, primary_key=True, autoincrement=True)
	username = db.Column(db.String(16), nullable=False, unique=True)


	def __repr__(self):
		return "<Username id=%d name=%s>" % (self.userid, self.username)


def user_info():
	"""Add data to users table"""

	User.query.delete()

	NewU = User(userid='userid',
				username='username')

	db.session.all([NewU])
	db.session.commit()


def set_val_user_id():
    """Set value for the next achievement_id"""

    # Get the Max achievement_id in the database
    result = db.session.query(func.max(User.user_id)).one()
    max_id = int(result[0])

    # Set the value for the next id to be max_id + 1
    query = "SELECT setval('users_user_id_seq', :new_id)"
    db.session.execute(query, {'new_id': max_id + 1})
    db.session.commit()


class CreatedAchievements(db.Model):
	"""Created achievements table"""

	__tablename__ = "created_achievements"

	achievement_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
	achievement_name = db.Column(db.String(30), nullable=False, unique=False)
	recurrence = db.Column(db.String, nullable=False)


	def __repr__(self):
		return "<This is the user's achievement %s>" % (self.achievement_id)


def achievement_info():
	"""Add data to create_achievements table"""

	CreatedAchievements.query.delete()

	NewA = CreatedAchievements(achievement_name='achievement_name',
								recurrence='recurrence')

	db.session.all([NewA])
	db.session.commit()


def set_val_achievement_id():
    """Set value for the next achievement_id"""

    # Get the Max achievement_id in the database
    result = db.session.query(func.max(User.achievement_id)).one()
    max_id = int(result[0])

    # Set the value for the next user_id to be max_id + 1
    query = "SELECT setval('users_user_id_seq', :new_id)"
    db.session.execute(query, {'new_id': max_id + 1})
    db.session.commit()

# Helper functions

def connect_to_db(app):
    """Connect to database"""

    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///achievements'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
    db.app = app
    db.init_app(app)

connect_to_db(app)

db.create_all()