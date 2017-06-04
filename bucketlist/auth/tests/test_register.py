from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from bucketlist.auth.models import Account
from bucketlist import db


class AccountTests(APITestCase):

    def setUp(self):
        db.create_all()

    def test_create_account(self):
        """
        Ensure we can create a new account object.
        """
        url = reverse('account')
        data = {
            'username': 'Evans',
            'password': '1245gacheru!',
            'email': 'evans.gacheru@andela.com'
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Account.objects.count(), 1)
        self.assertEqual(Account.objects.get().name, 'Evans')

    def test_create_existing_account(self):
        """
        Tests whether an same account can be created again.
        """
        user = Account(
            username='Evans',
            password='1234gaheru!',
            email='evans.gacheru@andela.com'
        )

        db.session.add(user)
        db.ession.commit()

        url = reverse('register')
        data = {
            'username': 'Evans',
            'password': '1245gacheru!',
            'email': 'evans.gacheru@andela.com'
        }

        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn("User already exists", data['message'])

    def test_create_account_with_short_password(self):
        """
        Tests whether new account being created has a short password
        """
        url = reverse('register')
        data = {
            'username': 'tryzeks',
            'password': '124',
            'email': 'tryzeks@tryzeks.com'
        }

        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn("Password should be more than 3 characters",
                      data["message"])

    def test_incomplete_account_details(self):
        """
        Tests whethere the account details are all filled
        """
        url = reverse('register')
        data = {'username': 'Evans'}

        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn("Provide a username, password and email",
                      data["message"])

    def tearDown(self):
        db.session.close_all()
        db.drop_all()
