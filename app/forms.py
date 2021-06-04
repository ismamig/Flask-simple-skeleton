from flask_wtf import FlaskForm
from wtforms.validators import DataRequired
'''
Import more elements here (ex : TextField, IntegerField, TextAreaField, SubmitField, RadioField)
'''
from wtforms import StringField


'''
Define your forms here.
'''

class MyForm(FlaskForm):
    name = StringField('name', validators=[DataRequired()])