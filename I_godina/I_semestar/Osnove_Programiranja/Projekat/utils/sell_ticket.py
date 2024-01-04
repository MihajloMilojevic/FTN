from datetime import datetime
from utils.get_selling_price import get_selling_price
from database.models import Ticket
from app.state import user

def sell_ticket(ticket: Ticket):
    ticket.sale_date = datetime.today()
    ticket.sold_price = get_selling_price(ticket)
    ticket.reserved = False
    ticket.seller_username = user.username
