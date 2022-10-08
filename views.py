from flask import Blueprint, render_template

views = Blueprint(__name__, "views")

@views.route("/")
def main():
    return render_template("index.html")

@views.route("/academics")
def academics():
    return render_template("Academics.html")

@views.route("/athletics")
def athletics():
    return render_template("Athletics.html")

@views.route("/other_interests")
def hobbies_interests():
    return render_template("Hobbies+Interests.html")