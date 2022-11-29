from datetime import datetime
from flask import Flask, render_template, url_for, flash, redirect
from api.controllers.login_controller import LoginController
from api.controllers.registration_controller import RegistrationController


# Create a Flask Instance
app = Flask(__name__)

# set secret key
app.config['SECRET_KEY'] = '4629c8cd6e0a2bdcd746587bf987093e'


# All routes
@app.route('/')
def index():
    return render_template('index.html', title="MyFlaskBlog")


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/registration', methods=['GET', 'POST'])
def registration(): 
    form = RegistrationController()
    if form.validate_on_submit():
        flash(f'Account created for {form.username.data}!', 'success')
        return redirect(url_for('index'))

    return render_template('register.html', title="Registration", form=form)


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginController()
    if form.validate_on_submit():
        if form.email == 'admin@gmail.com' and form.password == "1234":
            flash(f'You have beeb logged in!', 'success')
            return redirect(url_for('index'))
        else:
            flash(f'Login is failed. Please check the email and password', 'danger')

    return render_template('login.html', title="Login", form=form)


# Create custom error page
@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html", title="404"), 404


# Internal server error
@app.errorhandler(500)
def page_not_found(e):
    return render_template("500.html", title="500"), 500




