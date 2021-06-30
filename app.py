import os
from flask import (
    Flask, flash, render_template,
    redirect, request, session, url_for)
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from werkzeug.security import generate_password_hash, check_password_hash
if os.path.exists("env.py"):
    import env

app = Flask(__name__)

app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.config["SECRET_KEY"] = os.environ.get("SECRET_KEY")

mongo = PyMongo(app)


# ---------- LANDING PAGE ----------
@app.route("/")
@app.route("/landing")
def landing():
    return render_template("landing.html")


# ---------- ALL RECIPES PAGE ----------
@app.route("/get_recipes")
def get_recipes():
    recipes = mongo.db.recipes.find()
    return render_template("recipes.html", recipes=recipes)


# ---------- SIGN UP PAGE ----------
@app.route("/signup", methods=["GET", "POST"])
def signup():
    if request.method == "POST":
        # check if username already exsits in database
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})

        if existing_user:
            flash("Username already exists")
            return redirect(url_for("signup"))

        signup = {
            "username": request.form.get("username").lower(),
            "password": generate_password_hash(request.form.get("password"))
        }

        mongo.db.users.insert_one(signup)

        # put the new user into 'session cookie'
        session["user"] = request.form.get("username").lower()
        flash("You have signed up successfully!")

    return render_template("signup.html")


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)