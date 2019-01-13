from flask import Flask, render_template, request
from models import db, User
from forms import SignupForm

# This is how you define this script is a Flask application
app = Flask(__name__)
db.init_app(app)

# Application database configuration
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://localhost/learningflask'
app.secret_key = "development-key"

# Home route
@app.route("/")
def index():
    return render_template("index.html")

# About route
@app.route("/about")
def about():
    return render_template("about.html")

# Signup route
@app.route("/signup", methods=['GET', 'POST'])
def signup():
    form = SignupForm()

    if request.method == 'POST':
        if form.validate() == False:
            return render_template("signup.html", form=form)
        else:
            return 'Success!'
    elif request.method == 'GET':
        return render_template("signup.html", form=form)


if __name__ == '__main__':
    app.run(debug=True)