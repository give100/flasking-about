from flask import Flask
from flask import render_template
from flask_sqlalchemy import SQLAlchemy


def create_app(config_object="settings"):
    """Create application factory, as explained here: http://flask.pocoo.org/docs/patterns/appfactories/.

    :param config_object: The configuration object to use.
    """
    app = Flask(__name__)
    app.config.from_object(config_object)
    return app

app = create_app()
db = SQLAlchemy(app)

from models import User

@app.route('/')
def home():
    return render_template('home.html', users=User.query.all())

