# Flask-TurnKey Version 0.0.1
# App.py

# Flask
from flask import Flask
# Flask-TurboDuck
from flask_turboduck.db import Database

app = Flask(__name__)
app.config.from_object('config.Configuration')

db = Database(app)

def create_tables():
    User.create_table()
