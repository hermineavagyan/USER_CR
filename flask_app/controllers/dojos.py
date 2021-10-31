from flask_app import app # NEED this line
from flask import render_template, redirect, request
from flask_app.models.dojo import Dojo # Import each model needed here!
from flask_app.models.ninja import Ninja

@app.route("/")
def index():
    return redirect('/dojos')

@app.route('/dojos')
def read_all_dojos():
    dojos = Dojo.get_all()
    return render_template("readAll.html", all_dojos = dojos)

@app.route('/show/<int:id>')
def dojo_show_page(id):
    data = {
        'id': id,
    }
    dojo_with_ninjas = Dojo.get_one_with_ninjas(data)
    return render_template("dojo_show.html", dojo = dojo_with_ninjas )

@app.route('/create/dojo', methods=["POST"])
def create_dojo():
    data = {
        "name": request.form["name"]
    }
    Dojo.create(data)
    return redirect('/dojos')

@app.route('/dojos/<int:id>/delete', methods = ["POST"])
def delete_dojo(id):
    data = {
        'id':id
    }
    Dojo.delete(data)
    return redirect('/dojos')