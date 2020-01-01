'''
Pretty much an automatic way to
from ROUTE import *
'''

import os, importlib

for r in os.listdir('./Routes'):
    # Ignore init file
    if r.startswith('__'):
        continue

    # Get filename
    r = r.split('.py')[0]
    # Import file
    module = importlib.import_module(f'.{r}', package='Routes')

    if (hasattr(module, '__all__')):
        all_names = module.__all__
    else:
        all_names = [name for name in dir(module) if not name.startswith('__')]
    
    # Update global with modules
    globals().update({name: getattr(module, name) for name in all_names})