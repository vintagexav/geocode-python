from ..utils.utils import print_result
from urllib.parse import urlencode

"""
VEHICLE TESTS HELPERS
"""
def delete_vehicle(self, id, expected={}, should_fail=False, failure_error_code=400):
    data = urlencode({
        'vehicle_id': id,
    })
    url = '/api/vehicle/delete'
    result = self.app.delete(url, data=(data), headers=self.headers)
    print_result(result.json)
    self.assertEqual('error' in result.json, should_fail)
    if should_fail:
        print_result(result.json)
    else:
        self.assertEqual(result.status_code, 200)
        self.assertEqual(result.json['vehicle_id'], id)


