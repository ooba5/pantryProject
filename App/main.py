
from flask import Flask, render_template, session, request, redirect, url_for
import pandas as pd
from settings import Config
import datetime as dt

from utils import Food, Meal
app = Flask('__main__')
app.secret_key = Config.secret
existing_db = pd.read_csv("./foods.csv")
@app.route("/", methods = ("GET", "POST"))
def home():
    existing_db = pd.read_csv("./foods.csv")
    if request.method == "POST":
        loc = request.form["pantryFridgeFreezer"]
        name = request.form["foodName"]
        quantity = request.form["foodQuant"]

        existing_db = pd.concat((existing_db, pd.DataFrame({"name": [name], "price":[0],"location":[loc],
                                                             "quantity":[quantity], "shelf_life": [7], "date_stored":[dt.datetime.date(dt.datetime.now())]})))
        existing_db.to_csv("./foods.csv", index=False)

    return render_template("home.html", pantry=existing_db[existing_db.location=="Pantry"].to_html(),
                           freezer=existing_db[existing_db.location=="Freezer"].to_html(),
                           fridge=existing_db[existing_db.location=="Fridge"].to_html()
    )

app.run()