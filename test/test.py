# ran with py.test test/test.py --log-cli-level=10 -s
from flask import json
from src.setup import setup
from src.models.db import db
import unittest
from flask_fixtures import FixturesMixin
from .helpers.user import create_user, get_users, update_user
from .helpers.booking import create_booking, get_booking
from .helpers.vehicle import delete_vehicle

created_app = setup('config/test.cfg')
app = created_app.test_client()
app.testing = True
config = {
    'tear_down_db': True,
}
class Tests(unittest.TestCase, FixturesMixin):
    fixtures = ['test/data.json']
    app = created_app
    db = db

    @classmethod
    def setUpClass(cls):
        pass

    @classmethod
    def tearDownClass(cls):
        pass

    def dropDb(self):
        if config['tear_down_db']:
            with created_app.app_context():
                db.drop_all()
                db.session.remove()
                print('test db dropped')
    """
    executed once before tests
    """
    def setUp(self):
        print('setting up tests')
        self.app = app
        self.mimetype = 'application/json'
        self.headers = {
            'Content-Type': 'application/x-www-form-urlencoded',
            'Accept': self.mimetype
        }

    """
    executed after each test
    """
    def tearDown(self):
        print('tearing down test')

    """
    tests
    """
    def test_1_create_users(self):
        create_user(self, 'marge@simpson.com', 'Brussels', {'id':2,},)
        create_user(self, 'maggy@simpson.com', 'Brussels', {'id':3,},)
        create_user(self, 'maggy@simpson.com', 'Brussels', {}, True, 400) # error because of same email adress
        get_users(self, {'users_count':3,},)

    def test_2_create_booking(self):
        create_booking(self, 1, 1, {'id':2,},)
        create_booking(self, 41, 69, {}, True) # error because entities do not exist

    def test_3_get_booking(self):
        get_booking(self, 1)
        create_booking(self, 1, 1, {'id':2,},)
        get_booking(self, 2)

    def test_4_delete_vehicle(self):
        delete_vehicle(self, 1)
        delete_vehicle(self, 1048, {}, True) # error because vehicle does not exist

    def test_5_update_user(self):
        create_user(self, 'charley@burns.com', 'Brussels', {'id':2,},)
        update_user(self, 2, 'charles.montgomery.Monty@burns.com')
        update_user(self, 42, '', True) # error because user does not exist
