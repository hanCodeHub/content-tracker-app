from flask import render_template, flash, redirect, url_for

from main import app
from main.models.ContentModel import Content
from main.models.OwnerModel import Owner
from main.forms import ContentForm, OwnerForm

# APP ENDPOINTS
@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html')

@app.route("/inventory")
def inventory():
    return render_template('inventory.html', title='Content Lifecycle')

@app.route("/content", methods=['GET', 'POST'])
def content():
    # user is redirected to Inventory page after submitting ContentForm
    form = ContentForm()

    if form.validate_on_submit():
        # build dictionary from all choices. then get value from choice data
        choice = form.content_type.data
        choices = dict(ContentForm.SELECT_CHOICES)

        flash(f'Your {(choices.get(choice)).lower()} has been added!')
        return redirect(url_for('inventory'))

    return render_template('content_form.html', title='Content Form', form=form)

@app.route("/owner", methods=['GET', 'POST'])
def owner():
    # Owner page is reset after user submits OwnerForm
    form = OwnerForm()

    if form.validate_on_submit():
        name = form.owner_name.data
        email = form.owner_email.data

        form.owner_email.data = ''
        form.owner_name.data = ''

        flash(f'User {name} has been added!')

    return render_template('owner_form.html', title='Owner Form', form=form)
