from flask import render_template, redirect, flash, url_for
from werkzeug.exceptions import HTTPException
from datetime import date

from main.models.OwnerModel import Owner
from main.forms import OwnerForm

def owner_index():
    """Processing of the endpoint /owners which handles the owner form"""

    # Following block executes to handle submission of OwnerForm
    form = OwnerForm()
    if form.validate_on_submit():
        # obtain the data from the form
        name = form.owner_name.data
        email = form.owner_email.data

        # validate whether owner already exists
        if Owner.find_by_email(email):
            flash(f'User with email {email} already exists!', 'danger')
            return redirect(url_for('owner'))

        # create and save the new owner with form data
        new_owner = Owner(owner_name=name.title(),
                          owner_email=email,
                          joined_at=date.today())

        # saving owner errors are handled
        try:
            new_owner.save_owner()
        except HTTPException:
            return "Server cannot save the owner at this time", 500

        flash(f'User {name} has been created!', 'success')
        return redirect(url_for('owner'))

    # GET all existing owners from the database and render the view
    owners = Owner.get_all_owners()
    return render_template('owners.html',
                           title='Owner Form',
                           form=form,
                           owners=owners)


def handle_owner_delete(owner_id):
    """Processing of the endpoint /owner/delete to delete an owner"""

    owner = Owner.find_by_id(owner_id)
    # flash error message if owner does not exist
    if not owner:
        flash(f'Owner does not exist!', 'danger')
        return 'not deleted', 404
    # flash error message if owner still has existing content
    elif owner.contents:
        flash(f'{owner.owner_name} still has existing content!', 'danger')
        return 'not deleted', 400

    # owner is deleted and user is redirected (redirect code in owners.js)
    # deleting owner errors handled
    try:
        owner.delete_owner()
    except HTTPException:
        return "Server cannot delete the owner at this time", 500

    flash(f'{owner.owner_name} has been deleted!', 'success')
    return 'deleted', 202
