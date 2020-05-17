from flask_sqlalchemy import SQLAlchemy
import datetime
from .db import db

# ======
# VEHICLE
# ======

class Vehicle(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    created_at = db.Column(db.DateTime, nullable=False, default=datetime.datetime.utcnow)
    updated_at = db.Column(db.DateTime, nullable=True,)
    v = db.Column(db.Integer, nullable=False, default=1)
    #
    brand = db.Column(db.String(50), unique=False, nullable=False)
    license_plate = db.Column(db.String(50), unique=True, nullable=False)

    def to_json(self):
        res = {
            'id': self.id,
            'license_plate': self.license_plate,
            'created_at': datetime.timestamp(self.created_at),
            'v': self.v,
            #
            'brand': self.brand,
        }
        if self.updated_at:
            res['updated_at'] = datetime.timestamp(self.updated_at)
        return res

    def __repr__(self):
        return '<Vehicle #%s %s - %s>' % (self.id, self.brand,self.license_plate)
