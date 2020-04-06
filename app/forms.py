from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, IntegerField
from wtforms import validators
from wtforms.validators import DataRequired, ValidationError, NumberRange


class InputForm(FlaskForm):
    var1 = IntegerField('', validators=[DataRequired(), validators.NumberRange(min=1, max=10)])
    var2 = IntegerField('', validators=[DataRequired(), validators.NumberRange(min=10, max=2000)])
    var3 = IntegerField('', validators=[DataRequired(), validators.NumberRange(min=1, max=7)])
    submit = SubmitField('Розрахувати')


class Sigaretts(FlaskForm):
    var1 = IntegerField('', validators=[validators.NumberRange(min=0, max=100)])
    submit = SubmitField('Розрахувати')


class Water(FlaskForm):
    var1 = IntegerField('', validators=[validators.NumberRange(min=0, max=10)])
    submit = SubmitField('Розрахувати')
