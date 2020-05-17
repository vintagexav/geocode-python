from ..utils.utils import print_result
from urllib.parse import urlencode

"""
BOOKING TESTS HELPERS
"""

def create_booking(self, user_id, vehicle_id, expected={}, should_fail=False, failure_error_code=400):
    data = urlencode({
        'user_id': user_id,
        'vehicle_id': vehicle_id,
    })
    url = '/api/booking/create'
    result = self.app.put(url, data=(data), headers=self.headers)
    print_result(result.json)
    if (should_fail):
        self.assertEqual('error' in result.json, should_fail)
        self.assertEqual(result.status_code, failure_error_code)
    else:
        self.assertEqual(result.content_type, self.mimetype)
        self.assertEqual(result.status_code, 201)
        self.assertEqual(result.json['booking']['user_id'], user_id)
        self.assertEqual(result.json['booking']['vehicle_id'], vehicle_id)
        self.assertEqual(result.json['booking']['id'], expected['id'])
        self.assertEqual(result.json['booking']['v'], 1)

def get_booking(self, id, expected={}, should_fail=False, failure_error_code=400):
    data = urlencode({
        'booking_id': id,
    })
    url = '/api/booking/get'
    result = self.app.get(url, data=(data), headers=self.headers)
    print_result(result.json)
    self.assertEqual('error' in result.json, should_fail)
    self.assertEqual(result.status_code, 200)
    self.assertEqual(result.json['booking']['id'], id)
