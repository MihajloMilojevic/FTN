import database.models as Models
import app.state as State
import utils.serialize as Serialize
from datetime import datetime, timedelta

def report_a(date: datetime):
    def check(ticket: Models.Ticket):
        if ticket.reserved:
            return False
        return ticket.sale_date.date() == date.date()
    return [map_ticket(ticket) for ticket in State.db.tickets.Select(check)]

def report_b(date: datetime):
    def check(ticket: Models.Ticket):
        if ticket.reserved:
            return False
        showtime: Models.Showtime = ticket.showtime.get(State.db)
        return showtime.date.date() == date.date()
    return [map_ticket(ticket) for ticket in State.db.tickets.Select(check)]

def report_c(date: datetime, seller_name: str):
    if seller_name.strip() == "":
        return (0, 0)
    name, surname = seller_name.split()
    def isSeller(seller: Models.User):
        return seller.name == name and seller.surname == surname
    seller: Models.User = State.db.users.Select(isSeller)[0]
    def check(ticket: Models.Ticket):
        if ticket.reserved:
            return False
        return ticket.sale_date.date() == date.date() and ticket.seller_username == seller.username
    return [map_ticket(ticket) for ticket in State.db.tickets.Select(check)]

def report_d(day: Models.Days):
    def check(ticket: Models.Ticket):
        if ticket.reserved:
            return False
        ticket_day = Models.Days.all_days[ticket.sale_date.weekday()]
        return ticket_day == day
    prices: list[float] =  [ticket.sold_price for ticket in State.db.tickets.Select(check)]
    total_price = sum(prices)
    return (len(prices), total_price)

def report_e(day: Models.Days):
    def check(ticket: Models.Ticket):
        if ticket.reserved:
            return False
        showtime: Models.Showtime = ticket.showtime.get(State.db)
        showtime_day = Models.Days.all_days[showtime.date.weekday()]
        return showtime_day == day
    prices: list[float] =  [ticket.sold_price for ticket in State.db.tickets.Select(check)]
    total_price = sum(prices)
    return (len(prices), total_price)

def report_f(film_name: str):
    def check(ticket: Models.Ticket):
        if ticket.reserved:
            return False
        showtime: Models.Showtime = ticket.showtime.get(State.db)
        projection: Models.Projection = showtime.projection.get(State.db)
        film: Models.Film = projection.film.get(State.db)
        return film.name == film_name
    prices: list[float] =  [ticket.sold_price for ticket in State.db.tickets.Select(check)]
    total_price = sum(prices)
    return (len(prices), total_price)


def report_g(day: Models.Days, seller_name: str):
    if seller_name.strip() == "":
        return (0, 0)
    name, surname = seller_name.split()
    def isSeller(seller: Models.User):
        return seller.name == name and seller.surname == surname
    seller: Models.User = State.db.users.Select(isSeller)[0]
    def check(ticket: Models.Ticket):
        if ticket.reserved:
            return False
        ticket_day = Models.Days.all_days[ticket.sale_date.weekday()]
        return ticket_day == day and ticket.seller_username == seller.username
    prices: list[float] =  [ticket.sold_price for ticket in State.db.tickets.Select(check)]
    total_price = sum(prices)
    return (len(prices), total_price)

def report_h():
    data: dict[str, list[float]] = {}
    for user in State.db.users.SelectAll():
        if user.role != Models.Roles.prodavac:
            continue
        data[user.username] = []
    for ticket in State.db.tickets.SelectAll():
        if ticket.reserved:
            continue
        diff: timedelta = datetime.today() - ticket.sale_date
        if diff.days > 30:
            continue
        data[ticket.seller_username].append(ticket.sold_price)
    return [
        {
            "seller": seller_username, 
            "number": str(len(data[seller_username])), 
            "total": str(sum(data[seller_username]))
        } 
        for seller_username in data
    ]


def map_ticket(ticket: Models.Ticket):
    showtime: Models.Showtime = ticket.showtime.get(State.db)
    showtime
    projection: Models.Projection = showtime.projection.get(State.db)
    hall: Models.Hall = projection.hall.get(State.db)
    film: Models.Film = projection.film.get(State.db)
    name = ticket.full_name
    if name is None:
        user: Models.User = ticket.user.get(State.db)
        name = f"{user.name} {user.surname}"
    seller = ""
    if ticket.seller_username is not None:
        seller_user: Models.User = ticket.seller.get(State.db)
        seller = f"{seller_user.name} {seller_user.surname}"
    return {
        "id": ticket.id,
        "film": film.name,
        "hall": hall.id,
        "date": Serialize.serialize_date(showtime.date),
        "starting_time": Serialize.serialize_time(projection.starting_time),
        "ending_time": Serialize.serialize_time(projection.ending_time),
        "seat_tag": ticket.seat_tag,
        "status": "Rezervisano" if ticket.reserved else "Prodato",
        "name": name,
        "seller": seller
    }