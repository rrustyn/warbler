from flask import Flask, g, session, render_template
import os

from warbler.config import DATABASE_URL
from warbler.database import connect_db

from warbler.root.views import root_blueprint
from warbler.messages.views import messages_blueprint
from warbler.users.views import users_blueprint

from warbler.users.models import User
from warbler.root.forms import CSRFProtection

# create app and add configuration
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = DATABASE_URL
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True
app.config['SECRET_KEY'] = os.environ['SECRET_KEY']

connect_db(app)

CURR_USER_KEY = "curr_user"

@app.before_request
def add_user_to_g():
    """If we're logged in, add curr user to Flask global."""

    if CURR_USER_KEY in session:
        g.user = User.query.get(session[CURR_USER_KEY])

    else:
        g.user = None


@app.before_request
def add_csrf_only_form():
    """Add a CSRF-only form so that every route can use it."""

    g.csrf_form = CSRFProtection()


# register blueprints
app.register_blueprint(root_blueprint)
app.register_blueprint(users_blueprint, url_prefix='/users')
app.register_blueprint(messages_blueprint, url_prefix='/messages')


@app.errorhandler(404)
def page_not_found(e):
    """404 NOT FOUND page."""

    return render_template('404.html'), 404


@app.after_request
def add_header(response):
    """Add non-caching headers on every request."""

    # https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Cache-Control
    response.cache_control.no_store = True
    return response


