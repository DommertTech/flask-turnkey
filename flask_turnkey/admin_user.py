# Flask-TurnKey Version 0.0.1
# admin_user.py

# Creates User table and Admin User

from flask import *
from app import *
from auth import auth

auth.User.create_table(fail_silently=True) # make sure table created.
admin = auth.User(username='admin', email='', admin=True, active=True)
admin.set_password('admin')
admin.save()
print('Admin Created! ... Have a nice day')