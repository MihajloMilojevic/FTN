import app.state as State
import database.models as Models
from datetime import datetime

def cancel_upcoming_tickets():
    return State.db.tickets.Delete(check_ticket)
        
def check_ticket(ticket: Models.Ticket):
    if not ticket.reserved:
        return False
    showtime: Models.Showtime = ticket.showtime.get(State.db)
    if showtime.date.date() != datetime.today().date():
        return False
    projection: Models.Projection = showtime.projection.get(State.db)
    ticket_time = time_to_minutes(projection.starting_time)
    current_time = time_to_minutes(datetime.now())
    diff = ticket_time - current_time
    if 0 <= diff <= 30:
        return True
    return False

def time_to_minutes(t: datetime):
    return t.hour * 60 + t.minute