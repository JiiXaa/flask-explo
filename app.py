import os
from flask import Flask, render_template, flash
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

if os.path.exists("env.py"):
    import env

# Create a Flask instance

app = Flask(__name__)
app.secret_key = os.environ.get("SECRET_KEY")

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
    app.run(debug=True)
