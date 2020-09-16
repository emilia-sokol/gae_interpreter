"""`appengine_config` gets loaded when starting a new application instance."""
import sys
import os.path
from google.appengine.ext import vendor
# add `lib` subdirectory to `sys.path`, so our `main` module can load
# third-party libraries.
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'lib'))


# Add any libraries installed in the "lib" folder.
# windows
# vendor.add('venv/Lib/site-packages')

# ubuntu
vendor.add('venv/lib/python2.7/site-packages')

#for tests
# vendor.add('../venv/lib/python2.7/site-packages')

# uncomment if third party lib was copied to /lib directory
# vendor.add('lib')
