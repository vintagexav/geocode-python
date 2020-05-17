from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from .db import db
from ..constants.bookingStatus import BookingStatus

# ======
# Booking
# ======

class Booking(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    created_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, nullable=True,)
    v = db.Column(db.Integer, nullable=False, default=1)
    #
    user = db.relationship('User', backref=db.backref('user_bookings', lazy=True))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    vehicle = db.relationship('Vehicle', backref=db.backref('vehicle_bookings', lazy=True))
    vehicle_id = db.Column(db.Integer, db.ForeignKey('vehicle.id'), nullable=False)
    status = db.Column(db.Integer, nullable=False, default=BookingStatus.CREATED)

    def to_json(self):
        res = {
            'id': self.id,
            'created_at': datetime.timestamp(self.created_at),
            'v': self.v,
            #
            'user_id': self.user_id,
            'vehicle_id': self.vehicle_id,
            'status': self.status
        }
        if self.updated_at:
            res['updated_at'] = datetime.timestamp(self.updated_at)
        return res

    def __repr__(self):
        return '<Booking #%s user %s vehicle %s>' % (self.id, self.user_id, self.vehicle_id)
