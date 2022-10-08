from flask import Blueprint, render_template

views = Blueprint(__name__, "views")

@views.route("/")
def main():
    return render_template("index.html")

@views.route("/Academics.html")
def academics():
    return render_template("Academics.html")

@views.route("/Athletics.html")
def athletics():
    return render_template("Athletics.html")

@views.route("/Hobbies+Interests.html")
def hobbies_interests():
    return render_template("Hobbies+Interests.html")