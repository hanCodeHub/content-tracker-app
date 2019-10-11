from flask import render_template, redirect, flash, url_for, jsonify
from datetime import date

from main.models.ContentModel import Content
from main.models.OwnerModel import Owner
from main.forms import ContentForm

def content_index():
    """Processing for the endpoint /content which handles the content form"""

    # Following block executes to handle submission of ContentForm
    form = ContentForm()
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
        flash(f'{owner_obj.owner_name} has added a new {content_type.lower()}!',
              'success')
        return redirect(url_for('content'))

    # GET all existing contents and render it in the view
    contents = Content.get_all_content()

    # owner_id:owner_name pairs for each content is stored in owner_data
    owner_data = {}
    if contents:
        for content in contents:
            # for each content the owner is found
            content_owner = Owner.find_by_id(content.owner_id)
            if content_owner:
                owner_data[content.id] = content_owner.owner_name

    # view is rendered with all contents and owner data
    return render_template('content.html',
                           title='Content Form',
                           form=form,
                           contents=contents,
                           owner_data=owner_data)

def handle_content_edit(content_id):
    """Processing for the endpoint /content/edit/<content_id> to edit content"""
    
    # if content does not exist, flash error message
    content = Content.find_by_id(content_id)
    if not content:
        flash('Content no longer exists!', 'danger')
        return redirect(url_for('content'))

    # form is pre-populated with existing content data
    form = ContentForm()
    form.content_name.data = content.content_name
    form.owner_email.data = Owner.find_by_id(content.owner_id).owner_email
    form.valid_months.data = content.valid_months
    form.submit.data = "Update Content"

    # choice stored in this content is looked up against all choices
    for choice in ContentForm.SELECT_CHOICES:  # each choice is a tuple pair
        # choice becomes default value on form if it matches the stored value
        if choice[1] == content.content_type:
            form.content_type.data = choice[0]
    
    return render_template('content_edit.html',
                           content=content,
                           form=form)


def handle_content_delete(content_id):
    """Processing for the endpoint /content/delete to delete a content"""

    content = Content.find_by_id(content_id)
    # flash error message if content does not exist
    if not content:
        flash(f'Content does not exist!', 'danger')
        return jsonify('not deleted')

    # content is deleted and user is redirected to content page
    content.delete_content()
    flash(f'{content.content_name} has been deleted!', 'success')
    return jsonify('deleted')
