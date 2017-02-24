import unittest
import json
from flask import current_app, url_for
from app import create_app


class ApiPingTestCase(unittest.TestCase):
    def setUp(self):
        self.app = create_app('testing')
        self.app_context = self.app.app_context()
        self.app_context.push()
        self.client = self.app.test_client()

    def tearDown(self):
        self.app_context.pop()

    def test_endpoint_status(self):
        response = self.client.get('/api/sitemap/123',
                                   content_type='application/json')
        self.assertTrue(response.status_code == 200)

    def test_endpoint_response(self):
        response = self.client.get('/api/sitemap/123',
                                   content_type='application/json')
        json_response = json.loads(response.data.decode('utf-8'))
        self.assertTrue(json_response['id'] == 123)

    def test_app_is_testing(self):
        self.assertTrue(current_app.config['TESTING'])
