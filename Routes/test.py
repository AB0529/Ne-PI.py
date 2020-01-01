from flask import Blueprint

test = Blueprint('api', __name__)

@test.route('/api/test', methods=['GET'])
def tst():
    return {'message': 'Test success!', 'state': 'success', 'code': 200}, 200
