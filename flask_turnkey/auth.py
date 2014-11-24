# Flask-TurnKey Version 0.0.1
# Auth.py

from flask_turboduck.auth import Auth

from app import app, db
from models import User

# Authentication wrapper for TurboDuck
auth = Auth(app, db, user_model=User)
