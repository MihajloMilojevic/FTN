from datetime import datetime
from utils.get_selling_price import get_selling_price
from database.models import Ticket
import app.state as State

def sell_ticket(ticket: Ticket):
    ticket.sale_date = datetime.today()
    ticket.sold_price = get_selling_price(ticket)
    ticket.reserved = False
    print(State.user.toJsonString(2))
    if State.user is not None:
        ticket.seller_username = State.user.username
