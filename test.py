import unittest
import os
import sys
from myproject import create_app


class FlaskTest(unittest.TestCase):

    # Ensure welcome page loads
    def test_home_status(self):
        tester = create_app().test_client()
        response = tester.get('/',content_type='html/text')
        self.assertEqual(response.status_code,200)


    # Ensure welcome page loads with correct information
    def test_home_data(self):
        tester = create_app().test_client()
        response = tester.get('/',content_type='html/text')
        self.assertTrue(b"Hello! Welcome to the site" in response.data)

    # Ensure login page loads
    def test_login_status(self):
        tester = create_app().test_client()
        response = tester.get('/login',content_type='html/text')
        self.assertEqual(response.status_code,200)

    # Ensure login page loads with correct information
    def test_login_data(self):
        tester = create_app().test_client()
        response = tester.get('/login',content_type='html/text')
        self.assertTrue(b"Login" in response.data)

    # Ensure login functionallity works with correct credentials
    def test_valid_login(self):
        tester = create_app().test_client()
        response = tester.post(
            '/login',
            data=dict(email="test@test.com", password="test"),
            follow_redirects=True
        )
        self.assertIn(b'Welcome, Collin', response.data)

    # Ensure login functionallity doesnt work with incorrect credentials
    def test_invalid_login(self):
        tester = create_app().test_client()
        response = tester.post(
            '/login',
            data=dict(email="wrong@test", password="test"),
            follow_redirects=True
        )
        self.assertIn(b'Please check your login details and try again.', response.data)



if __name__ == '__main__':
    unittest.main()
