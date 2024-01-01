import app.state as State
import database.models as Models

def generate_seating_plan(showtime_id):
    showtime: Models.Showtime = State.db.showtimes.SelectById(showtime_id)
    projection: Models.Projection = showtime.projection.get(State.db)
    hall: Models.Hall = projection.hall.get(State.db)
    tickets: list[Models.Ticket] = State.db.tickets.Select(lambda ticket: ticket.showtime_id == showtime_id)
    seating_plan = []
    for _ in range(hall.row_count):
        seating_plan.append([Models.SeatStatus.free] * hall.row_count)
    for ticket in tickets:
        row, column = map_seat(ticket.seat_tag)
        seating_plan[row][column] = Models.SeatStatus.occupied
    return seating_plan

def map_seat(seat_tag):
    row_part, column_part = seat_tag.split("-")
    row_number = int(row_part) - 1
    column_number = ord(column_part) - ord("A")
    return row_number, column_number