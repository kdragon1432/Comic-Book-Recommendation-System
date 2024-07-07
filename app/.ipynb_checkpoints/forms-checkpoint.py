from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

class SearchForm(FlaskForm):
    issue_name = StringField('Issue Name', validators=[DataRequired()])
    submit = SubmitField('Submit')