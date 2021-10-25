from flask import Flask, render_template, request, redirect
# import the class from friend.py
from user import User
app = Flask(__name__)
@app.route("/")
def index():
    return redirect('/users')

@app.route('/users')
def read_all_users():
    # call the get all classmethod to get all friends
    users = User.get_all()
    return render_template("readAll.html", all_users = users)

@app.route('/new/user')
def new():
    return render_template("create.html")


@app.route('/create/user', methods=["POST"])
def create_user():
    # we create a data dictionary from our request.form coming from our template.
    # The keys in data need to line up exactly with the variables in our query string.
    data = {
        "fname": request.form["fname"],
        "lname" : request.form["lname"],
        "email" : request.form["email"]
    }
    # We pass the data dictionary into the save method from the Friend class.
    
    User.save(data)
    # Don't forget to redirect after saving to the database.
    return redirect('/users')
    
            
if __name__ == "__main__":
    app.run(debug=True)