import mimetypes
import os

from flask import Blueprint, request, url_for

from server import PyMongo

share_x = Blueprint('api', __name__)

@share_x.route('/api/share_x', methods=['POST'])
def sx():
    # Get sent file, key, and name
    file = request.files['d']
    key = request.form.get('key')
    name = request.form.get('name')
    # Find file extension
    ext = mimetypes.guess_extension(file.content_type)

    # Check key agsint local key
    if key != os.getenv('SHAREX_KEY'):
        return 'Unauthorized!', 401
    
    # TODO: Save into mongodb
    # Save file
    file.save(os.path.join(f'{os.path.abspath("./")}/Share_X_Test', f'{name}{ext}'))
    
    return f'{os.getenv("URL")}/{name}{ext}', 200 
