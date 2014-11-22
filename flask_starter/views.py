# Flask-TurnKey Version 0.0.1
# Views.py

import datetime
from app import app
from auth import auth
from models import User
from flask import request, redirect, url_for, render_template, flash
from flask_turboduck.utils import get_object_or_404, object_list




# Private Area
@app.route('/private/')
@auth.login_required
def private_timeline():
    user = auth.get_logged_in_user()
    return 'PRIVATE!'




# Login Page
@app.route('/login/')
def login():
    return redirect('/accounts/login/')