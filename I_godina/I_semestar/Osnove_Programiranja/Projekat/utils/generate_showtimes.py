import app.state as State
import database.models as Models
from datetime import datetime, timedelta
from utils.serialize import serialize_date

def generate_all(start: datetime, length: int):
    projections: list[Models.Projection] = State.db.projections.SelectAll()
    for projection in projections:
        generate_single(projection, start, length)

def generate_single(projection: Models.Projection, start: datetime, number_of_days: int):
    days = [day_index(d) for d in projection.days]
    for delta in range(number_of_days):
        date = start + timedelta(days=delta)
        # projekcija se ne prikazuje tog dana
        if date.weekday() not in days:
            continue
        showtimes = [showtime for showtime in State.db.showtimes.SelectAll() if showtime.projection_id == projection.id]
        # termin za trenutni datum postoji
        if len([showtime for showtime in showtimes if serialize_date(showtime.date) == serialize_date(date)]) != 0:
            continue
        print(projection.id, serialize_date(date))
        # generisi termin
        ids = [showtime.id for showtime in showtimes]
        letters = [0, 0]
        id = projection.id + chr(ord("A") + letters[0]) + chr(ord("A") + letters[1])
        while id in ids:
            letters[1] += 1
            letters[0] += letters[1]//26
            letters[0] %= 26
            letters[1] %= 26
            if letters[0] == 0 and letters[1] == 0:
                print(f"All ids are taken for projection id: {projection.id} on {serialize_date(date)}")
                return
            id = projection.id + chr(ord("A") + letters[0]) + chr(ord("A") + letters[1])
        new_showtime = Models.Showtime(id, projection.id, date)
        State.db.showtimes.Insert(new_showtime)
        



def day_index(day: str):
    return Models.Days.all_days.index(day)