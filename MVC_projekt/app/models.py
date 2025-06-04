events = []

def get_all_events():
    return events

def add_event(name, date, seats):
    event = {
        'id': len(events) + 1,
        'name': name,
        'date': date,
        'seats': seats
    }
    events.append(event)

def get_event(event_id):
    return next((e for e in events if e['id'] == event_id), None)

def update_event(event_id, name, date, seats):
    event = get_event(event_id)
    if event:
        event['name'] = name
        event['date'] = date
        event['seats'] = seats

def delete_event(event_id):
    global events
    events = [e for e in events if e['id'] != event_id]
