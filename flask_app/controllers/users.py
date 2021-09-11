from flask_app import app
from flask import render_template,redirect,request,session,flash
from models.user import User


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

@app.route('/edit/<int:id>')
def edit(id):
    data = {
        "id":id
    }
    fries = User.show(data)
    return render_template('edit.html', user = fries)


@app.route('/edited', methods=["POST"])
def edited():
    data = {
        "id" : request.form["id"],
        "fname": request.form["fname"],
        "lname" : request.form["lname"],
        "email" : request.form["email"]
    }
    User.edit(data)
    return redirect('/')


@app.route('/show/<int:user_id>')
def show(user_id):
    data={
        "id":user_id
    }
    return render_template("show.html", user=User.show(data))


@app.route('/create_user')
def create_user():
    return render_template("create.html")


@app.route('/delete/<int:id>')
def delete(id):
    data={
        "id" : id
    }
    User.delete(data)
    return render_template("delete.html")