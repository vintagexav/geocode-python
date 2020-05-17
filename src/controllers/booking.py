from flask import request, jsonify, Blueprint
from ..models.User import User
from ..models.Vehicle import Vehicle
from ..models.Booking import Booking
from ..models.db import db
from ..routes.booking import routes_booking
from ..utils.error import res_error
from datetime import datetime

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
