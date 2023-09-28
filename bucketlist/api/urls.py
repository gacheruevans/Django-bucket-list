from django.urls import path
from .views import UserView, CreateBucketListView, BucketListView

urlpatterns = [
    path('bucketlist/', CreateBucketListView.as_view()),
    path('bucketlist/', BucketListView.as_view()),
    path('user/', UserView.as_view())
]
