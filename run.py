from locale import currency
from booking.booking import Booking

with Booking() as bot:
    bot.land_first_page()
    # bot.change_currency(currency="EUR")
    bot.search_location('Orlando, FL')
    bot.select_dates(leaving="2022-02-10", returning="2022-02-28")