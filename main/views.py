from flask import render_template, flash, redirect, url_for
from datetime import date

from main import app
from main.models.ContentModel import Content
from main.models.OwnerModel import Owner
from main.forms import ContentForm, OwnerForm

from main.routes import inventory_routes, content_routes, owner_routes

# APP ENDPOINTS

# Routes for homepage
@app.route("/")
def index():
    return redirect(url_for('home'))
@app.route("/home")
def home():
    return render_template('home.html')

@app.route('/inventory')
def inventory():
    return inventory_routes.inventory_index()

@app.route("/content", methods=['GET', 'POST'])
def content():
    return content_routes.content_index()

@app.route("/owners", methods=['GET', 'POST'])
def owner():
    return owner_routes.owner_index()
