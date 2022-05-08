from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField
from wtforms.validators import DataRequired


class NameForm(FlaskForm):
    name = StringField('What is your name?', validators=[DataRequired()])
    submit = SubmitField('Submit')

class StarsForm(FlaskForm):
    STARS_FIELD = [
        ("Public Engagement", "Public Engagement"),
        ("Campus as a Living Lab", "Campus as a Living Lab"),
        ("What", "What"),
        ("I don't care", "I don't care")
    ]
    field = SelectField('STARS Field', choices=STARS_FIELD)
    submit = SubmitField('Submit')  

class SearchForm(FlaskForm):
    keyword = StringField('Keyword')
