from flask import Flask, render_template, request, redirect, session


app = Flask (__name__)

app.secret_key = "ABC"

@app.route("/")
def homepage():
	"""This is the homepage."""

	return render_template ("homepage.html")









if __name__ == "__main__":
    app.run(debug = True)

