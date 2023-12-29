import app.state as GlobalState
import database.models as Models
from datetime import datetime
from utils.serialize import serialize_date, serialize_time, deserialize_time


def get_data(date: datetime):
    showtimes = [showtime for showtime in GlobalState.db.showtimes.SelectAll() if serialize_date(date) == serialize_date(showtime.date)]
    data = [map_showtime(showtime) for showtime in showtimes ]
    print(data)
    data.sort(key=lambda x: deserialize_time(x["starting_time"]))
    return data

def map_showtime(showtime: Models.Showtime):
    projection: Models.Projection = showtime.projection.get(GlobalState.db)
    film: Models.Film = projection.film.get(GlobalState.db)
    hall: Models.Hall = projection.hall.get(GlobalState.db)

    return {
        "id": showtime.id,
        "date": serialize_date(showtime.date),
        "film": film.name,
        "hall": hall.id,
        "starting_time": serialize_time(projection.starting_time),
        "ending_time": serialize_time(projection.ending_time)
    }