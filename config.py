import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY', 'dev_key')
    SQLALCHEMY_DATABASE_URI = 'sqlite:////Users/martinawill/Desktop/🆑😎🆑😎🆑/python/python_visual_code_studio/Book Alchemy/data/library.sqlite'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
