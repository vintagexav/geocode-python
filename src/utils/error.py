from flask import jsonify
import sys

# ======
# ERROR
# ======

def error_404(name, error):
    print(error)
    return jsonify({
        'type': 404,
        'source':'%s' % name,
        'details': '%s' % error
    })

def res_error(e):
    error_string = 'Unexpected error %s' % e
    print(error_string)
    res = {
        'error': error_string,
        'type': str(sys.exc_info()[0]),
    }
    return res
