from flask import Flask, session, render_template, request, redirect, g, url_for, jsonify
from flask_sqlalchemy import SQLAlchemy
from model import CreatedAchievements, connect_to_db, User
import os

app = Flask(__name__)
app.secret_key = os.urandom(24)


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
        #     Clear the feild in the form
        #     display an error

##################################################

@app.route('/logout')
def logout():
    """Logs user out of a session"""

    session.pop('user', None)
    return 'Dropped!'

##################################################

@app.route('/pick_one', methods =['GET', 'POST'])
def pick_one():
    """This will take the user to the 'create your own' page"""

    return render_template("create_your_own.html")

##################################################

@app.route('/results')
def see_results():
    """This will display what the user created or the achievement they selected"""

    new_achievement = request.values.get('createnew')
    selected_achievement = request.values.get('choosefrom')

    if new_achievement == "new":
        return render_template("create_your_own.html")

    if selected_achievement == "old":
        return render_template("created_achievements.html")

##################################################

@app.route('/created', methods = ['POST'])
def show_created_chosen_achievements():
    """This will handle all submissions from create_your_own.html
     and choose_achievement.html"""

    nameofachievement = request.form.get('nameofachievement')
    recurrence = request.form.get('recurrence')

    # actually add this to db

    new_achievement = CreatedAchievements(
        achievement_name=nameofachievement,
        recurrence=recurrence)

    db.session.add(new_achievement)
    db.session.commit()

    return render_template('new_achievements.html',
                            nameofachievement = nameofachievement,
                            recurrence = recurrence)


################################################## 



if __name__ == '__main__':
    connect_to_db(app)
    app.run(debug=True)

    app.run()

