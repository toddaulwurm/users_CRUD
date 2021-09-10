from flask import Flask, render_template, redirect, request
from user import User
app = Flask(__name__)

@app.route("/")
def index():
    user = User.get_all()
    print(user)
    return render_template("index.html", all_users = user)

@app.route('/created', methods=["POST"])
def created():
    data = {
        "fname": request.form["fname"],
        "lname" : request.form["lname"],
        "email" : request.form["email"]
    }
    User.save(data)
    return redirect('/')

@app.route('/create_user')
def create_user():

    return render_template("create.html")




if __name__ == "__main__":
    app.run(debug=True)

