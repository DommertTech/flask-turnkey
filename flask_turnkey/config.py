# Flask-TurnKey Version 0.0.1
# Config.py

class Configuration(object):
    DATABASE = {
        'name': 'flask_turnkey.db',
        'engine': 'peewee.SqliteDatabase',
        'check_same_thread': False,
    }
    HOST = '0.0.0.0'
    PORT = 5002
    DEBUG = True
    SECRET_KEY = 'shhhhh!!!'
    TEMPLATE_DEFAULTS = {
'nav': 'site/blocks/rum_nav.html',
'footer': 'site/blocks/rum_footer.html'
}
