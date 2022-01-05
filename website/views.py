# the website pages (the blueprint) are set-up in views.py
from flask import Blueprint, render_template

views = Blueprint("views", __name__) # usually easier to name this variable with the same name of the file

@views.route("/") # homepage
def home():
    return (render_template("home.html"))



