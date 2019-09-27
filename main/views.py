from flask import render_template, flash, redirect, url_for
from datetime import date

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

@app.route("/owners", methods=['GET', 'POST'])
def owner():
    # Owner page is reset after user submits OwnerForm
    form = OwnerForm()

    # Following if block executes when the form is submitted and validated
    if form.validate_on_submit():
        # obtain the data from the form and clear the form fields
        name = form.owner_name.data
        email = form.owner_email.data
        form.owner_email.data = ''
        form.owner_name.data = ''

        # validate whether owner already exists
        if Owner.find_by_email(email):
            flash(f'User with email {email} already exists!')

        # create and save the new owner with form data
        new_owner = Owner(owner_name=name,
                          owner_email=email,
                          joined_at=date.today().split(' ')[0])
        new_owner.save_owner()
        flash(f'User {name} has been created!')

    # Get all existing owners from the database and render the view
    owners = Owner.get_all_owners()
    return render_template('owner_form.html',
                           title='Owner Form',
                           form=form,
                           owners=owners)
