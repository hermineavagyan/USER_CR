from flask_app import app # NEED this line
from flask import render_template, redirect, request
from flask_app.models.dojo import Dojo # Import each model needed here!
from flask_app.models.ninja import Ninja

@app.route("/")
def ninjas_index():
    return redirect('/dojos')

# Page for adding a ninja - HTML
@app.route("/new_ninja")
def new_ninja_page():
    all_dojos = Dojo.get_all()
    return render_template("ninja_page.html", dojos = all_dojos)


@app.route('/create_ninja', methods=["POST"])
def create_ninja():
    data = {
        "first_name": request.form["first_name"],
        "last_name": request.form["last_name"],
        "age": request.form["age"],
        "dojo_id": request.form["dojo_id"],
    }
    
    new_ninja_id = Ninja.create_one(data)
    dojo_id = request.form["dojo_id"]
    print(new_ninja_id)
    # return redirect('/dojos')
    return redirect(f"/show/{dojo_id}")

