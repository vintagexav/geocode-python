from ..utils.utils import print_result
import urllib

"""
VEHICLE TESTS HELPERS
"""
def delete_vehicle(self, vehicle_id, expected={}, should_fail=False, failure_error_code=400):
    data = urllib.urlencode({
        'vehicle_id': vehicle_id,
    })
    url = '/api/vehicle/delete'
    result = self.app.delete(url, data=(data), headers=self.headers)
    print_result(result.json)
    self.assertEqual('error' in result.json, should_fail)
    if should_fail: # KO ERROR
        self.assertEqual(result.status_code, failure_error_code)
    else: # OK
        self.assertEqual(result.status_code, 200)
        self.assertEqual(result.json['vehicle_id'], vehicle_id)


