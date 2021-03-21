# STEPS TO EXECUTE THE TEST
# 1. The test database should have been created - eg. test_envsrvdb
# 2. The following environment variable should be set (setup_test_jwt.bat)
# TEST_DATABASE_URL=postgresql://postgres:postgres@localhost:5432/test_envsrvdb
# CHIEF_OFFICER_JWT should contain valid JWT of CHIEF_OFFICER
# SERVICES_MANAGER_JWT should contain valid JWT of SERVICES_MANAGER_JWT
# 3. Run the test python class
# py test_app.py

import os
import unittest
import json
import string
import random
from settings import TEST_DATABASE_URL, CHIEF_OFFICER_JWT, SERVICES_MANAGER_JWT
from flask_sqlalchemy import SQLAlchemy
from app import create_app
from models import setup_db, Region, Service
from test_util import generate_region_payload, generate_service_payload

new_region_id = -1
new_service_id = -1
CHIEF_OFFICER_JWT = str(CHIEF_OFFICER_JWT)


class EnvServicesTestCase(unittest.TestCase):
    """This class represents the Environment services test cases"""

    def setUp(self):
        """Define test variables and initialize app."""
        self.app = create_app()
        self.client = self.app.test_client
        self.headers = {'Content-Type': 'application/json'}
        self.database_path = TEST_DATABASE_URL

        setup_db(self.app, self.database_path)

        # binds the app to the current context
        with self.app.app_context():
            self.db = SQLAlchemy()
            self.db.init_app(self.app)
            # recreate all tables
            self.db.drop_all()
            self.db.create_all()

    def tearDown(self):
        """Executed after reach test"""
        pass

    '''
    Region
    '''
    '''
    Create Region - Only by Chief Officer
    '''
    def test_public_create_region(self):
        '''
        Public - Without authorization headers - Cannot create regions
        '''
        test_payload = generate_region_payload()
        res = self.client().post('/regions', json=test_payload)
        self.assertEqual(res.status_code, 401)

        '''
        Services Manager - Cannot create regions
        '''
        test_payload = generate_region_payload()
        self.headers.update(
            {'Authorization': 'Bearer ' + SERVICES_MANAGER_JWT})
        res = self.client().post('/regions', json=test_payload,
                                 headers=self.headers)
        self.assertEqual(res.status_code, 401)

        '''
        CHIEF OFFICER - Can create regions
        '''
        test_payload = generate_region_payload()
        self.headers.update({'Authorization': 'Bearer ' + CHIEF_OFFICER_JWT})
        res = self.client().post('/regions', json=test_payload,
                                 headers=self.headers)
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['created'])

    '''
    Read a Region Detail - Every one can
    '''
    def test_read_a_region(self):
        # Create Region by Chief Officer
        test_payload = generate_region_payload()
        self.headers.update({'Authorization': 'Bearer ' + CHIEF_OFFICER_JWT})
        res = self.client().post('/regions', json=test_payload,
                                 headers=self.headers)
        data = json.loads(res.data)
        created_region_id = data['created']

        # Read a region detail by Public
        res = self.client().get('/regions/' + str(created_region_id))
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['region'])

        # Read a region detail by Services Manager
        self.headers.update(
            {'Authorization': 'Bearer ' + SERVICES_MANAGER_JWT})
        res = self.client().get(
            '/regions/' +
            str(created_region_id),
            headers=self.headers)
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['region'])

        # Read a region detail by Chief Officer
        self.headers.update({'Authorization': 'Bearer ' + CHIEF_OFFICER_JWT})
        res = self.client().get(
            '/regions/' +
            str(created_region_id),
            headers=self.headers)
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['region'])

    '''
    Read All Regions - Everyone can
    '''
    def test_get_regions(self):
        res = self.client().get('/regions')
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['regions'])

    '''
    Update a region - Only a Chief Officer can
    '''
    def test_update_a_region(self):
        # Create Region by Chief Officer
        test_payload = generate_region_payload()
        self.headers.update({'Authorization': 'Bearer ' + CHIEF_OFFICER_JWT})
        res = self.client().post('/regions', json=test_payload,
                                 headers=self.headers)
        self.assertEqual(res.status_code, 200)
        data = json.loads(res.data)
        created_region_id = data['created']

        test_payload = {
            "regionhead": "AnithaKarunakaran"
        }

        # UPDATE A REGION BY PUBLIC - NOT ALLOWED
        res = self.client().patch('/regions/' + str(created_region_id),
                                  json=test_payload)
        self.assertEqual(res.status_code, 401)

        # UPDATE A REGION BY SERVICES MANAGER - NOT ALLOWED
        self.headers.update(
            {'Authorization': 'Bearer ' + SERVICES_MANAGER_JWT})
        res = self.client().patch(
            '/regions/' +
            str(created_region_id),
            json=test_payload,
            headers=self.headers)
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 401)

        # UPDATE A REGION BY CHIEF OFFICER
        self.headers.update({'Authorization': 'Bearer ' + CHIEF_OFFICER_JWT})
        res = self.client().patch(
            '/regions/' +
            str(created_region_id),
            json=test_payload,
            headers=self.headers)
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['updated'])

    '''
    Delete a region - Only a Chief Officer can
    '''
    def test_delete_a_region(self):
        # Create Region by Chief Officer
        test_payload = generate_region_payload()
        self.headers.update({'Authorization': 'Bearer ' + CHIEF_OFFICER_JWT})
        res = self.client().post('/regions', json=test_payload,
                                 headers=self.headers)
        self.assertEqual(res.status_code, 200)
        data = json.loads(res.data)
        created_region_id = data['created']

        # Public cannot delete a region
        res = self.client().delete('/regions/' + str(created_region_id))
        self.assertEqual(res.status_code, 401)

        # Services Manager cannot delete a region
        self.headers.update(
            {'Authorization': 'Bearer ' + SERVICES_MANAGER_JWT})
        res = self.client().delete(
            '/regions/' + str(created_region_id),
            headers=self.headers)
        self.assertEqual(res.status_code, 401)

        # Chief Officer can delete a region
        self.headers.update({'Authorization': 'Bearer ' + CHIEF_OFFICER_JWT})
        res = self.client().delete(
            '/regions/' + str(created_region_id),
            headers=self.headers)
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['deleted'])

    '''
    Services
    '''
    '''
    Create a new Service - Only Service Manager and Chief Officer can
    '''
    def test_create_service(self):
        # Create a new region by chief officer
        test_region_payload = generate_region_payload()
        self.headers.update({'Authorization': 'Bearer ' + CHIEF_OFFICER_JWT})
        res = self.client().post(
            '/regions',
            json=test_region_payload,
            headers=self.headers)
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['created'])
        created_region_id = data['created']

        # Create a new service by Services Manager
        test_payload = generate_service_payload(created_region_id)
        self.headers.update(
            {'Authorization': 'Bearer ' + SERVICES_MANAGER_JWT})
        res = self.client().post('/services', json=test_payload,
                                 headers=self.headers)
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['created'])
        created_service_id = data['created']

        # Create a new service by Chief Officer
        test_payload = generate_service_payload(created_region_id)
        self.headers.update({'Authorization': 'Bearer ' + CHIEF_OFFICER_JWT})
        res = self.client().post('/services', json=test_payload,
                                 headers=self.headers)
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['created'])
        created_service_id = data['created']

    '''
    Read a Service or all services - Everyone can
    '''
    def test_read_a_service(self):

        # Create a new region by chief officer
        test_region_payload = generate_region_payload()
        self.headers.update({'Authorization': 'Bearer ' + CHIEF_OFFICER_JWT})
        res = self.client().post(
            '/regions',
            json=test_region_payload,
            headers=self.headers)
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['created'])
        created_region_id = data['created']

        # Create a new service by Services Manager
        test_payload = generate_service_payload(created_region_id)
        self.headers.update(
            {'Authorization': 'Bearer ' + SERVICES_MANAGER_JWT})
        res = self.client().post('/services', json=test_payload,
                                 headers=self.headers)
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['created'])
        created_service_id = data['created']

        # Read a service
        res = self.client().get('/services/' + str(created_service_id))
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['service'])

        # Read all services
        res = self.client().get('/services')
        self.assertEqual(res.status_code, 200)

    '''
    Update a Service - Only Service Manager and Chief Officer Can
    '''
    def test_update_a_service(self):
        # Create a new region by chief officer
        test_region_payload = generate_region_payload()
        self.headers.update({'Authorization': 'Bearer ' + CHIEF_OFFICER_JWT})
        res = self.client().post(
            '/regions',
            json=test_region_payload,
            headers=self.headers)
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['created'])
        created_region_id = data['created']

        # Create a new service by Services Manager
        test_payload = generate_service_payload(created_region_id)
        self.headers.update(
            {'Authorization': 'Bearer ' + SERVICES_MANAGER_JWT})
        res = self.client().post('/services', json=test_payload,
                                 headers=self.headers)
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['created'])
        created_service_id = data['created']

        # UPDATE A SERVICE BY CHIEF OFFICER
        test_update_service_payload = {
            "address": "Test Address",
            "phone": "+91-1112223344"
        }
        self.headers.update({'Authorization': 'Bearer ' + CHIEF_OFFICER_JWT})
        res = self.client().patch(
            '/services/' + str(created_service_id),
            json=test_update_service_payload,
            headers=self.headers)
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['updated'])

        # UPDATE A SERVICE BY SERVICES MANAGER
        self.headers.update(
            {'Authorization': 'Bearer ' + SERVICES_MANAGER_JWT})
        res = self.client().patch('/services/' + str(created_service_id),
                                  json=test_update_service_payload,
                                  headers=self.headers)
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['updated'])

        # UPDATE A SERVICE BY PUBLIC - Not allowed
        res = self.client().patch(
            '/services/' + str(created_service_id),
            json=test_update_service_payload)
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 401)

    '''
     Delete a Service - Only Service Manager and Chief Officer Can
     '''
    def test_delete_a_service(self):
        # Create a new region by chief officer
        test_region_payload = generate_region_payload()
        self.headers.update({'Authorization': 'Bearer ' + CHIEF_OFFICER_JWT})
        res = self.client().post(
            '/regions',
            json=test_region_payload,
            headers=self.headers)
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['created'])
        created_region_id = data['created']

        # Create a new service by Services Manager
        test_payload = generate_service_payload(created_region_id)
        self.headers.update(
            {'Authorization': 'Bearer ' + SERVICES_MANAGER_JWT})
        res = self.client().post('/services', json=test_payload,
                                 headers=self.headers)
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['created'])
        created_service_id = data['created']

        # DELETE A SERVICE
        self.headers.update(
            {'Authorization': 'Bearer ' + SERVICES_MANAGER_JWT})
        res = self.client().delete(
            '/services/' + str(created_service_id),
            headers=self.headers)
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['deleted'])

        # Create a new service again by Services Manager
        test_payload = generate_service_payload(created_region_id)
        self.headers.update(
            {'Authorization': 'Bearer ' + SERVICES_MANAGER_JWT})
        res = self.client().post('/services', json=test_payload,
                                 headers=self.headers)
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['created'])
        created_service_id = data['created']

        # DELETE A PARENT REGION - Cascade delete region and its services -
        # Only by Chief Officer
        self.headers.update({'Authorization': 'Bearer ' + CHIEF_OFFICER_JWT})
        res = self.client().delete(
            '/regions/' + str(created_region_id),
            headers=self.headers)
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['deleted'])

    '''
     Get a non-existing Service
     '''
    def test_read_non_existing_service(self):
        res = self.client().get('/services/99999')
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 404)

    '''
     Get a non-existing Region
     '''
    def test_read_non_existing_region(self):
        res = self.client().get('/regions/99999')
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 404)


# Make the tests conveniently executable
if __name__ == "__main__":
    unittest.main()
