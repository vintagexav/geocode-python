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
    TESTS HELPERS
    """
    def _create_user(self, email, address, id, should_fail=False):
        data = urlencode({
            'email': email,
            'address': address,
        })
        url = '/api/user/create'
        result = app.put(url, data=(data), headers=headers)#
        self.assertEqual('error' in result.json, False)
        print(result.json)
        self.assertEqual(result.status_code, 201)
        self.assertEqual(result.json['user']['email'], email)
        self.assertEqual(result.json['user']['address'], address)
        self.assertEqual(result.content_type, self.mimetype)
        self.assertEqual(result.json['user']['id'], id)
        self.assertEqual(result.json['user']['v'], 1) # new users are created with version = 1
        print(result.json)

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

    def test_1_create_users(self):
        self._create_user('marge@simpson.com', 'Brussels', 2)
