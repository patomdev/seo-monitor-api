import unittest
from app import create_app
from utils import load
from expecter import expect

class ApiRootTestCase(unittest.TestCase):
    def setUp(self):
        self.app = create_app('testing')
        self.app_context = self.app.app_context()
        self.app_context.push()
        self.client = self.app.test_client()

    def tearDown(self):
        self.app_context.pop()

    def test_endpoint_status(self):
        status, data = load(self.client.get('/api',
                                   content_type='application/json'))
        expect(status == 200)

    def test_endpoint_response(self):
        status, data = load(self.client.get('/api',
                                   content_type='application/json'))
        expect(status) == 200
        expect(data == {
           'sites': 'http://localhost:5000/v1/sites/',
           'version': 'v1'
        })

    def test_ping_response(self):
        status, data = load(self.client.get('/ping',
                                   content_type='application/json'))
        expect(data == {'msg': 'ok'})
