import mimetypes
import os

from flask import Blueprint, request

from server import db

get_image = Blueprint('api', __name__)

@get_image.route('/<name>', methods=['GET'])
def get_img(name):
    return name
