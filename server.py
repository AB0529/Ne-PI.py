# Imports
from flask import Flask
from termcolor import colored
from importlib import import_module
import os, config


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
# Routes in Routes directory
routes_dir = os.path.abspath('./Routes')
# List of all routes in dir
api_routes = [('Routes', r.rstrip('.py'), '/api') for r in os.listdir(routes_dir) if not r.startswith('__')]
# Register routes
register_bps(api_routes)

# Run app
app.run(port=config.PORT, debug=True)
