# Flask-TurnKey Version 0.0.1
# Author: Dommert (Dommert@Gmail.com)
#


from app import app, db
from auth import *
from admin import admin
#from api import api
from models import *
from views import *
from rum import rum

admin.setup()
#api.setup()

if __name__ == '__main__':
    auth.User.create_table(fail_silently=True)
    app.run(host=app.config['HOST'], port=app.config['PORT'], debug=app.config['DEBUG'])
