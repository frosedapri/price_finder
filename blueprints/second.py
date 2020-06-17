from flask import Blueprint, render_template

second = Blueprint("second", __name__, static_folder="static", template_folder="")

@second.route("/home")
@second.route("/")
def home():
    render_template("home.html")