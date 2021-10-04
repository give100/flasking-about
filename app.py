from flask import Flask
from flask import render_template
from flask_sqlalchemy import SQLAlchemy
from models.user import User

app = Flask(__name__)
app.config.from_object("config.Config")
db = SQLAlchemy(app)

@app.route('/')
def home():
    return render_template('home.html', users=User.query.all())
