# STEPS TO EXECUTE THE TEST
# 1. The test database should have been created - eg. test_envsrvdb
# 2. The following environment variable should be set :
#    TEST_DATABASE_URL=postgresql://postgres:postgres@localhost:5432/test_envsrvdb
# Run the test python class
# py test_env_services.py

import os
import unittest
import json
import string
import random
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
    Test case for creating, reading, updating and deleting region
    '''

    def test_create_read_update_delete_region(self):
        #generate random name for region
        region_name = 'test_'.join(random.choices(string.ascii_uppercase +
                             string.digits, k = 7))

        # CREATE REGION
        test_payload = {
        "name": region_name,
        "city": "Chennai",
        "state": "Tamil Nadu",
        "country": "India",
        "regionhead": "Anitha"
        }
        res = self.client().post('/regions', json=test_payload)
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['created'])

        created_region_id = data['created']
        print('created a region with id:'+ str(created_region_id))

        # READ A REGION
        res = self.client().get('/regions/'+ str(created_region_id))
        # print('In get regions: res: ' + str(res))
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['region'])
        print('read a region with id:' + str(created_region_id))

        # UPDATE A REGION
        test_payload = {
            "regionhead": "AnithaKarunakaran"
        }
        res = self.client().patch('/regions/'+ str(created_region_id), json=test_payload)
        # print('In get regions: res: ' + str(res))
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['updated'])
        print('updated a region with id:' + str(created_region_id))

        # DELETE A REGION
        res = self.client().delete('/regions/'+ str(created_region_id))
        # print('In get regions: res: ' + str(res))
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['deleted'])
        print('deleted a region with id:' + str(created_region_id))

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
    Test case for creating, reading, updating and deleting region
    '''

    def test_create_read_update_delete_service(self):
        print('******************** SERVICE TESTS START ********************')
        # generate random name for region
        rnd_region_name = 'rg_'.join(random.choices(string.ascii_uppercase +
                                                  string.digits, k=7))

        # CREATE REGION
        test_region_payload = {
            "name": rnd_region_name,
            "city": "Chennai",
            "state": "Tamil Nadu",
            "country": "India",
            "regionhead": "Anitha"
        }
        res = self.client().post('/regions', json=test_region_payload)
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['created'])

        created_region_id = data['created']
        print('created a region with id:' + str(created_region_id))

        #generate random name for region
        service_name = ''.join(random.choices(string.ascii_uppercase +
                             string.digits, k = 7))

        # CREATE SERVICE WITH RANDOM SERVICE NAME FOR THE NEW REGION CREATED ABOVE
        test_payload = {
            "name": service_name,
            "type": "Test Service Type ",
            "address": "Test Address",
            "region_id": created_region_id,
            "email": "info@ssrms.com",
            "phone": "+91-1112223344",
            "website": "www.ssrms.com"
        }
        res = self.client().post('/services', json=test_payload)
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['created'])

        created_service_id = data['created']
        print('created a service with id:'+ str(created_service_id) +" name: "+ service_name)

        # READ A SERVICE
        res = self.client().get('/services/'+ str(created_service_id))
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['service'])
        print('read a service with id:' + str(created_service_id))

        # UPDATE A SERVICE
        test_update_service_payload = {
            "address": "Test Address",
            "phone": "+91-1112223344"
        }
        res = self.client().patch('/services/'+ str(created_service_id), json=test_update_service_payload)
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['updated'])
        print('updated a service with id:' + str(created_service_id))

        # DELETE A SERVICE
        res = self.client().delete('/services/'+ str(created_service_id))
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['deleted'])
        print('deleted a service with id:' + str(created_service_id))

        # DELETE A PARENT REGION
        # res = self.client().delete('/regions/'+ str(created_region_id))
        # # print('In get regions: res: ' + str(res))
        # data = json.loads(res.data)
        # self.assertEqual(res.status_code, 200)
        # self.assertEqual(data['success'], True)
        # self.assertTrue(data['deleted'])
        # print('deleted a region with id:' + str(created_region_id))

# Make the tests conveniently executable
if __name__ == "__main__":
    unittest.main()
