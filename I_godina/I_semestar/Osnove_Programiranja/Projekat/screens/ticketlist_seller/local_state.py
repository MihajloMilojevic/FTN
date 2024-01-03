import app.state as GlobalState
import database.models as Models
from utils.serialize import serialize_date, serialize_time, deserialize_date
from datetime import datetime


criteria = {
    "projections": [],
    "films": [],
    "status": [],
    "name": "",
    "date": {
        "min": None,
        "max": None
    },
    "time": {
        "min": None,
        "max": None
    },
}

def get_data():
    tickets = GlobalState.db.tickets.Select(check)
    return [map_ticket(ticket) for ticket in tickets]

def map_ticket(ticket: Models.Ticket):
    showtime: Models.Showtime = ticket.showtime.get(GlobalState.db)
    showtime
    projection: Models.Projection = showtime.projection.get(GlobalState.db)
    hall: Models.Hall = projection.hall.get(GlobalState.db)
    film: Models.Film = projection.film.get(GlobalState.db)
    name = ticket.full_name
    if name is None:
        user: Models.User = GlobalState.db.users.SelectById(ticket.username)
        name = f"{user.name} {user.surname}"
    return {
        "id": ticket.id,
        "film": film.name,
        "hall": hall.id,
        "date": serialize_date(showtime.date),
        "starting_time": serialize_time(projection.starting_time),
        "ending_time": serialize_time(projection.ending_time),
        "seat_tag": ticket.seat_tag,
        "status": "Rezervisano" if ticket.reserved else "Prodato",
        "name": name
    }

def check(ticket: Models.Ticket) -> bool:
    return (
        check_projection(ticket) and
        check_film(ticket) and
        check_status(ticket) and
        check_name(ticket) and
        check_date(ticket) and
        check_time(ticket)
    )

def check_projection(ticket: Models.Ticket) -> bool:
    if len(criteria["projections"]) == 0:
        return True
    showtime: Models.Showtime = ticket.showtime.get(GlobalState.db)
    return showtime.projection_id in criteria["projections"]

def check_film(ticket: Models.Ticket) -> bool:
    if len(criteria["films"]) == 0:
        return True
    showtime: Models.Showtime = ticket.showtime.get(GlobalState.db)
    projection: Models.Projection = showtime.projection.get(GlobalState.db)
    film: Models.Film = projection.film.get(GlobalState.db)
    return film.name in criteria["films"]

def check_status(ticket: Models.Ticket) -> bool:
    if len(criteria["status"]) == 0:
        return True
    return ("Rezervisano" if ticket.reserved else "Prodato") in criteria["status"]

def check_name(ticket: Models.Ticket) -> bool:
    if criteria["name"] == "":
        return True
    name = ticket.full_name
    if name is None:
        user: Models.User = GlobalState.db.users.SelectById(ticket.username)
        name = f"{user.name} {user.surname}"
    return criteria["name"].lower() in name.lower() 

def check_date(ticket: Models.Ticket):
    if criteria["date"]["min"] is None and criteria["date"]["max"] is None:
        return True
    showtime: Models.Showtime = ticket.showtime.get(GlobalState.db)
    is_above_min = criteria["date"]["min"] is None or showtime.date.date() >= criteria["date"]["min"]
    is_below_max = criteria["date"]["max"] is None or showtime.date.date() <= criteria["date"]["max"]
    return is_above_min and is_below_max

def check_time(ticket: Models.Ticket):
    if criteria["time"]["min"] is None and criteria["time"]["max"] is None:
        return True
    showtime: Models.Showtime = ticket.showtime.get(GlobalState.db)
    projection: Models.Projection = showtime.projection.get(GlobalState.db)
    is_above_min = criteria["time"]["min"] is None or projection.starting_time.time() >= criteria["time"]["min"]
    is_below_max = criteria["time"]["max"] is None or projection.ending_time.time() <= criteria["time"]["max"]
    return is_above_min and is_below_max