from urllib.parse import urlencode

"""
USER TESTS HELPERS
"""

def create_user(self, email, address, expected, should_fail=False):
    data = urlencode({
        'email': email,
        'address': address,
    })
    url = '/api/user/create'
    result = self.app.put(url, data=(data), headers=self.headers)
    print(result.json)
    self.assertEqual('error' in result.json, should_fail)
    self.assertEqual(result.content_type, self.mimetype)
    self.assertEqual(result.status_code, 201)
    self.assertEqual(result.json['user']['email'], email)
    self.assertEqual(result.json['user']['address'], address)
    self.assertEqual(result.json['user']['id'], expected['id'])
    self.assertEqual(result.json['user']['v'], 1) # new users are created with version = 1

def get_users(self, expected, should_fail=False):
    data = urlencode({})
    url = '/api/user/all'
    result = self.app.get(url, data=(data), headers=self.headers)
    print(result.json)
    self.assertEqual('error' in result.json, should_fail)
    self.assertEqual(result.content_type, self.mimetype)
    self.assertEqual(result.status_code, 200)
    self.assertEqual(len(result.json['users']), expected['users_count'])