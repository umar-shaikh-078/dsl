queue = []

def add_event(e):
    queue.append(e)
    print("Event added:", e)

def process_event():
    if queue:
        print("Processing:", queue.pop(0))
    else:
        print("No events to process")

def display_events():
    print("Pending events:", queue)

def cancel_event(e):
    if e in queue:
        queue.remove(e)
        print("Event cancelled:", e)
    else:
        print("Cannot cancel. Event not found:", e)

add_event("Login")
add_event("Payment")
add_event("Logout")
add_event("Upload")
display_events()
process_event()
cancel_event("Logout")
display_events()
cancel_event("Email")