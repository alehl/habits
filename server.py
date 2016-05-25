from flask import Flask, session, render_template, request, redirect, g, url_for, jsonify
from flask_sqlalchemy import SQLAlchemy
from model import CreatedAchievements, connect_to_db, User
from flask_debugtoolbar import DebugToolbarExtension
import os

app = Flask(__name__)
app.secret_key = "os.urandom(24)"


db = SQLAlchemy()

##################################################

@app.route('/')
def index():

    """Homepage"""

    # return "This is the homepage"
    return render_template('index.html')

##################################################

@app.route('/choose_achievement')
def chooseachievement():

    """Two options: create new achievement or select one from the app"""

    if g.user:
        return render_template('choose_achievement.html', username=session['user'])

    return redirect(url_for('index'))

##################################################

@app.before_request
def before_request():
    g.user = None
    if 'user' in session:
        g.user = session['user']

##################################################

@app.route('/login', methods=['POST'])
def login():
    """'password' is the default pwd and begins session if entered"""

    # if request.method == 'POST':
    #     session.pop('user', None)
    print "In login route"

    if request.form['password'] == 'password':
        print "Password token"
        session['user'] = request.form['username']


# if 'user' in session:
#     return session['user']

# return 'Not logged in!'

#This adds the username to db if it's not there already.

        username = request.form.get("username")
        password = request.form.get("password")

        checks = User.query.filter_by(username=session['user']).first()

        if checks == None:

            new_user = User(username=username)

            db.session.add(new_user)
            db.session.commit()
            print "added to DB"

        return render_template('choose_achievement.html', username=username)
        
        # else:
        #     Clear the field in the form
        #     display an error

##################################################

@app.route('/logout')
def logout():
    """Logs user out of a session"""

    session.pop('user', None)
    return 'Dropped!'

##################################################

@app.route('/results')
def see_results():
    """This will display what the user created or the achievement they selected"""

    new_achievement = request.values.get('createnew')
    selected_achievement = request.values.get('choosefrom')

    if new_achievement == "new":
        return render_template("new_achievements.html")

    if selected_achievement == "old":
        return render_template("created_achievements.html")


##################################################

@app.route('/created', methods = ['POST'])
def show_created_chosen_achievements():
    """This will handle all submissions from new_achievements.html"""
    print "in created route"

    mo_goal = request.form.get('name1')
    mo_notes = request.form.get('data1')
    tu_goal = request.form.get('name2')
    tu_notes = request.form.get('data2')
    we_goal = request.form.get('name3')
    we_notes = request.form.get('data3')
    th_goal = request.form.get('name4')
    th_notes = request.form.get('data4')
    fr_goal = request.form.get('name5')
    fr_notes = request.form.get('data5')
    sa_goal = request.form.get('name6')
    sa_notes = request.form.get('data6')
    su_goal = request.form.get('name7')
    su_notes = request.form.get('data7')
    print "in created route"
    print mo_notes, mo_goal, tu_notes, tu_goal, su_notes, su_goal
    # actually add this to db

    new_achievement = CreatedAchievements(mo_goal=mo_goal, mo_notes=mo_notes,
                                        tu_goal=tu_goal, tu_notes=tu_notes,
                                        we_goal=we_goal, we_notes=we_notes,
                                        th_goal=th_goal, th_notes=th_notes,
                                        fr_goal=fr_goal, fr_notes=fr_notes,
                                        sa_goal=sa_goal, sa_notes=sa_notes,
                                        su_goal=su_goal, su_notes=su_notes)

    db.session.add(new_achievement)
    db.session.commit()

    username=session['user']

    return render_template('new_achievements.html', username=username)


################################################## 
if __name__ == '__main__':
    app.debug = True
    connect_to_db(app)

    DebugToolbarExtension(app)

    app.run()

