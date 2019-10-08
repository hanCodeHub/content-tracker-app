from flask import render_template, redirect, url_for, request

from main import app
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

# Routes for content page
@app.route("/content", methods=['GET', 'POST'])
def content():
    return content_routes.content_index()

# Routes for owners page
@app.route("/owners", methods=['GET', 'POST'])
def owner():
    return owner_routes.owner_index()

@app.route("/owners/delete", methods=['DELETE'])
def owner_delete():
    owner_id = request.get_json()['owner_id']
    return owner_routes.owner_delete(owner_id)
