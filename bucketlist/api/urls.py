from django.urls import path
from .views import UserView, BucketListView

urlpatterns = [
    path('bucketlist/', BucketListView.as_view()),
    # path('bucketlist/Item', ProductView.as_view()),
    path('user/', UserView.as_view())
]
