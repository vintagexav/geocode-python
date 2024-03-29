from flask import request, jsonify, Blueprint
from ..models.User import User
from ..models.db import db
from ..routes.user import routes_user
from ..utils.error import res_error
from datetime import datetime
import os
import geocoder

# ======
# CONTROLLER: USER
# ======

user_api = Blueprint('user_api', __name__)

@user_api.route(**(routes_user['create']))
def create_user():
    try:
        email = request.form['email'] if 'email' in request.form else ''
        address  =  request.form['address'] if 'address' in request.form else ''
        googlekey = os.getenv('GEOCODE_KEY')
        g = geocoder.google(address, key=googlekey)
        latlng = g.latlng if g.latlng else '' # WARNING without a correct GEOCODE_KEY as env key, lat lng wil be empty
        #
        user = User(email=email, name='', address=address, latlng=latlng)
        db.session.add(user)
        db.session.commit()
        res = {
            'user': user.to_json(),
        }
        return jsonify(res), 201
    except Exception as e:
        db.session.rollback()
        res = res_error(e)
    return jsonify(res), 400

@user_api.route(**(routes_user['update']))
def update_user():
    try:
        email = request.form['email'] # THIS MIGHT NOT EXIST
        user_id = request.form['user_id'] # THIS MIGHT NOT EXIST
        #
        user = User.query.get(int(user_id))
        user.email = email
        user.updated_at = datetime.utcnow()
        user.v = user.v+1
        db.session.commit()
        res = {
            'user': user.to_json(),
        }
        return jsonify(res), 200
    except Exception as e:
        res = res_error(e)
    return jsonify(res), 400

@user_api.route(**(routes_user['all']))
def get_all_users():
    res = {
        'users': list(map(lambda u:u.to_json(), User.query.all())),
    }
    return jsonify(res), 200
