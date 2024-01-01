import app.state as GlobalState
import database.models as Models
from datetime import datetime
from utils.serialize import serialize_date, serialize_time, deserialize_time

criteria = {
    "film": [],
    "hall": [],
    "time": {
        "min": None,
        "max": None
    },
}

def reset():
    criteria["film"] = []
    criteria["hall"] = []
    criteria["time"] = {
        "min": None,
        "max": None
    }

    
def get_data(date: datetime):
    showtimes = [showtime for showtime in GlobalState.db.showtimes.SelectAll() if serialize_date(date) == serialize_date(showtime.date)]
    data = [map_showtime(showtime) for showtime in showtimes ]
    data.sort(key=lambda x: deserialize_time(x["starting_time"]))
    return [item for item in data if check_all_criteria(item)]

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

def check_all_criteria(item):
    return (
        _check(item, "film") and
        _check(item, "hall") and
        check_time(item)
    )

def _check(item, field):
    if len(criteria[field]) == 0:
        return True
    if item[field] in criteria[field]:
        return True
    return False

def check_time(item): 
    if criteria["time"]["min"] is None and criteria["time"]["max"] is None:
        return True
    item_starting_time = deserialize_time(item["starting_time"]).time()
    item_ending_time = deserialize_time(item["ending_time"]).time()
    is_above_min = criteria["time"]["min"] is None or item_starting_time >= criteria["time"]["min"]
    is_below_max = criteria["time"]["max"] is None or item_ending_time <= criteria["time"]["max"]
    return is_above_min and is_below_max