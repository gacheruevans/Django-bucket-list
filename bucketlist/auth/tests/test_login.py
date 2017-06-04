import json

from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from bucketlist.auth.models import Account
from bucketlist import db


class LoginTestCase(APITestCase):

    def setUp(self):
        """
        Creates a record for testing purposes
        """
        db.create_all()
        user = Account(
            username='Evans',
            password='1245gacheru!',
            email='evans.gacheru@andela.com'
        )
        db.session.add(user)
        db.session.commit()

    def test_login_endpoint(self):
        """
        Instructive fuction that guides the users on how to login
        """
        url = reverse('login')
        response = self.client.get(url)
        data = json.loads(response.get_data(as_text=True))
        self.assert_status(response.status_code, status.HTTP_200_OK)
        self.assertIn('Login by sending a POST request to /login',
                      data['message'])

    def test_login_with_right_credentials(self):
        url = reverse('login')
        response = self.client.post(
            url,
            data=json.dumps(
                {
                    'username': 'Evans',
                    'password': '1245gacheru!'
                })
        )
        data = json.loads(response.get_data(as_text=True))
        self.assertIn("token", data.keys)

    def test_login_with_non_existing_user(self):
        """
        Tests whether a non existent user can login.
        """
        url = reverse('login')
        response = self.client.post(
            url,
            data=json.dumps(
                {
                    'username': 'Ann',
                    'password': 'm0nty'
                })
        )
        self.assert_status(response, status.HTTP_400_BAD_REQUEST)
        data = json.loads(response.get_data(as_text=True))
        self.assertIn("User does not exist", data['message'])

    def test_login_with_incomplete_credentials(self):
        """
        Tests whether a user can login without filling in the desired credentials.
        """
        url = reverse('login')
        response = self.client.post(
            url,
            data=json.dumps(
                {
                    'username': '',
                    'password': ''
                })
        )
        self.assert_assert(response, status.HTTP_401_UNAUTHORIZED)
        data = json.loads(response.get_data(as_text=True))
        self.assertEqual(
            "Kindly fill in your username and password", data['message'])

    def tearDown(self):
        db.session.close_all()
        db.drop_all()
