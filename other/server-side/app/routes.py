from webapp import myapp
from flask import *

#when a web browser requests either of these two URLs, Flask is going to invoke this function and pass the return value of it back to the browser as a response.
@myapp.route('/')
def index():
    return render_template("index.html")

@myapp.route('/login')
def login():
     return render_template("login.html")

@myapp.route('/signup')
def signup():
    return render_template("signup.html")

@myapp.route('/account')
def account():
    return render_template("account.html")
