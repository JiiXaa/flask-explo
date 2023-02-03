import os
from flask import Flask, render_template, flash, redirect, url_for
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

# database imports
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import desc

# import the datetime module to get the current date and time for the database timestamp field
from datetime import datetime

if os.path.exists("env.py"):
    import env

# Create a Flask instance
app = Flask(__name__)
# Set the database URI
# app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get("DATABASE_URL")
app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get("MYSQL_URL")

# Secret key is used to protect the application against modification of cookies and cross-site request forgery attacks
app.secret_key = os.environ.get("SECRET_KEY")

# Create a database instance
db = SQLAlchemy(app)

# Create a database model
class User(db.Model):
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(50), nullable=False, unique=True)
    date_added = db.Column(db.DateTime, default=datetime.utcnow)

    # Create a string representation of the database model
    def __repr__(self):
        return f"{self.name} {self.email} {self.date_added}"
        return "<Name %r>" % self.name

    # Create a constructor to initialize the database fields when creating a new user object in the database model
    # def __init__(self, name, email):
    #     self.name = name
    #     self.email = email


# with app.app_context():
#     db.create_all()
#     # Insert some sample data into the "users" table
#     user1 = User(name="Tom", email="tom@example.com")
#     user2 = User(name="Oli", email="oli@example.com")
#     db.session.add(user1)
#     db.session.add(user2)
#     db.session.commit()

# with app.app_context():
#     # Query the "users" table and print its contents
#     users = User.query.all()
#     for user in users:
#         print(f"Username: {user.name}, Email: {user.email}")


# Create a form class
class UserForm(FlaskForm):
    name = StringField("Name", validators=[DataRequired()])
    email = StringField("Email", validators=[DataRequired()])
    submit = SubmitField("Submit")


# Create a form class
class NameForm(FlaskForm):
    name = StringField("What is your name?", validators=[DataRequired()])
    submit = SubmitField("Submit")


# Create a route decorator
@app.route("/")
def index():
    user = "Tomm"
    names_list = ["John", "Mary", "Jane", "Bob"]
    return render_template("index.html", names=names_list, user=user)


@app.route("/user/add", methods=["GET", "POST"])
def add_user():
    name = None
    form = UserForm()
    if form.validate_on_submit():
        # Check if the user already exists in the database
        user = User.query.filter_by(email=form.email.data).first()
        if user:
            flash("User already exists!")
            return redirect(url_for("add_user"))
        else:
            name = form.name.data
            email = form.email.data
            # Create a new user object
            user = User(name=name, email=email)
            # Add the new user object to the database
            db.session.add(user)
            # Commit the changes to the database
            db.session.commit()
            name = form.name.data
            # set the name data to an empty string so that the form is cleared
            form.name.data = ""
            form.email.data = ""
            flash("User added successfully!")
            # return redirect(url_for("users"))
    our_users = User.query.order_by(desc(User.date_added))
    return render_template("add_user.html", form=form, name=name, our_users=our_users)


@app.route("/users")
def users():
    users = User.query.all()
    return render_template("users.html", users=users)


# Dynamic route with a user name
@app.route("/user/<name>")
def user(name):
    return render_template("user.html", user_name=name)


@app.route("/name", methods=["GET", "POST"])
def name():
    # set name to None so that it is not undefined in the template
    name = None
    form = NameForm()
    # validate_on_submit() method checks if the form has been submitted and if all the validators pass
    if form.validate_on_submit():
        name = form.name.data
        # set the name data to an empty string so that the form is cleared
        form.name.data = ""

        # flash a message to the user
        flash("Form submitted successfully!")
    return render_template("name.html", name=name, form=form)


@app.errorhandler(404)
def page_not_found(error):
    return render_template("404.html"), 404


@app.errorhandler(500)
def internal_error(error):
    return render_template("500.html"), 500


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"), port=int(os.environ.get("PORT")), debug=True)
