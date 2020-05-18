from ..utils.utils import print_result
import urllib

"""
BOOKING TESTS HELPERS
"""

def create_booking(self, user_id, vehicle_id, expected={}, should_fail=False, failure_error_code=400):
    data = urllib.urlencode({
        'user_id': user_id,
        'vehicle_id': vehicle_id,
    })
    url = '/api/booking/create'
    result = self.app.put(url, data=(data), headers=self.headers)
    print_result(result.json)
    if (should_fail): # KO ERROR
        self.assertEqual('error' in result.json, should_fail)
        self.assertEqual(result.status_code, failure_error_code)
    else: # OK
        self.assertEqual(result.content_type, self.mimetype)
        self.assertEqual(result.status_code, 201)
        self.assertEqual(result.json['booking']['user_id'], user_id)
        self.assertEqual(result.json['booking']['vehicle_id'], vehicle_id)
        self.assertEqual(result.json['booking']['id'], expected['id'])
        self.assertEqual(result.json['booking']['v'], 1)

def get_booking(self, booking_id, expected={}, should_fail=False, failure_error_code=400):
    data = urllib.urlencode({
        'booking_id': booking_id,
    })
    url = '/api/booking/get'
    result = self.app.get(url, data=(data), headers=self.headers)
    print_result(result.json)
    if should_fail: # KO ERROR
        print_result(result.json)
        self.assertEqual(result.status_code, failure_error_code)
    else: # OK
        self.assertEqual('error' in result.json, should_fail)
        self.assertEqual(result.status_code, 200)
        self.assertEqual(result.json['booking']['id'], booking_id)

