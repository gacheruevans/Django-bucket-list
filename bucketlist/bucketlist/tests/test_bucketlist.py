import datetime
import json

from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from bucketlist import db


class Test_bucketlist(APITestCase):

    def setUp(cls):
        db.create_all()
        cls.client.post(
            url=reverse('register'),
            data=json.dumps(
                {
                    'username': 'Evans',
                    'password': '1245gacheru!',
                    'email': 'evans.gacheru@andela.com'})
        )
        response = cls.client.post(
            url=reverse('login'),
            data=json.dumps({
                'username': 'Evans',
                'password': '1245gacheru!'}),
        )
        data = json.loads(response.get_data(as_text=True))

        cls.token = {'Authorization': data['token']}

    def test_create_new_bucketlist(self):
        response = self.client.post(
            url=reverse('bucketlist'),
            data=json.dumps(
                {
                    'name': 'Adventure',
                    'date_created': str(datetime.datetime.now())}),
            headers=self.token)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        data = json.loads(response.get_data(as_text=True))
        self.assertIn("created bucketlist successfully",
                      data['message'])

    def test_view_all_bucketlists(self):
        self.client.post(
            url=reverse('bucketlist'),
            data=json.dumps({
                'name': 'test_bucketlist',
                'date_created': str(datetime.datetime.now())
            }),
            headers=self.token)
        response = self.client.get(
            url=reverse('bucketlist'),
            headers=self.token)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        data = json.loads(response.get_data(as_text=True))
        self.assertIsNotNone(data)

    def test_view_a_bucketlists(self):
        self.client.post(
            url=reverse('bucketlist'),
            data=json.dumps({
                'name': 'test_bucketlist',
                'date_created': str(datetime.datetime.now())
            }),
            headers=self.token)
        response = self.client.get(
            url=reverse('onebucketlist', bucketlists_id=1),
            headers=self.token)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        data = json.loads(response.get_data(as_text=True))
        self.assertIsNotNone(data)

    def test_delete_bucketlist(self):
        self.client.post(
            url=reverse('bucketlist'),
            data=json.dumps({
                'name': 'test_bucketlist',
                'date_created': str(datetime.datetime.now())
            }),
            headers=self.token)
        response = self.client.delete(
            url=reverse('onebucketlist', bucketlists_id=1),
            headers=self.token)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        data = json.loads(response.get_data(as_text=True))
        self.assertIsNotNone(data)
        self.assertIn("successfully deleted",
                      data['message'])

        response = self.client.get(
            url=reverse('onebucketlist', bucketlists_id=1),
            headers=self.token)
        self.assert_status(response, status.HTTP_400_BAD_REQUEST)

    def test_search_for_bucketlist(self):
        self.client.post(
            url=reverse('bucketlist'),
            data=json.dumps({
                'name': 'bucketlist1',
                'date_created': str(datetime.datetime.now())
            }),
            headers=self.token)
        response = self.client.get(
            '/api/v1/bucketlists?q=bucketlist',
            headers=self.token)
        self.assert_200(response)
        data = json.loads(response.get_data(as_text=True))
        self.assertIsNotNone(data)

        response = self.client.get(
            '/api/v1/bucketlists?q=none',
            headers=self.token)
        self.assert_status(response, status.HTTP_400_BAD_REQUEST)
        result = json.loads(response.get_data(as_text=True))
        self.assertIsNotNone(result)
        self.assertIn('No bucketlist matching the search param',
                      result['message'])

    def test_edit_bucketlist(self):
        self.client.post(
            url=reverse('bucketlist'),
            data=json.dumps({
                'name': 'test_bucketlist',
                'date_created': str(datetime.datetime.now())
            }),
            headers=self.token)
        response = self.client.put(
            url=reverse('onebucketlist', bucketlists_id=1),
            data=json.dumps({
                'name': 'Travel',
                'date_created': str(datetime.datetime.now())
            }),
            headers=self.token)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_existing_bucketlist(self):
        self.client.post(
            url=reverse('bucketlist'),
            data=json.dumps(
                {
                    'name': 'Adventure'}),
            headers=self.token)

        response = self.client.post(
            url=reverse('bucketlist'),
            data=json.dumps({'name': 'Adventure'}),
            headers=self.token)
        data = json.loads(response.get_data(as_text=True))
        self.assertIn("Bucketlist already exists",
                      data['message'])

    def test_incomplete_detail_on_bucketlist(self):
        response = self.client.post(
            url=reverse('bucketlist'),
            data=json.dumps({'name': ''}),
            headers=self.token)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        data = json.loads(response.get_data(as_text=True))
        self.assertIn("Kindly provide the name",
                      data['message'])

    def tearDown(self):
        db.session.close_all()
        db.drop_all()
