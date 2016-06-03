from flask import Flask, session, render_template, request, redirect, g, url_for, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask.ext.babel import Babel, gettext
from model import CreatedAchievements, connect_to_db, User
from flask_debugtoolbar import DebugToolbarExtension
import os, time, datetime

app = Flask(__name__)
babel = Babel(app)
app.secret_key = "os.urandom(24)"


db = SQLAlchemy()

##################################################

@app.route('/')
def index():

    """Homepage"""

    # return "This is the homepage"
    return render_template('index.html')

##################################################

##################################################
@app.route('/choose_achievement')
def chooseachievement():

    """Two options: create new achievement or select one from the app"""

    if g.user:
        return render_template('path_to_wp.html', username=session['user'])

    return redirect(url_for('index'))

##################################################

@app.before_request
def before_request():
    g.user = None
    if 'user' in session:
        g.user = session['user']

##################################################

@app.route('/login', methods=['POST'])
# @app.route('/login')
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
        session['lang'] = 'en'
        return render_template('path_to_wp.html', username=username)


        
##################################################

@app.route('/logout')
def logout():
    """Logs user out of a session"""

    session.pop('user', None)
    return 'Dropped!'

##################################################

@app.route('/set_lang')
def setlang():
    session['lang'] = request.args.get('lang')
    return ""

@babel.localeselector
def get_locale():
    """Direct babel to use the language defined in the session."""

    return g.get('current_lang', session.get('lang','en'))


@app.before_request
def before():
    if request.view_args and 'lang_code' in request.view_args:
        g.current_lang = request.view_args['lang_code']
        session['lang'] = g.current_lang
        request.view_args.pop('lang_code')



@app.route('/<lang_code>/results')
@app.route('/results')
def see_results():   
    print "language:", session['lang']
    new_achievement = request.values.get('createnew')
    selected_achievement = request.values.get('choosefrom')

    if new_achievement == "new":
        return render_template("weekly_planner.html", session=session)


##################################################

@app.route('/created', methods = ['POST', 'GET'])
def show_created_chosen_achievements():
    """This will handle all submissions from weekly_planner.html"""

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
    # now = datetime.datetime.now()
    # today = now.date()
    # moment = now.time()
    return render_template('weekly_planner.html', username=username)
    

################################################## 
if __name__ == '__main__':
    app.debug = True
    connect_to_db(app)

    # DebugToolbarExtension(app)

    app.run()

