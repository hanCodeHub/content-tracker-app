from flask import Flask, render_template, flash, redirect, url_for
from datetime import date, timedelta

from forms import ContentForm


app = Flask(__name__)

app.config['SECRET_KEY'] = '582b482752caf974aa4ab020395f993a'

today = date.today()
time_delta = timedelta(days=120)
expired_at = today + time_delta

contents = [
    {
        'content_name': 'product brochure',
        'content_type': 'PDF',
        'owner_name': 'Han',
        'owner_email': 'han@email.com',
        'created_date': today,
        'expired_date': expired_at
    },
    {
        'content_name': 'product demo',
        'content_type': 'video',
        'owner_name': 'Sean',
        'owner_email': 'sean@email.com',
        'created_date': today,
        'expired_date': expired_at
    }
]


@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html')


@app.route("/inventory")
def inventory():
    return render_template('contents.html',
                           contents=contents,
                           title='Content Lifecycle')


@app.route("/content", methods=['GET', 'POST'])
def content():
    # instantiate the form object and render the form HTML page
    form = ContentForm()

    if form.validate_on_submit():
        choice = form.content_type.data
        choices = dict(ContentForm.SELECT_CHOICES)

        flash(f'Your {(choices.get(choice)).lower()} has been added!')
        return redirect(url_for('inventory'))

    return render_template('content_form.html',
                           title='Content Form',
                           form=form)


# only true if run from app.py
if __name__ == '__main__':
    app.run(port=5000, debug=True)

