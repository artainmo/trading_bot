#environment variable export FLASK_APP=flask_call:myapp
from flask import *

myapp = Flask(__name__) # Flask uses the location of the module passed here as a starting point when it needs to load associated resources

from app import routes #Routes are the different URLs that the application implements
