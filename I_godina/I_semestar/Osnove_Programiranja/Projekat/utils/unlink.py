import app.state as State
import database.models as Models

def unlink_showtime(showtime_id: str):
    def should_delete(ticket: Models.Ticket):
        return ticket.showtime_id == showtime_id
    State.db.tickets.Delete(should_delete)

def unlink_projection(projection_id: str):
    def should_delete(showtime: Models.Showtime):
        return showtime.projection_id == projection_id
    showtimes: list[Models.Showtime] = State.db.showtimes.Select(should_delete)
    for showtime in showtimes:
        unlink_showtime(showtime.id)
        State.db.showtimes.DeleteById(showtime.id)

def unlink_film(film_id: str):
    def should_delete(projection: Models.Projection):
        return projection.film_id == film_id
    projections: list[Models.Projection] = State.db.projections.Select(should_delete)
    for projection in projections:
        unlink_projection(projection.id)
        State.db.projections.DeleteById(projection.id)

def unlink_hall(hall_id: str):
    def should_delete(projection: Models.Projection):
        return projection.hall_id == hall_id
    projections: list[Models.Projection] = State.db.projections.Select(should_delete)
    for projection in projections:
        unlink_projection(projection.id)
        State.db.projections.DeleteById(projection.id)

