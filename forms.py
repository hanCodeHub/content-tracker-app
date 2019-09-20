from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField
from wtforms.validators import DataRequired, Length, Email, NumberRange


class ContentForm(FlaskForm):
    # passed arguments are the label for the form control and its validators
    content_name = StringField('Content Name',
                               validators=[
                                   DataRequired(), Length(min=5, max=30)
                               ])

    owner_name = StringField('Owner Name',
                             validators=[
                                 DataRequired(), Length(min=2, max=20)
                             ])

    owner_email = StringField('Owner Email',
                              validators=[
                                  DataRequired(), Email()
                              ])

    valid_days = IntegerField('Days Until Expiration',
                              validators=[
                                  DataRequired(), NumberRange(min=1, max=365)
                              ])

    submit = SubmitField('Save Content')
