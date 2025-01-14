import unittest
from my_app.app import app

class TestApp(unittest.TestCase):
    def test_index(self):
        client = app.test_client()
        response = client.get('/')
        self.assertEqual(response.status_code, 200)

if __name__ == '__main__':
    unittest.main()
