from flask import Flask, session, render_template, request, redirect, g, url_for, jsonify
import os

app = Flask(__name__)
app.secret_key = os.urandom(24)

# These functions create a session for the user. 

@app.route('/', methods=['GET', 'POST'])
def index():

    """Sets 'password' as default password and begins session
    if password is entered correctly"""

    if request.method == 'POST':
        session.pop('user', None)

        if request.form['password'] == 'password':
            session['user'] = request.form['username']
            return redirect('/choose_achievement')

    return render_template('index.html')


@app.route('/choose_achievement')
def chooseachievement():
    """Takes user to page where they can choose whether they want to
    create their own achievement or get a predefined achievement"""

    if g.user:
        return render_template('choose_achievement.html')

    return redirect(url_for('index'))

@app.before_request
def before_request():
    g.user = None
    if 'user' in session:
        g.user = session['user']

@app.route('/login')
def login():
    if 'user' in session:
        return session['user']

    return 'Not logged in!'

@app.route('/dropsession')
def dropsession():
    """Logs user out of a session"""

    session.pop('user', None)
    return 'Dropped!'
        
@app.route('/pick_one', methods =['GET', 'POST'])
def pick_one():
    """This will take the user to the 'create your own' page"""

    return render_template("create_your_own.html")

@app.route('/results')
def see_results():
    """This will display what the user created or the achievement they selected"""

    new_achievement = request.values.get('createnew')
    selected_achievement = request.values.get('choosefrom')

    if new_achievement == "new":
        return render_template("create_your_own.html")

    if selected_achievement == "old":
        return render_template("created_achievements.html")


@app.route('/created', methods = ['GET', 'POST'])
def show_created_chosen_achievements():
    """This will handle all submissions from create_your_own.html
     and choose_achievement.html"""

    nameofachievement = request.form.get('nameofachievement')
    achievementday = request.form.get('achievementday')
    numberftimes = request.form.get('numberftimes')
    recurrence = request.form.get('recurrence')

    return render_template(overview.html,
        nameofachievement = nameofachievement,
        achievementday = achievementday,
        numberftimes = numberftimes,
        recurrence = recurrence)



if __name__ == '__main__':
    app.run(debug=True)

    app.run()