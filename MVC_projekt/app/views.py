from flask import Blueprint, render_template, request, redirect, url_for
from . import models, controllers

views = Blueprint('views', __name__)

@views.route('/')
def index():
    return render_template('index.html', events=models.get_all_events())

@views.route('/add', methods=['GET', 'POST'])
def add_event():
    if request.method == 'POST':
        controllers.handle_add_event(request.form)
        return redirect(url_for('views.index'))
    return render_template('add_event.html')

@views.route('/edit/<int:event_id>', methods=['GET', 'POST'])
def edit_event(event_id):
    event = models.get_event(event_id)
    if request.method == 'POST':
        controllers.handle_update_event(event_id, request.form)
        return redirect(url_for('views.index'))
    return render_template('edit_event.html', event=event)

@views.route('/delete/<int:event_id>')
def delete_event(event_id):
    controllers.handle_delete_event(event_id)
    return redirect(url_for('views.index'))
