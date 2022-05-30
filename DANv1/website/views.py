from flask import Blueprint, render_template

views = Blueprint('views', __name__)

@views.route('/')
def home():
    return render_template("home.html")

@views.route('/login')
def login():
    return render_template("login.html")

@views.route('/about')
def about():
    return render_template("about.html")

@views.route('/dogs')
def dogs():
    return render_template("dogs.html")