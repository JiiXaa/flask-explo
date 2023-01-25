from flask import Flask, render_template

# Create a Flask instance

app = Flask(__name__)

# Create a route decorator
@app.route("/")
def index():
    user = "Tomm"
    names_list = ["John", "Mary", "Jane", "Bob"]
    return render_template("index.html", names=names_list, user=user)


@app.route("/user/<name>")
def user(name):
    return render_template("user.html", user_name=name)


@app.errorhandler(404)
def page_not_found(error):
    return render_template("404.html"), 404


@app.errorhandler(500)
def internal_error(error):
    return render_template("500.html"), 500


if __name__ == "__main__":
    app.run(debug=True)
