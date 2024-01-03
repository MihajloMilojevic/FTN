import database.models as Models
from constants import LOYALTY_SUM
from datetime import datetime
import app.state as State

def check_loyalty(username) -> bool:
    def check(ticket: Models.Ticket) -> bool:
        if ticket.reserved:
            return False
        if ticket.username is None:
            return False
        if ticket.username != username:
            return False
        today = datetime.now()
        last_year = today.replace(year=today.year-1)
        if ticket.sale_date < last_year:
            return False
        return True
    if username is None:
        return False
    tickets = State.db.tickets.Select(check)
    total_value = sum([ticket.sold_price for ticket in tickets])
    return total_value >= LOYALTY_SUM