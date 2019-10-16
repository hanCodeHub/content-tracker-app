from flask import render_template, redirect, url_for, request

from main import app
from main.routes import inventory_routes, content_routes, owner_routes

# APP ENDPOINTS

# HOMEPAGE
# Route for base URL - redirect to /home
@app.route('/')
def index():
    return redirect(url_for("home"))
# Route for homepage - notifications and content data displayed
@app.route("/home")
def home():
    return render_template("home.html")

# TEST PAGE
@app.route("/inventory")
def inventory():
    return inventory_routes.inventory_index()

# CONTENT PAGE
# Route for /content page - new content form and table displayed
@app.route("/content", methods=["GET", "POST"])
def content():
    return content_routes.content_index()

# Route for /content/edit page - edit form modal displayed
@app.route("/content/edit", methods=["GET", "POST"])
def content_edit():
    content_id = request.args.get('content_id')
    return content_routes.handle_content_edit(content_id)

# Route for delete request - accepts JSON with content_id
@app.route("/content/delete", methods=["DELETE"])
def content_delete():
    content_id = request.get_json()["content_id"]
    return content_routes.handle_content_delete(content_id)

# OWNERS PAGE
# Route for /owners page - new owner form and table displayed
@app.route("/owners", methods=["GET", "POST"])
def owner():
    return owner_routes.owner_index()

# Route for delete request - accepts JSON with owner_id
@app.route("/owners/delete", methods=["DELETE"])
def owner_delete():
    # owner_id is in json payload, supplied by fetch from the browser (owner.js)
    owner_id = request.get_json()["owner_id"]
    return owner_routes.handle_owner_delete(owner_id)
