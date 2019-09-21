from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField, SelectField
from wtforms.validators import DataRequired, Length, Email, NumberRange, Regexp


class ContentForm(FlaskForm):
    SELECT_CHOICES = [('course', 'Course package'),
                      ('video', 'Video'),
                      ('audio', 'Audio'),
                      ('article', 'Article/Blog'),
                      ('ppt', 'Presentation'),
                      ('img', 'Graphic'),
                      ('code', 'Code snippet')]

    # passed arguments are the label for the form control and its validators
    content_name = StringField('Content Name',
                               validators=[
                                   DataRequired(), Length(min=5, max=30)
                               ])

    content_type = SelectField('Content Type',
                               choices=SELECT_CHOICES,
                               validators=[DataRequired()]
                               )

    owner_name = StringField('Owner Name',
                             validators=[
                                 DataRequired(), Length(min=2, max=20),
                                 Regexp(regex='[A-Za-z]+',
                                        message='Only enter letters and spaces')
                             ])

    owner_email = StringField('Owner Email',
                              validators=[
                                  DataRequired(), Email()
                              ])

    valid_months = IntegerField('Months Until Expiration',
                                validators=[
                                    DataRequired(), NumberRange(min=1, max=60)
                                ])

    submit = SubmitField('Save Content')
