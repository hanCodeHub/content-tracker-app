from flask import render_template, redirect, flash, url_for, jsonify
from datetime import date, timedelta

from main.models.ContentModel import Content
from main.models.OwnerModel import Owner
from main.forms import ContentForm

def content_index():
    """Processing for the endpoint /content which handles the content form"""
    form = ContentForm()

    # POST - Following block executes to handle submission of ContentForm
    if form.validate_on_submit():
        choice = form.content_type.data  # content type choice by user
        choices = dict(ContentForm.SELECT_CHOICES)  # all possible choices

        # user input from the content form is stored in the following:
        owner_email = form.owner_email.data
        content_name = form.content_name.data.lower()
        content_type = choices.get(choice)
        valid_months = form.valid_months.data

        # validation - if owner does not exist, reload page with error msg
        owner_obj = Owner.find_by_email(owner_email)
        if not owner_obj:
            flash(f'Owner with the email {owner_email} does not exist!',
                  'danger')
            return redirect(url_for('content'))

        # validation - if content already exists, reload page with error msg
        if Content.find_by_name(content_name):
            flash(f'Content with the name {content_name} already exists!',
                  'danger')
            return redirect(url_for('content'))

        # new content is saved and page is reloaded with success msg
        new_content = Content(content_name=content_name,
                              content_type=content_type,
                              updated_at=date.today(),
                              valid_months=valid_months,
                              owner_id=owner_obj.id)
        new_content.save_content()

        flash(f'{owner_obj.owner_name} has a new {content_type.lower()}!',
              'success')
        return redirect(url_for('content'))

    # GET all existing contents and render it in the view
    contents = Content.get_all_content()

    # content_id:[owner_name, days_left] for each content stored in owner_data
    content_data = {}
    if contents:
        for content in contents:
            # for each content the owner is found and stored in content_data
            content_owner = Owner.find_by_id(content.owner_id).owner_name
            # for each content the days left until expiry is calculated
            days_left = content.calc_days_left()

            content_data[content.id] = [content_owner, days_left]

    # view is rendered with all contents and owner data
    return render_template('content.html',
                           title='Content Form',
                           form=form,
                           contents=contents,
                           content_data=content_data)

def handle_content_edit(content_id):
    """Processing for the endpoint /content/edit/<content_id> to edit content"""
    form = ContentForm()
    content = Content.find_by_id(content_id)

    # POST - for handling the edit content form
    if form.validate_on_submit():
        choice = form.content_type.data  # content type choice by user
        choices = dict(ContentForm.SELECT_CHOICES)  # all possible choices

        # validation - if owner does not exist, reload edit page with error msg
        owner_email = form.owner_email.data
        owner_obj = Owner.find_by_email(owner_email)
        if not owner_obj:
            flash(f'Owner with the email {owner_email} does not exist!',
                  'danger')
            return redirect(url_for('content_edit'))

        # content is updated with form values and saved to the database
        content.content_name = form.content_name.data.lower()
        content.content_type = choices.get(choice)
        content.valid_months = form.valid_months.data
        content.updated_at = date.today()  # today's date becomes last updated
        content.owner_id = owner_obj.id

        content.save_content()

        # user is redirected to the main content page with success msg
        flash(f'{content.content_name} has been updated!', 'success')
        return redirect(url_for('content'))

    # GET - display the form
    # if content does not exist, flash error message
    if not content:
        flash('Content no longer exists!', 'danger')
        return redirect(url_for('content'))

    # form is pre-populated with existing content data
    form.content_name.data = content.content_name
    form.owner_email.data = Owner.find_by_id(content.owner_id).owner_email
    form.valid_months.data = content.valid_months
    form.submit.data = "Update Content"

    # content type stored in this content is looked up against all types
    # each choice is a tuple pair - (stored choice, displayed choice)
    for form_type in ContentForm.SELECT_CHOICES:
        # choice becomes default value on form if it matches the stored value
        if form_type[1] == content.content_type:
            form.content_type.data = form_type[0]

    return render_template('content_edit.html',
                           content_name=content.content_name.title(),
                           form=form)


def handle_content_delete(content_id):
    """Processing for the endpoint /content/delete to delete a content"""

    content = Content.find_by_id(content_id)
    # flash error message if content does not exist
    if not content:
        flash(f'Content does not exist!', 'danger')
        return 'not deleted', 404

    # content is deleted and user is redirected to content page
    content.delete_content()
    flash(f'{content.content_name} has been deleted!', 'success')
    return 'deleted', 202
