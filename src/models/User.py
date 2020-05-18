from flask_sqlalchemy import SQLAlchemy
import datetime
from .db import db

# ======
# MODEL: USER
# ======

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    created_at = db.Column(db.DateTime, nullable=False, default=datetime.datetime.utcnow)
    updated_at = db.Column(db.DateTime, nullable=True,)
    v = db.Column(db.Integer, nullable=False, default=1)
    #
    email = db.Column(db.String(50), unique=True, nullable=False)
    name = db.Column(db.String(50), nullable=True) # should be divided in firstname/lastname columns
    address = db.Column(db.String(200), unique=False, nullable=True)
    latlng = db.Column(db.String(80), unique=False, nullable=True)
#     role = db.Column(db.String(80), unique=False, nullable=False, default='user') # WARNINGit would be much cleaner to keep an associative table for this ;) > 1 table for user, 1 table for role, 1 table for user-role > and protect routes with decorator @roles_required - see https://flask-user.readthedocs.io/en/v0.5/authorization.html

    def to_json(self):
        res = {
            'id': self.id,
            'created_at': self.created_at.strftime("%d/%m/%Y-%H:%m:%S"),
            'v': self.v,
            #
            'email': self.email,
            'name': self.name,
            'address': self.address,
            'latlng': self.latlng,
            'bookings': list(map(lambda c:c.to_json(), self.user_bookings)),
            #             'role': self.role,# WARNINGit would be much cleaner to keep an associative table for this ;) > 1 table for user, 1 table for role, 1 table for user-role > and protect routes with decorator @roles_required - see https://flask-user.readthedocs.io/en/v0.5/authorization.html
        }
        if self.updated_at:
            res['updated_at'] = self.updated_at.strftime("%d/%m/%Y-%H:%m:%S")
        return res

    def __repr__(self):
        return '<User #%s %s>' % (self.id, self.name)
