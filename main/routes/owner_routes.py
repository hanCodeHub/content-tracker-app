from flask import render_template, redirect, flash, url_for, jsonify
from datetime import date

from main.models.OwnerModel import Owner
from main.forms import OwnerForm

def owner_index():
    """Processing of the endpoint /owners which handles the owner form"""

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
            flash(f'User with email {email} already exists!', 'danger')
            return redirect(url_for('owner'))

        # create and save the new owner with form data
        new_owner = Owner(owner_name=name,
                          owner_email=email,
                          joined_at=date.today()
                          )
        new_owner.save_owner()
        flash(f'User {name} has been created!', 'success')

    # Get all existing owners from the database and render the view
    owners = Owner.get_all_owners()
    return render_template('owner_form.html',
                           title='Owner Form',
                           form=form,
                           owners=owners)

def owner_delete(owner_id):
    """Processing of the endpoint /owner/delete?owner_id to delete an owner"""

    owner = Owner.find_by_id(owner_id)
    # flash error message if owner does not exist
    if not owner:
        flash(f'Owner does not exist!', 'danger')
        return jsonify('not deleted')
    # flash error message if owner still has existing content
    elif owner.contents:
        flash(f'{owner.owner_name} still has existing content!', 'danger')
        return jsonify('not deleted')

    # owner is deleted and user is redirected to owner page
    owner.delete_owner()
    flash(f'{owner.owner_name} has been deleted!', 'success')
    return jsonify('deleted')
