from flask import Blueprint, render_template, request, jsonify, redirect, url_for

views = Blueprint(__name__, "views")

@views.route("/")
def home():
    return render_template("index.html", name="name");

@views.route("/json")
def getJson():
    return jsonify({'name': 'vladimir', 'soviet': True})


@views.route("/data")
def getIncomingData():
    data = request.json
    return jsonify(data)

@views.route("/go-to-homepage")
def goToHomepage():
    return redirect(url_for("views.getJson"))
