import datetime
import json

from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from bucketlist.bucketlist.models import Bucketlist, Item
from bucketlist import db


class TestItems(APITestCase):
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

        cls.client.post(
            url=reverse('bucketlist'),
            data=json.dumps(
                {
                    'name': 'Adventure',
                    'date_created': str(datetime.datetime.now())}),
            headers=cls.token)
        cls.bucketlist = Bucketlist.query.filter_by(name="Adventure").first()

    def test_create_new_item(self):
        response = self.client.post(
            url=reverse('items', bucketlists_id=self.bucketlist.id),
            data=json.dumps(
                {
                    'name': 'Ziplining'
                }),
            headers=self.token)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        data = json.loads(response.get_data(as_text=True))
        self.assertIsNotNone(data)
        self.assertIn("created bucketlist item successfully",
                      data['message'])

    def test_view_all_items(self):
        self.client.post(
            url=reverse('items', bucketlists_id=self.bucketlist.id),
            data=json.dumps({
                'name': 'test_item',
                'done': False
            }),
            headers=self.token)
        response = self.client.get(
            url=reverse('items', bucketlists_id=self.bucketlist.id),
            headers=self.token)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        data = json.loads(response.get_data(as_text=True))
        self.assertIsNotNone(data)

    def test_view_an_item(self):
        self.client.post(
            url=reverse('items', bucketlists_id=self.bucketlist.id),
            data=json.dumps({
                'name': 'test_item',
                'done': False,
            }),
            headers=self.token)
        item = Item.query.filter_by(name="test_item").first()
        response = self.client.get(
            url=reverse('oneitem',
                        bucketlists_id=self.bucketlist.id,
                        item_id=item.id),
            headers=self.token)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        data = json.loads(response.get_data(as_text=True))
        self.assertIsNotNone(data)

    def test_delete_item(self):
        self.client.post(
            url=reverse('items', bucketlists_id=self.bucketlist.id),
            data=json.dumps({
                'name': 'test_item',
                'done': False
            }),
            headers=self.token)
        item = Item.query.filter_by(name="test_item").first()
        response = self.client.delete(
            url=reverse('oneitem',
                        bucketlists_id=self.bucketlist.id,
                        item_id=item.id),
            headers=self.token)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        data = json.loads(response.get_data(as_text=True))
        self.assertIsNotNone(data)

        response = self.client.get(
            url=reverse('oneitem',
                        bucketlists_id=self.bucketlist.id,
                        item_id=item.id),
            headers=self.token)
        self.assert_status(response, status.HTTP_400_BAD_REQUEST)

    def test_search_for_item(self):
        self.client.post(
            url=reverse('items', bucketlists_id=self.bucketlist.id),
            data=json.dumps({
                'name': 'item1',
                'done': False,
            }),
            headers=self.token)
        response = self.client.get(
            '/bucketlists/{}/items?q=item'.format(self.bucketlist.id),
            headers=self.token)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        data = json.loads(response.get_data(as_text=True))
        self.assertIsNotNone(data)

        response = self.client.get(
            '/bucketlists/{}/items?q=none'.format(self.bucketlist.id),
            headers=self.token)
        self.assert_status(response, status.HTTP_400_BAD_REQUEST)
        result = json.loads(response.get_data(as_text=True))
        self.assertIn('No item matching the search param',
                      result['message'])

    def test_edit_item(self):
        self.client.post(
            url=reverse('items', bucketlists_id=self.bucketlist.id),
            data=json.dumps({
                'name': 'test_item',
                'done': False
            }),
            headers=self.token)
        item = Item.query.filter_by(name="test_item").first()
        response = self.client.put(
            url=reverse('oneitem',
                        bucketlists_id=self.bucketlist.id,
                        item_id=item.id),
            data=json.dumps({
                'name': 'Bangee jumping',
                'done': False
            }),
            headers=self.token)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        data = json.loads(response.get_data(as_text=True))
        self.assertIsNotNone(data)

    def test_create_existing_item(self):
        item = Item(
            name='Ziplining')

        db.session.add(item)
        db.session.commit()
        response = self.client.post(
            url=reverse('items', bucketlists_id=self.bucketlist.id),
            data=json.dumps(
                {
                    'name': 'Ziplining'
                }),
            headers=self.token)
        data = json.loads(response.get_data(as_text=True))
        self.assertIn("Item already exists",
                      data['message'])

    def test_incomplete_detail_on_item(self):
        response = self.client.post(
            url=reverse('items', bucketlists_id=self.bucketlist.id),
            data=json.dumps({'name': ''}),
            headers=self.token)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        data = json.loads(response.get_data(as_text=True))
        self.assertIn("provide the name",
                      data['message'])

    def tearDown(self):
        db.session.close_all()
        db.drop_all()
