# STEPS TO EXECUTE THE TEST
# APPLICATION SHOULD BE RUNNING
# py test_env_services.py

import os
import unittest
import json
from settings import TEST_DATABASE_URL
from flask_sqlalchemy import SQLAlchemy
from app import create_app
from models import setup_db, Region, Service

# TEST_DATABASE_URL=os.getenv("TEST_DATABASE_URL")
new_region_id = -1
new_service_id = -1

class EnvServicesTestCase(unittest.TestCase):
    """This class represents the Environment services test cases"""

    def setUp(self):
        """Define test variables and initialize app."""
        self.app = create_app()
        self.client = self.app.test_client
        self.database_path = TEST_DATABASE_URL

        setup_db(self.app, self.database_path)

        # binds the app to the current context
        with self.app.app_context():
            self.db = SQLAlchemy()
            self.db.init_app(self.app)
            # create all tables
            self.db.create_all()

    def tearDown(self):
        """Executed after reach test"""
        pass

    '''
    Test case for creating region
    '''

    def test_create_region(self):
        test_payload = {
        "name": "Thookukudi",
        "city": "Chennai",
        "state": "Tamil Nadu",
        "country": "India",
        "regionhead": "Amutha"
        }
        res = self.client().post('/regions', json=test_payload)
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['created'])

    '''
    Test for GET request for all the regions
    '''
    def test_get_regions(self):
        res = self.client().get('/regions')
        print('In get regions: res: ' + str(res))
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['regions'])

    '''
    Test for test_get_a_region
    '''
    def test_get_a_region(self):
        res = self.client().get('/regions/1')
        #print('In get regions: res: ' + str(res))
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['region'])

    '''
    Test for update region
    '''
    def test_update_region(self):
        test_payload = {
            "name": "RR Nagar",
            "regionhead": "Priya"
            }
        res = self.client().patch('/regions/3', json=test_payload)
        #print('In get regions: res: ' + str(res))
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['updated'])

    '''
    Test for delete region
    '''
    def test_delete_region(self):
        res = self.client().delete('/regions/3')
        #print('In get regions: res: ' + str(res))
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['deleted'])

# Make the tests conveniently executable
if __name__ == "__main__":
    unittest.main()
