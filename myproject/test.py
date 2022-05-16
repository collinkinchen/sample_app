import unittest
import os
import sys
from __init__ import create_app


class FlaskTest(unittest.TestCase):


    def test_index(self):
        tester = create_app().test_client()
        response = tester.get('/login',content_type='html/text')
        self.assertEqual(response.status_code,200)


if __name__ == '__main__':
    unittest.main()
