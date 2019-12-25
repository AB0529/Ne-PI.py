from flask import Blueprint

test = Blueprint('api', __name__)

@test.route('/test')
def run():
    return {'message': 'Test success!', 'state': 'success', 'code': 200}, 200
