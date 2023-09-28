from django.test import TestCase
from .models import User, Bucketlist, Item


class UserTest(TestCase):
    def test_user_model_exist(self):
        """ Test if the user model exists """

        user = User.objects.count()
        self.assertEqual(user, 0)

    def test_user_creation(self):
        """ Tests for creating a new user and saving it to database."""
        user = User.objects.create(
            username='testuser',
            email='testuser@test.com',
            password='123456'
        )

        self.assertEqual(str(user), user.username)


class BucketlistTest(TestCase):

    def setUp(self):
        self.user = User.objects.create(
            username='testuser',
            email='testuser@test.com',
            password="123456"
        )

    def test_bucket_list_model_exist(self):
        """Test bucket list model exists"""

        bucketlist = Bucketlist.objects.count()
        self.assertEqual(bucketlist, 0)

    def test_bucket_list_creation(self):
        """ Test that a new bucket is created successfully."""

        bucketlist = Bucketlist.objects.create(
            title='Go to the Maldives',
            created_by=User.objects.get(id=self.user.id)
        )

        self.assertEqual(str(bucketlist), bucketlist.title)


class BucketlistPageTest(TestCase):
    def setUp(self):
        self.user = User.objects.create(
            username='testuser',
            email='testuser@test.com',
            password="123456"
        )

        self.bucketlist = Bucketlist.objects.create(
            title='Go to Israel',
            created_by=User.objects.get(id=self.user.id)
        )

    def test_bucket_list_page_returns_correct_response(self):

        response = self.client.get('/bucketlist')

        self.assertTemplateUsed(
            response, 'templates/frontend/index.html')
        self.assertEqual(response.status_code, 200)

    def test_bucket_list_page_returns_data(self):
        """Tests whether or not the bucket list page has any data in it to display on screen"""

        response = self.client.get('/bucketlist')

        self.assertContains(response, self.bucketlist.title)
        self.assertEqual(response.status_code, 200)
