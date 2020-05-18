from flask import request, jsonify, Blueprint
from ..models.Vehicle import Vehicle
from ..models.db import db
from ..routes.vehicle import routes_vehicle
from ..utils.error import res_error
import datetime

# ======
# CONTROLLER: VEHICLE
# ======

vehicle_api = Blueprint('vehicle_api', __name__)

@vehicle_api.route(**(routes_vehicle['delete']))
def delete_vehicle():
    try:
        if not request.form['vehicle_id']:
         raise Exception
        vehicle_id = int(request.form['vehicle_id']) # THIS MIGHT NOT EXIST
        vehicle = Vehicle.query.get(int(vehicle_id))
        Vehicle.query.filter_by(id=vehicle_id).delete()
        db.session.commit()
        res = {
            'vehicle_id': vehicle_id,
            'vehicle': vehicle.to_json(),
        }
        print(res)
        return jsonify(res), 200
    except Exception as e:
        res = res_error(e)
    return jsonify(res), 400
