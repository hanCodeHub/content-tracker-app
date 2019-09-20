from flask import Flask, render_template, url_for
from forms import ContentForm

from datetime import date, timedelta

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

@app.route("/content_form")
def content():
    form = ContentForm()
    return render_template('content_form.html',
                           title='Content Form',
                           form=form)

# only true if run from app.py
if __name__ == '__main__':
    app.run(port=5000, debug=True)

