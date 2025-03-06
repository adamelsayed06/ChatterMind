#database settings, JWT secrets, credentials etc.

import os

class TestingConfig():
    SQLALCHEMY_DATABASE_URI = os.environ.get('TEST_DATABASE_URL') or 'sqlite:///test.db'
    TESTING = True  #Enable testing mode (disables error catching)

