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
    def _create_user(self, email, address, expected, should_fail=False):
        data = urlencode({
            'email': email,
            'address': address,
        })
        url = '/api/user/create'
        result = app.put(url, data=(data), headers=headers)
        print(result.json)
        self.assertEqual('error' in result.json, should_fail)
        self.assertEqual(result.content_type, mimetype)
        self.assertEqual(result.status_code, 201)
        self.assertEqual(result.json['user']['email'], email)
        self.assertEqual(result.json['user']['address'], address)
        self.assertEqual(result.json['user']['id'], expected['id'])
        self.assertEqual(result.json['user']['v'], 1) # new users are created with version = 1

    def _get_users(self, expected, should_fail=False):
        data = urlencode({})
        url = '/api/user/all'
        result = app.get(url, data=(data), headers=headers)
        print(result.json)
        self.assertEqual('error' in result.json, should_fail)
        self.assertEqual(result.content_type, mimetype)
        self.assertEqual(result.status_code, 200)
        self.assertEqual(len(result.json['users']), expected['users_count'])


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
        self._create_user('marge@simpson.com', 'Brussels', {'id':2,})
        self._get_users({'users_count':2,})
