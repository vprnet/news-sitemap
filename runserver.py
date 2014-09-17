#!/usr/local/bin/python2.7

import sys

from main import app
from flask_frozen import Freezer

if len(sys.argv) > 1 and sys.argv[1] == 'freeze':
    freezer = Freezer(app)
    freezer.freeze()
else:
    app.debug = True
    app.run()
