from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField, SelectField
from wtforms.validators import DataRequired, Length, Email, NumberRange, Regexp

# FORM FOR ADDING NEW CONTENT
class ContentForm(FlaskForm):
    """Each Field defines a type of control on the new/edit content form"""

    # possible choices for content_type
    SELECT_CHOICES = [
        ('video', 'Video'),
        ('audio', 'Audio'),
        ('course', 'Course package'),
        ('article', 'Article/Blog'),
        ('ppt', 'Presentation'),
        ('img', 'Graphic'),
        ('code', 'Code snippet')
    ]

    content_name = StringField('Content Name',
                               validators=[
                                   DataRequired(), Length(min=5, max=30)
                               ])

    content_type = SelectField('Content Type',
                               choices=SELECT_CHOICES,
                               validators=[DataRequired()])

    owner_email = StringField('Owner Email',
                              validators=[
                                  DataRequired(), Email()
                              ])

    valid_months = IntegerField('Months Until Next Update',
                                default=1,
                                validators=[NumberRange(min=1, max=60)])

    submit = SubmitField('Save Content')


# FORM FOR CREATING NEW OWNERS
class OwnerForm(FlaskForm):
    """Each Field defines a type of control on the new owner Form"""

    owner_name = StringField('Owner Name',
                             validators=[
                                 DataRequired(),
                                 Length(min=2, max=20),
                                 Regexp(regex=r'^[A-Za-z\s]+$',
                                        message='Only enter letters and spaces')
                             ])

    owner_email = StringField('Owner Email',
                              validators=[
                                  DataRequired(), Email(), Length(max=50)
                              ])

    submit = SubmitField('Save Owner')
