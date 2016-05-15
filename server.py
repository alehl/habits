from flask import Flask, session, render_template, request, redirect, g, url_for, jsonify
from flask_sqlalchemy import SQLAlchemy
import model
from model import CreatedAchievements, connect_to_db, Users
import os

app = Flask(__name__)
app.secret_key = os.urandom(24)


db = SQLAlchemy()

# These functions create a session for the user.

####################################################

@app.route('/')
def index():

    """Homepage"""

    return "This is the homepage"


####################################################

@app.before_request
def before_request():
    g.user = None
    if 'user' in session:
        g.user = session['user']


####################################################!

@app.route('/login', methods=['GET', 'POST'])
def login():
    """'password' is the default pwd and begins session if entered"""

    if request.method == 'POST':
        session.pop('user', None)

        if request.form['password'] == 'password':
            session['user'] = request.form['username']
            return redirect('/choose_achievement')

    return render_template('index.html')
    
    if 'user' in session:
        return session['user']
    

####################################################!

@app.route('/choose_achievement', methods=['POST', 'GET'])
def chooseachievement():   
    """Two options: create new achievement or select one from the app"""

    username = request.form.get("username")
    password = request.form.get("password")


    # new_user = Users(username=username,
    #                 password=password)

    # db.session.add(new_user)
    # db.session.commit()


    # if g.user:
    if 'user':
        return render_template('choose_achievement.html',
                            username=username,
                            password=password)
        
        return redirect(url_for('index'))



####################################################

@app.route('/logout')
def logout():
    """Logs user out of a session"""

    session.pop('user', None)
    return render_template("homepage.html")


####################################################

@app.route('/results', methods =['GET', 'POST'])
def see_results():
    """This will display the achievement they selected/created"""

    new_achievement = request.values.get('createnew')
    selected_achievement = request.values.get('choosefrom')

    if new_achievement == "new":
        return render_template("create_your_own.html")

    if selected_achievement == "old":
        return render_template("created_achievements.html")

####################################################

@app.route('/created', methods = ['POST'])
def show_created_chosen_achievements():
    """This will handle all submissions from create_your_own.html
     and choose_achievement.html"""

    nameofachievement = request.form.get('nameofachievement')
    weekdays = request.form.get('weekdays')
    recurrence = request.form.get('recurrence')

    # actually add this to db

    new_achievement = CreatedAchievements(
        achievement_name=nameofachievement, 
        weekdays=weekdays,
        recurrence=recurrence)

    db.session.add(new_achievement)
    db.session.commit()

    return render_template('new_achievements.html',
                            nameofachievement = nameofachievement,
                            weekdays = weekdays,
                            recurrence = recurrence)
    
####################################################

if __name__ == '__main__':
    connect_to_db(app)
    app.run(debug=True)

    app.run()

