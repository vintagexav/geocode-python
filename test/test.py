# ran with py.test test/test.py --log-cli-level=10 -s
from flask import json
from src.setup import setup
from src.models.db import db
import unittest
from flask_fixtures import FixturesMixin
from .helpers.user import create_user, get_users
from .helpers.booking import create_booking

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
        self.dropDb()

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
