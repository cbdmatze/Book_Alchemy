from flask_wtf import FlaskForm
from wtforms import StringField, DateField, SelectField, SubmitField, IntegerField
from wtforms.validators import DataRequired, Length, NumberRange

class AddAuthorForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired(), Length(max=100)])
    birth_date = DateField('Birth Date', format='%Y-%m-%d', validators=[DataRequired()])
    submit = SubmitField('Add Author')

class AddBookForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired(), Length(max=200)])
    isbn = StringField('ISBN', validators=[DataRequired(), Length(min=10, max=13)])
    author = SelectField('Author', coerce=int)
    publication_year = IntegerField('Publication Year', validators=[DataRequired()])
    submit = SubmitField('Add Book')

class RateBookForm(FlaskForm):
    rating = IntegerField('Rating (1-10)', validators=[DataRequired(), NumberRange(min=1, max=10)])
    submit = SubmitField('Submit Rating')
