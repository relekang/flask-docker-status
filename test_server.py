import unittest

import server


class ServerTests(unittest.TestCase):

    def setUp(self):
        self.app = server.app.test_client()

    def test_index_view(self):
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertIn('CONTAINER ID', response.data.decode())
