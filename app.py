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


# ---------- ALL RECIPES ----------
@app.route("/get_recipes")
def get_recipes():
    recipes = list(mongo.db.recipes.find())
    return render_template("recipes.html", recipes=recipes)


# ---------- SEARCH ----------
@app.route("/search", methods=["GET", "POST"])
def search():
    search = request.form.get("search")
    recipes = list(mongo.db.recipes.find({"$text": {"$search": search}}))
    recipesearched = list(mongo.db.recipes.find())
    return render_template("recipes.html", recipes=recipes,
                           recipesearched=recipesearched)


# ---------- SIGN UP ----------
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
        return redirect(url_for("my_recipes", username=session["user"]))

    return render_template("signup.html")


# ---------- LOG IN ----------
@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        # check if username exsits in database
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})

        if existing_user:
            # ensure hashed password matches user input
            if check_password_hash(
                    existing_user["password"], request.form.get("password")):
                session["user"] = request.form.get("username").lower()
                flash("Welcome, {}!".format(request.form.get("username")))
                return redirect(url_for(
                        "my_recipes", username=session["user"]))
            else:
                # invalid password match
                flash("Incorrect username and/or password")
                return redirect(url_for("login"))

        else:
            # username doesn't exist
            flash("Incorrect username and/or password")
            return redirect(url_for("login"))

    return render_template("login.html")


# ---------- MY RECIPES ----------
@app.route("/my_recipes/<username>", methods=["GET", "POST"])
def my_recipes(username):
    # grab the session user's username from db
    username = mongo.db.users.find_one(
            {"username": session["user"]})["username"]
    myrecipes = list(mongo.db.recipes.find({"created_by": session["user"]}))

    if session["user"]:
        return render_template(
                "myrecipes.html", username=username, myrecipes=myrecipes)

    return redirect(url_for("login"))


# ---------- LOGOUT ----------
@app.route("/logout")
def logout():
    # remove user from session cookies
    flash("You have been logged out")
    session.pop("user")
    return redirect(url_for("login"))


# ---------- ADD RECIPE ----------
@app.route("/add_recipe", methods=["GET", "POST"])
def add_recipe():
    # grab the session user's username from db
    username = mongo.db.users.find_one(
            {"username": session["user"]})["username"]

    if request.method == "POST":
        recipe = {
            "category_name": request.form.get("category_name"),
            "recipe_name": request.form.get("recipe_name"),
            "serves": request.form.get("serves"),
            "cooks_in": request.form.get("cooks_in"),
            "ingredients": request.form.getlist("ingredients"),
            "method": request.form.getlist("method"),
            "image": request.form.get("image"),
            "created_by": session["user"]
        }
        mongo.db.recipes.insert_one(recipe)
        flash("Recipe Successfully Added")
        return redirect(url_for("my_recipes", username=username))

    categories = mongo.db.categories.find().sort("category_name", 1)
    return render_template("add_recipe.html", categories=categories,
                           username=username)


# ---------- EDIT RECIPE ----------
@app.route("/edit_recipe/<recipe_id>", methods=["GET", "POST"])
def edit_recipe(recipe_id):
    # grab the session user's username from db
    username = mongo.db.users.find_one(
            {"username": session["user"]})["username"]

    if request.method == "POST":
        submit = {
            "category_name": request.form.get("category_name"),
            "recipe_name": request.form.get("recipe_name"),
            "serves": request.form.get("serves"),
            "cooks_in": request.form.get("cooks_in"),
            "ingredients": request.form.getlist("ingredients"),
            "method": request.form.getlist("method"),
            "image": request.form.get("image"),
            "created_by": session["user"]
        }
        mongo.db.recipes.update({"_id": ObjectId(recipe_id)}, submit)
        flash("Recipe Successfully Updated")
        return redirect(url_for("my_recipes", username=username))

    recipe = mongo.db.recipes.find_one({"_id": ObjectId(recipe_id)})
    categories = mongo.db.categories.find().sort("category_name", 1)
    return render_template("edit_recipe.html", recipe=recipe,
                           categories=categories, username=username)


