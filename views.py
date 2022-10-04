from flask import Blueprint, render_template

views = Blueprint(__name__, "views")

@views.route("/")
def main():
    return render_template("index.html");

@views.route("/Home.html")
def home():
    return render_template("Home.html");