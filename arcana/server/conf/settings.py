"""
Evennia settings file.

The available options are found in the default settings file found
here:

/home/coret/Desktop/mud-devel/evennia/evennia/settings_default.py

Remember:

Don't copy more from the default file than you actually intend to
change; this will make sure that you don't overload upstream updates
unnecessarily.

When changing a setting requiring a file system path (like
path/to/actual/file.py), use GAME_DIR and EVENNIA_DIR to reference
your game folder and the Evennia library folders respectively. Python
paths (path.to.module) should be given relative to the game's root
folder (typeclasses.foo) whereas paths within the Evennia library
needs to be given explicitly (evennia.foo).

"""

# Use the defaults from Evennia unless explicitly overridden
from evennia.settings_default import *

######################################################################
# Evennia base server config
######################################################################

# This is the name of your game. Make it catchy!
SERVERNAME = "MageMUD"

#SLOW EXITS#
#BASE_EXIT_TYPECLASS = "evennia.contrib.slow_exit.SlowExit"

MULTISESSION_MODE=0

######################################################################
# Django web features
######################################################################
INSTALLED_APPS += ('web.chargen',
		'web.character',
                'web.ff',)
DEBUG = True
# The secret key is randomly seeded upon creation. It is used to sign
# Django's cookies. Do not share this with anyone. Changing it will
# log out all active web browsing sessions. Game web client sessions
# may survive.
SECRET_KEY = 'Tg"%FpD1+Px_sy0eIobz*92H)S@,jOE6|R=Y;~Vc'

WEBSERVER_PORTS = [(80, 5001)]
