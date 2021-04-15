# Importing the os module
import os
# Import the json Library
import json
# Importing the Flask class from flask, pulling in a template
# import the 'request' library from Flask. Request is going to
# handle things like finding out what method we used,
# and it will also contain our form object when we've posted it
# Importing flasj to display some feedback to the user
from flask import Flask, render_template, request, flash

# Import env if the system can find an env.py file.

if os.path.exists("env.py"):
    import env


# !!Two blank lines between code blocks & functions to keep PEP8 compliant!!


# Creating an instance of the Flask class and saving it in the variable "app"
app = Flask(__name__)
app.secret_key = os.environ.get("SECRET_KEY")


@app.route("/")  # Decorator
def index():
    return render_template("index.html")


@app.route("/about")  # Decorator
def about():
    data = []
    with open("data/company.json", "r") as json_data:
        data = json.load(json_data)
    return render_template("about.html", page_title="About", company=data)


@app.route("/about/<member_name>")
def about_member(member_name):
    member = {}
    with open("data/company.json", "r") as json_data:
        data = json.load(json_data)
        for obj in data:
            if obj["url"] == member_name:
                member = obj
    return render_template("member.html", member=member)


@app.route("/contact", methods=["GET", "POST"])  # Decorator
def contact():
    if request.method == "POST":
        flash("Thanks {}, we have received your message!".format(
            request.form.get("name")))
    return render_template("contact.html", page_title="Contact")


@app.route("/careers")  # Decorator
def careers():
    return render_template("careers.html", page_title="Careers")


if __name__ == "__main__":  # Main = default module in python
    app.run(  # Run the app using these arguments
        host=os.environ.get("IP", "0.0.0.0"),
        port=int(os.environ.get("PORT", "5000")),
        debug=True  # Debug=True should never be present in a production config
        # also never when we submit our projects for assessment
    )
