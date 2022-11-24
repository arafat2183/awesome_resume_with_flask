from datetime import datetime
from flask import Flask, render_template, url_for, flash, redirect
from api.controllers.login_controller import login_controller

# Create a Flask Instance
app = Flask(__name__)

# Create a route decorator

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/about')
def about():
    return render_template('about.html')

    

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = login_controller()
    return render_template('login.html', title="Login", form=form)



#Create custom error page
@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html", title="404"), 404

#internal server error
@app.errorhandler(500)
def page_not_found(e):
    return render_template("500.html", title="500"), 500




