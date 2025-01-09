from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from data_models import db, Author, Book


app = Flask(__name__)

# Configuration of the db. connection
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////Users/martinawill/Desktop/🆑😎🆑😎🆑/python/python_visual_code_studio/Book Alchemy/data/library.sqlite'
db.init_app(app)


# Create the tables
with app.app_context():
    db.create_all()
