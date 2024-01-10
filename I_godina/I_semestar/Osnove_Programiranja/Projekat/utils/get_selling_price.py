import database.models as Models
from constants import LOYALTY_DISCOUNT_PERCENT, PRICE_ADJUSTMENTS_PER_DAY
import app.state as State
from utils.check_for_loyalty import check_loyalty

def get_selling_price(ticket: Models.Ticket) -> float:
    showtime: Models.Showtime = ticket.showtime.get(State.db)
    projection: Models.Projection = showtime.projection.get(State.db)
    selling_price: float = projection.price
    if check_loyalty(ticket.username):
        selling_price -= selling_price * (LOYALTY_DISCOUNT_PERCENT / 100)
    selling_price += PRICE_ADJUSTMENTS_PER_DAY[showtime.date.weekday()]
    return round(selling_price, 2)