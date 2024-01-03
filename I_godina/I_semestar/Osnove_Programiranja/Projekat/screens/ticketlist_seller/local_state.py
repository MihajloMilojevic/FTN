import app.state as GlobalState
import database.models as Models
from utils.serialize import serialize_date, serialize_time, deserialize_date
from datetime import datetime

def get_data():
    tickets = GlobalState.db.tickets.SelectAll()
    return [map_ticket(ticket) for ticket in tickets]

def map_ticket(ticket: Models.Ticket):
    showtime: Models.Showtime = ticket.showtime.get(GlobalState.db)
    showtime
    projection: Models.Projection = showtime.projection.get(GlobalState.db)
    hall: Models.Hall = projection.hall.get(GlobalState.db)
    film: Models.Film = projection.film.get(GlobalState.db)
    return {
        "id": ticket.id,
        "film": film.name,
        "hall": hall.id,
        "date": serialize_date(showtime.date),
        "starting_time": serialize_time(projection.starting_time),
        "ending_time": serialize_time(projection.ending_time),
        "seat_tag": ticket.seat_tag,
        "status": "Rezervisano" if ticket.reserved else "Prodato"
    }