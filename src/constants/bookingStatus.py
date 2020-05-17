# ======
# BookingStatus
# ======

# The status is useful so that we can check in UNAVAILABLE_STATES if a vehicle can be booked

class BookingStatus:
    CREATED = 0
    CONFIRMED = 1
    STARTED = 2
    ENDED = 3
    UNAVAILABLE_STATES = [CREATED, CONFIRMED, STARTED, ENDED,]
