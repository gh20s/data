"""
Handle environment-specific configuration settings.
Uses dotenv to read the configuration settings:
 - for local development, the filesystem will be walked up until a .env file is found.
 - for OpenShift deployment, the value is read from a deploymentconfig environment variable.
"""

import os

import dotenv


dotenv.load_dotenv()

DB_HOSTNAME = os.getenv('TEST_DB_HOSTNAME')
DB_PORT = int(os.getenv('TEST_DB_PORT', '5432'))
DB_NAME = os.getenv('TEST_DB_NAME')
DB_USERNAME = os.getenv('TEST_DB_USERNAME')
DB_PASSWORD = os.getenv('TEST_DB_PASSWORD')
