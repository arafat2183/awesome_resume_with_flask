from flask import Flask, render_template

# Create a Flask Instance
app = Flask(__name__)

# Create a route decorator

@app.route('/')


def index():
    return render_template("index.html")


#Create custom error page
@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html"), 404

#internal server error
@app.errorhandler(500)
def page_not_found(e):
    return render_template("500.html"), 500














