from . import models

def handle_add_event(form):
    models.add_event(form['name'], form['date'], int(form['seats']))

def handle_update_event(event_id, form):
    models.update_event(event_id, form['name'], form['date'], int(form['seats']))

def handle_delete_event(event_id):
    models.delete_event(event_id)
