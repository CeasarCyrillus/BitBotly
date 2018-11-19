from flask import Flask
import jinja2
from config import Config
from flask_assets import Environment, Bundle
from flask_compress import Compress
import admin
import os
from flask_login import LoginManager, AnonymousUserMixin
import sendgrid
#Init app

template_dir = os.path.dirname(os.path.realpath(__file__))
app = Flask(__name__, template_folder=template_dir)
sg = sendgrid.SendGridAPIClient(apikey=os.environ["SENDGRID_API_KEY"])

#Setup loginmanager

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'
#Init assets
assets = Environment(app)


#Bundle js and css
js = Bundle('js/jquery.min.js', 'js/jquerySlim.js', 'js/vex.combined.js', 'js/script.js', 'js/api.js', filters='jsmin', output='gen/packed.js')
css = Bundle('css/style.css', 'css/vex.css', 'css/vex-theme-os.css', filters='cssmin', output='gen/packed.css')

assets.register('css', css)
assets.register('js', js)

css_path = "../templates/components/css/"
js_path = "../templates/components/js/"

component_bundle_js = Bundle(
    js_path+"mainMenu.js",
    js_path+"header.js",
    js_path+"menuBase.js",
    js_path+"register.js",
    js_path+"login.js",
	js_path+"privacy.js",
    filters='jsmin', output='gen/components_packed.js')

component_bundle_css = Bundle(
    css_path+"mainMenu.css",
    css_path+"header.css",
    css_path+"menuBase.css",
    css_path+"register.css",
    css_path+"login.css",
	css_path+"privacy.css",
    filters='cssmin', output='gen/components_packed.css')



assets.register("component_css", component_bundle_css)
assets.register("component_js", component_bundle_js)

#Compress app
Compress(app)



app.secret_key = os.environ["FLASK_SECRET_KEY"]

#Database stuffs
app.config.from_object(Config)



_js_escapes = {
	'\\': '\\u005C',
	'\'': '\\u0027',
	'"': '\\u0022',
	'>': '\\u003E',
	'<': '\\u003C',
	'&': '\\u0026',
	'=': '\\u003D',
	'-': '\\u002D',
	';': '\\u003B',
	u'\u2028': '\\u2028',
	u'\u2029': '\\u2029'
}
# Escape every ASCII character with a value less than 32.
_js_escapes.update(('%c' % z, '\\u%04X' % z) for z in range(32))
def jinja2_escapejs_filter(value):
	retval = []
	for letter in value:
		if letter in _js_escapes:
			retval.append(_js_escapes[letter])
		else:
			retval.append(letter)

	return jinja2.Markup("".join(retval))
app.jinja_env.filters['escapejs'] = jinja2_escapejs_filter

from models import *
from utils import send_mail_async