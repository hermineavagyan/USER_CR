# burgers.py

from flask import render_template,redirect,request,session,flash
from flask_app import app
from flask_app.models.user import User

# from models.user import User

@app.route("/")
def index():
    return redirect('/users')

@app.route('/users')
def read_all_users():
    # call the get all classmethod to get all friends
    users = User.get_all()
    return render_template("readAll.html", all_users = users)

@app.route('/show/<int:user_id>')
def user_detail_page(user_id):
    data = {
        'id': user_id
    }
    return render_template("user_details_page.html", user = User.get_one(data))

@app.route('/new/user')
def new():
    return render_template("create.html")


@app.route('/create/user', methods=["POST"])
def create_user():
    data = {
        "fname": request.form["fname"],
        "lname" : request.form["lname"],
        "email" : request.form["email"]
    }
    User.save(data)
    return redirect('/users')

@app.route('/users/<int:id>/edit_page')
def edit_user_page(id):
    data = {
        "id": id,
    }
    user = User.get_one(data)
    return render_template("edit_user.html", user = user)


@app.route('/users/<int:id>/edit', methods = ["GET","POST"])
def edit_user(id):
    data = {
        "id":id,
        "first_name": request.form["first_name"],
        "last_name": request.form["last_name"],
        "email": request.form["email"],
    }
    User.update(data)# saves the changes for this user
    return redirect('/users')

# @app.route('/delete/<int:user_id>')
@app.route('/users/<int:user_id>/delete', methods = ["POST"])
def delete_user(user_id):
    data = {
        'id': user_id
    }
    User.delete(data)
    # return redirect('/users')
    return redirect('/users')