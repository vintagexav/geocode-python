# ======
# CONSTANT: BOOKINGSTATUS
# ======

# The status is used to check in UNAVAILABLE_STATES if a vehicle can be booked

class BookingStatus:
    CREATED = 1
    CONFIRMED = 2
    STARTED = 3
    ENDED = 4
    UNAVAILABLE_STATES = [CREATED, CONFIRMED, STARTED, ENDED,]
