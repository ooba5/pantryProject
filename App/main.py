
from flask import Flask, render_template, session, request,redirect, url_for

from settings import Config
from utils import Food, Meal
app = Flask('__main__')
app.secret_key = Config.secret

@app.route("/")
def home():

    return render_template("home.html")

app.run()