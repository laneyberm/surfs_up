# Import the dependancies
from flask import Flask

app = Flask(__name__)

# Define the root
@app.route('/')
def hello_world():
    return 'Hello world'

# Skill Drill
# Simple code from which you could create a route