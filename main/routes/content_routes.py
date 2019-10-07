from flask import render_template, redirect, flash, url_for
from datetime import date

from main.models.ContentModel import Content
from main.models.OwnerModel import Owner
from main.forms import ContentForm

def content_index():
    """Returns the endpoint for /content which handles the content form"""

    form = ContentForm()
    # Upon successful submission of form:
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

    # if there are contents, a dict holds owner id:name pairs for each content
    owner_names_by_id = {}
    if contents:
        for content in contents:
            content_owner_name = Owner.find_by_id(content.owner_id).owner_name
            owner_names_by_id[content.id] = content_owner_name

    return render_template('content_form.html',
                           title='Content Form',
                           form=form,
                           contents=contents,
                           owner_names=owner_names_by_id)
