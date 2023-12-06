from database.models.enums import Roles, Genres, Days
from database.models.film import Film
from database.models.ticket import Ticket
from database.models.user import User
from database.models.projection import Projection
from database.models.hall import Hall
from database.models.showtime import Showtime

models_by_name = {
    "Roles": Roles,
    "Genres": Genres,
    "Days": Days,
    "Film": Film,
    "Ticket": Ticket,
    "User": User,
    "Projection": Projection,
    "Hall": Hall,
    "Showtime": Showtime
}