# ran with py.test test/test.py --log-cli-level=10 -s
from flask import json
from src.setup import setup
from src.models.db import db
import unittest
from urllib.parse import urlencode
from flask_fixtures import FixturesMixin

created_app = setup('config/test.cfg')
app = created_app.test_client()
app.testing = True
mimetype = 'application/json'
headers = {
    'Content-Type': 'application/x-www-form-urlencoded',
    'Accept': mimetype
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

    """
    executed before tests
    """
    def setUp(self):
        print('setting up tests')

    """
    executed after each test
    """
    def tearDown(self):
        print('tearing down test')

    def test_0_true(self):
        self.assertEqual(True, True)
