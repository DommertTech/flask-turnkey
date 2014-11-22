from app import app
from flask_rum.main import rum
#import flask_rum.rum_config as rum_config
#app.config.from_object(rum_config)
app.config.THEME_FOLDER='rum/banana/'
app.config.PROJECT_TITLE = '[Flask-Rum]'
app.config.TEMPLATE_DEFAULTS = {
'nav': 'site/blocks/rum_nav.html',
'footer': 'site/blocks/rum_footer.html'
}
app.register_blueprint(rum)
