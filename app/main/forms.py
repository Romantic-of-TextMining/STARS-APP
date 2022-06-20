from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField
from wtforms.validators import DataRequired


class NameForm(FlaskForm):
    name = StringField('What is your name?', validators=[DataRequired()])
    submit = SubmitField('Submit')

class FieldForm(FlaskForm):
    # need to chnge to api
    STARS_FIELD = [
        ("AC_8_Campus_As_A_Living_Laboratory", "AC_8_Campus_As_A_Living_Laboratory"),
        ("AC_9_Research_and_Scholarship", "AC_9_Research_and_Scholarship"),
        ("EN_14_Participation_in_Public_Policy", "EN_14_Participation_in_Public_Policy"),
        ("OP_10_Biodiversity", "OP_10_Biodiversity"),
        ("PA_1_Sustainability_Coordination", "PA_1_Sustainability_Coordination")
    ]
    field = SelectField('STARS Field', choices=STARS_FIELD)
    submit = SubmitField('Submit')  

class SearchForm(FieldForm):
    query = StringField('Keyword')
