from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField
from wtforms.validators import DataRequired


class NameForm(FlaskForm):
    name = StringField('What is your name?', validators=[DataRequired()])
    submit = SubmitField('Submit')

class FieldForm(FlaskForm):
    # need to chnge to api
    STARS_FIELD = [
        ("ac_8_campus_as_a_living_laboratory", "ac_8_campus_as_a_living_laboratory"),
        ("en_14_participation_in_public_policy", "en_14_participation_in_public_policy"),
        ("What", "What"),
        ("I don't care", "I don't care")
    ]
    field = SelectField('STARS Field', choices=STARS_FIELD)
    submit = SubmitField('Submit')  

class SearchForm(FieldForm):
    query = StringField('Keyword')
