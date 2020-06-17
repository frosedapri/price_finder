from flask import Flask, redirect, url_for, render_template, request, session, flash
#from chatterbot import ChatBot
#from chaterbot.trainers import ListTrainer
import os
from datetime import timedelta
from flask_sqlalchemy import SQLAlchemy
import pickle
from flask_socketio import SocketIO, emit
import mymodules as mm

print(mm.levenshtein("bob", "hello"))

app = Flask(__name__)
app.secret_key = "8vyIOl0badS3RgHvpK0wunwlWZjFGhXdQyb1ZtJsNOhKsYKGPSI9jciIl6e4W6IzH8Wd1i22gVYateJAxr7YQxeYhpCqnHKUnItTfIUCRDR6QVPowFyM9Fl2qyAOjLVIM6yS7Ax5WUJjNtz3c3znBvRs0SfStdlPx9AAHD4k8HaM02RaALeaiKfMNfKWd2YUXRqsjUnGUIVt3C8jnEFLPD8cjgyl9rnx2LuL7ihgJ0noBqx2kiXj2yfUje"
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.sqlite3'
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = True
app.permanent_session_lifetime = timedelta(days=5)

db = SQLAlchemy(app)

class users(db.Model):
    _id = db.Column("id", db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    email = db.Column(db.String(100))
    password = db.Column(db.String(100))
    Amazon = db.Column(db.String(250))
    #Ebay = db.Column(db.String(250))

    def __init__(self, name, email, password, Amazon):
        self.name = name
        self.email = email
        self.password = password
        self.Amazon = Amazon
        #self.Ebay = Ebay



@app.route("/")
@app.route("/home")
@app.route("/menu")
def home():
    return render_template("base.html")

@app.route("/view")
def view():
    return render_template("view.html", values=users.query.all())












@app.route("/login", methods=["POST", "GET"])
def login():
    if request.method == "POST":
        session.permanent = True
        user = request.form["nm"]
        session["user"] = user
        found_user = users.query.filter_by(name=user).first()

        if found_user:
            session["email"] = found_user.email
            session["password"] = found_user.password
            session["Amazon"] = found_user.Amazon
            #session["Ebay"] = found_user.Ebay
        else:
            usr = users(user, "", "", "")
            db.session.add(usr)
            db.session.commit()




        flash("Login Succesful!")
        return redirect(url_for("user"))
    else:
        if "user" in session:
            flash("Already Logged In!")
            return redirect(url_for("user"))
        return render_template("login.html")



@app.route("/user", methods=["POST", "GET"])
def user():
    email = None
    if "user" in session:
        user = session["user"]

        if request.method == "POST":
            email = request.form["email"]
            session["email"] = email
            found_user = users.query.filter_by(name=user).first()
            found_user.email = email
            db.session.commit()
            flash("Email was saved!")
            return redirect(url_for("password"))
        else:
            if "email" in session:
                email = session["email"]
        return render_template("user.html", email=email)
    else:
        flash("You are not logged in!")
        return redirect(url_for("login"))




@app.route("/password", methods=["POST", "GET"])

def password():
    password = None
    if "user" in session:
        user = session["user"]

        if request.method == "POST":
            password = request.form["password"]
            session["password"] = password
            found_user = users.query.filter_by(name=user).first()
            found_user.password = password
            db.session.commit()
            flash("Password was saved!")
        else:
            if "password" in session:
                password = session["password"]

        return render_template("password.html", password=password)
    else:
        flash("You are not logged in!")
        return redirect(url_for("login"))

@app.route("/pr_link", methods=["POST", "GET"])
def Product_Links():
    Amazon = None
    if "user" in session:
        user = session["user"]

        if request.method == "POST":
            Amazon = request.form["Amazon"]
            session["Amazon"] = Amazon
            found_user = users.query.filter_by(name=user).first()
            found_user.Amazon = Amazon
            pickle.dump(Amazon, open("Liens.dat", "wb"))
            db.session.commit()
            flash("Amazon link was saved!")
        else:
            if "Amazon" in session:
                Amazon = session["Amazon"]
                pickle.dump(Amazon, open("Liens.dat", "wb"))

        return render_template("Product_link.html", Amazon=Amazon)
    else:
        flash("You are not logged in!")
        return redirect(url_for("login"))

@app.route("/pr_price")
def pr_price():
    converted_price = pickle.load(open("Prix.dat", "rb"))
    return render_template("Product_Price.html", priceA=priceA)



@app.route("/delete")
def delete():
    if "user" in session and "email" in session:
        user = session["user"]
        email = session["email"]
        users.query.filter_by(name=user).delete()
        users.query.filter_by(email=email).delete()
        db.session.commit()
        flash("Record deleted successfully!")
    elif "user" in session and "email" not in session:
        user = session["user"]
    if not users.query.filter_by(name=user).first():
        flash("Unable to delete since there is no record found!")
    else:
        users.query.filter_by(name=user).delete()
        db.session.commit()
        flash("Record deleted successfully!")

    return redirect(url_for("user"))

@app.route("/logout")
def logout():
    if "user" in session:
        user = session["user"]
        flash(f"You have been logged out, {user}", "info")
    session.pop("user", None)
    session.pop("email", None)
    session.pop("password", None)
    session.pop("Amazon", None)
    return redirect(url_for("login"))



@app.route("/pr_links_find", methods=["POST", "GET"])
def find():
    my_list = []
    l = mm.readDocument("data")
    for i in range(len(l)):
        temp_list = []
        temp_list.append(l[i])
        temp_list.append(0)    
        my_list.append(temp_list)
    product = request.form["product"]
    words = my_list
    values = mm.find_closest_words(words, product)
    return render_template("find.html", value=values)






















@app.route("/animation")
def animation():
    return render_template("animation.html")









socketio = SocketIO( app )

@app.route( '/chat' )
def hello():
  return render_template( 'ChatApp.html' )

def messageRecived():
  print( 'message was received!!!' )

@socketio.on( 'my event' )
def handle_my_custom_event( json ):
  print( 'recived my event: ' + str( json ) )
  socketio.emit( 'my response', json, callback=messageRecived )


  



if __name__ == "__main__":
    db.create_all()
    socketio.run( app, debug = True )







