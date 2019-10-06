from flask import render_template

def inventory_index():
    return render_template('inventory.html', title='Content Lifecycle')
