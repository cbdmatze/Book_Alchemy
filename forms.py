from flask_wtf import FlaskForm
from wtforms import StringField, DateField, SelectField, SubmitField
from wtforms.validators import DataRequired, Length


class AddAuthorForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired(), Length(max=100)])
    birth_date = DateField('Birth Date', format='%Y-%m-%d', validators=[DataRequired()])
    submit = SubmitField('Add Author')


class AddBookForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired(), Length(max=200)])
    isbn = StringField('ISBN', validators=[DataRequired(), Length(min=10, max=13)])
    author = SelectField('Author', coerce=int) # Dropdown list for authors
    submit = SubmitField('Add Book')
