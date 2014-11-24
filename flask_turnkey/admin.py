# Flask-TurnKey Version 0.0.1
# Admin.py

import datetime
from app import app, db
from auth import auth
from models import User
from flask import request, redirect
from flask_turboduck.admin import Admin, ModelAdmin, AdminPanel

admin = Admin(app, auth, branding='Example Site')

class UserStatsPanel(AdminPanel):
    template_name = 'admin/user_stats.html'

    def get_context(self):
        last_week = datetime.datetime.now() - datetime.timedelta(days=7)
        signups_this_week = User.select().where(User.join_date > last_week).count()
        messages_this_week = Note.select().where(Note.created > last_week).count()
        return {
            'signups': signups_this_week,
            'messages': messages_this_week,
        }

# ---- Admin Panels -----


class UserAdmin(ModelAdmin):
    columns = ('username', 'email', 'admin')

    # Make sure the user's password is hashed, after it's been changed in
    # the admin interface. If we don't do this, the password will be saved
    # in clear text inside the database and login will be impossible.
    def save_model(self, instance, form, adding=False):
        orig_password = instance.password

        user = super(UserAdmin, self).save_model(instance, form, adding)

        if orig_password != form.password.data:
            user.set_password(form.password.data)
            user.save()

        return user


auth.register_admin(admin)
admin.register(User, UserAdmin)
admin.register_panel('User Stats', UserStatsPanel)
