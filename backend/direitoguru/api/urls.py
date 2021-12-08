from django.contrib import admin
from django.urls import path
from django.conf.urls import include
from rest_framework import routers
from .views import UserViewSet, api_feed, api_feeds

router = routers.DefaultRouter()
router.register('users', UserViewSet)
# router.register('feed', FeedViewSet)


urlpatterns = [
    path('', include(router.urls)),
    path('feed/', api_feeds),
    path('feed/<int:feed_id>', api_feed),
]