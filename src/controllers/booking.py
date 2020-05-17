from flask import request, jsonify, Blueprint
from ..models.User import User
from ..models.Vehicle import Vehicle
from ..models.Booking import Booking
from ..models.db import db
from ..routes.booking import routes_booking
from ..utils.error import res_error
from ..constants.bookingStatus import BookingStatus

# ======
# BOOKING
# ======

booking_api = Blueprint('booking_api', __name__)

@booking_api.route(**(routes_booking['create']))
def create_booking():
    try:
        user_id = request.form['user_id'] # mandatory in Model
        vehicle_id  =  request.form['vehicle_id'] # mandatory in Model
        #
        user = db.session.query(User).get(int(user_id))
        vehicle = db.session.query(Vehicle).get(int(vehicle_id))
        if vehicle.vehicle_bookings: # let's check if the vehicle is available
            vehicle_is_busy = list(map(lambda v: v.status in BookingStatus.UNAVAILABLE_STATES, vehicle.vehicle_bookings))[0]
            if vehicle_is_busy:
                res = res_error('Vehicle is already booked')
                return jsonify(res), 409
        print('...\n\n')
        booking = Booking(user=user, vehicle=vehicle)
        db.session.add(booking)
        db.session.commit()
        res = {
            'booking': booking.to_json(),
        }
        return jsonify(res), 201
    except Exception as e:
        db.session.rollback()
        res = res_error(e)
    return jsonify(res), 400

@booking_api.route(**(routes_booking['get']))
def get_booking():
    try:
        booking_id = request.form['booking_id']
        #
        booking = Booking.query.get(int(booking_id))
        res = {
            'booking': booking.to_json(),
        }
        return jsonify(res), 200
    except Exception as e:
        res = res_error(e)
    return jsonify(res), 400
