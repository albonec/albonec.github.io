from flask import Blueprint, render_template, request, jsonify, redirect, url_for

views = Blueprint(__name__, "views")

@views.route("/views")
def home():
    return render_template("index.html", name="Alessandro");

@views.route("/views/profile")
def profile():
    return render_template("profile.html");

@views.route("/json")
def getJson():
    return jsonify({'name': 'vladimir', 'soviet': True})


@views.route("/data")
def getIncomingData():
    data = request.json
    return jsonify(data)

@views.route("/views/go-to-homepage")
def goToHomepage():
    return redirect(url_for("views.getJson"))
