# Imports
import os
from importlib import import_module

from dotenv import load_dotenv
from flask import Flask
from flask_pymongo import PyMongo
from termcolor import colored

load_dotenv()

# Automaticly register blueprints from Routes dir
def register_bps(routes):
    # Get all routes
    for folder, module, prefix in routes:
        mod = import_module(folder)

        # Register route
        if hasattr(mod, module):
            bp = getattr(mod, module)

            if prefix.strip() == '/':
                app.register_blueprint(bp)
            else:
                app.register_blueprint(bp, url_prefix=prefix)


# Setup flask
def setup_app():
    app = Flask(__name__, static_folder='./Share_X_Test')

    return app


app = setup_app()
# Setup PyMongo
app.config['MONGO_URI'] = os.getenv('MONGO_URI')
# Register mongo
mongo = PyMongo(app)

# Routes in Routes directory
routes_dir = os.path.abspath('./Routes')
# List of all routes in dir
api_routes = [('Routes', r.rstrip('.py'), '/api') for r in os.listdir(routes_dir) if not r.startswith('__')]
# Register routes
register_bps(api_routes)

# Run app
app.run(port=os.getenv('PORT'), debug=True)
