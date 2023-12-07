import app.state as GlobalState
import database.models as Models

criteria = {
    "name": "",
    "genre": [],
    "duration": {
        "min": None,
        "max": None
    },
    "director": [],
    "role": [],
    "country": [],
    "year": []
}

def get_film_list():
    all_films = GlobalState.db.films.SelectAll()
    return [film for film in all_films if check_all_criteria(film)]

def check_all_criteria(film: Models.Film):
    return (
        check_name(film) and
        check_genres(film) and
        check_duration(film) and
        check_director(film) and
        check_roles(film) and 
        check_country(film) and
        check_year(film)
    )

def check_name(film: Models.Film):
    if criteria["name"] == "":
        return True
    return criteria["name"].lower() in film.name.lower()

def check_genres(film: Models.Film):
    if len(criteria["genre"]) == 0:
        return True
    for genre in criteria["genre"]:
        if genre in film.genres:
            return True
    return False

def check_duration(film: Models.Film):
    if criteria["duration"]["min"] is None and criteria["duration"]["max"] is None:
        return True
    is_above_min = criteria["duration"]["min"] is None or film.duration >= criteria["duration"]["min"]
    is_below_max = criteria["duration"]["max"] is None or film.duration <= criteria["duration"]["max"]
    return is_above_min and is_below_max

def check_director(film: Models.Film):
    if len(criteria["director"]) == 0:
        return True
    for director in criteria["director"]:
        if director == film.director:
            return True
    return False

def check_roles(film: Models.Film):
    if len(criteria["role"]) == 0:
        return True
    for role in criteria["role"]:
        if role in film.main_roles:
            return True
    return False

def check_country(film: Models.Film):
    if len(criteria["country"]) == 0:
        return True
    for country in criteria["country"]:
        if country == film.country:
            return True
    return False

def check_year(film: Models.Film):
    if len(criteria["year"]) == 0:
        return True
    for year in criteria["year"]:
        if year == film.year:
            return True
    return False