# ---------- DELETE RECIPE ----------
@app.route("/delete_recipe/<recipe_id>", methods=["GET", "POST"])
def delete_recipe(recipe_id):
    # grab the session user's username from db
    username = mongo.db.users.find_one(
            {"username": session["user"]})["username"]

    mongo.db.recipes.remove({"_id": ObjectId(recipe_id)})
    flash("Recipe Successfully Deleted")
    return redirect(url_for("my_recipes", username=username))


# ---------- FULL RECIPE ----------
@app.route("/full_recipe/<recipe_id>")
def full_recipe(recipe_id):

    recipe = mongo.db.recipes.find_one({"_id": ObjectId(recipe_id)})

    fullrecipes = mongo.db.recipes.find({"_id": ObjectId(recipe_id)})

    # Search for keywords functionality
    # - gets all records with the keywords
    adsearch = list(mongo.db.recipes.find({"$text": {"$search": "mix mixer"}}))

    # ----- CODE CREDIT -----
    # - gets the list of only _id: value pairs of those records
    # https://stackoverflow.com/questions/13254241/removing-key-values-pairs-from-a-list-of-dictionaries
    idvalues = [{k: v for k, v in d.items() if k == '_id'} for d in adsearch]

    # - turns the list of dicts into the list of "_id" values
    # https://stackoverflow.com/questions/20891141/convert-list-of-dicts-to-list
    adverts = []
    for idvalue in idvalues:
        adverts.append(idvalue["_id"])

    # ----- END OF CODE CREDIT -----

    # - joins lists into strings
    allingredients_list = recipe.get("ingredients")
    ingredients = ''.join(allingredients_list)

    allmethods_list = recipe.get("method")
    methods = ''.join(allmethods_list)

    return render_template("full_recipe.html",
                           recipe=recipe, fullrecipes=fullrecipes,
                           adverts=adverts, ingredients=ingredients,
                           methods=methods)


# ---------- CATEGORIES ----------
@app.route("/get_categories")
def get_categories():
    username = mongo.db.users.find_one(
            {"username": session["user"]})["username"]
    categories = list(mongo.db.categories.find().sort("category_name", 1))
    return render_template("categories.html", categories=categories,
                           username=username)


# ---------- ADD CATEGORY ----------
@app.route("/add_category", methods=["GET", "POST"])
def add_category():
    username = mongo.db.users.find_one(
            {"username": session["user"]})["username"]

    if request.method == "POST":
        category = {
            "category_name": request.form.get("category_name")
        }
        mongo.db.categories.insert_one(category)
        flash("New Category Added")
        return redirect(url_for("get_categories"))

    return render_template("add_category.html", username=username)


# ---------- EDIT CATEGORY ----------
@app.route("/edit_category/<category_id>", methods=["GET", "POST"])
def edit_category(category_id):
    username = mongo.db.users.find_one(
            {"username": session["user"]})["username"]

    if request.method == "POST":
        submit = {
            "category_name": request.form.get("category_name")
        }
        mongo.db.categories.update({"_id": ObjectId(category_id)}, submit)
        flash("Category Successfully Updated")
        return redirect(url_for("get_categories"))

    category = mongo.db.categories.find_one({"_id": ObjectId(category_id)})
    return render_template("edit_category.html", category=category,
                           username=username)


# ---------- DELETE CATEGORY ----------
@app.route("/delete_category/<category_id>")
def delete_category(category_id):
    mongo.db.categories.remove({"_id": ObjectId(category_id)})
    flash("Category Successfully Deleted")
    return redirect(url_for("get_categories"))


# ---------- CONTACT PAGE ----------
@app.route("/contact")
def contact():
    return render_template("contact.html")


# ---------- CODE CREDIT ----------
# https://www.geeksforgeeks.org/python-404-error-handling-in-flask/

# ---------- 404 PAGE ----------
@app.errorhandler(404)
def not_found(e):
    return render_template("404.html")

# ---------- END OF CODE CREDIT ----------


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=False)