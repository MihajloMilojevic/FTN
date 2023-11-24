from Database.Models.Enums import Roles, Genres, Days
from Database.Models.Film import Film
from Database.Models.Ticket import Ticket
from Database.Models.User import User
from Database.Models.Projection import Projection
from Database.Models.Hall import Hall
from Database.Models.Showtime import Showtime

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