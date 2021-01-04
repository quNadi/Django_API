from django.urls import include,path
from django.conf.urls import url

#alternatywnie urls.py

from rest_framework.routers import SimpleRouter

from .viewset import UserViewSet, PostViewSet

router=SimpleRouter()
router.register('users',UserViewSet,basename='users')
router.register('dataset',PostViewSet,basename='dataset')

urlpatterns=router.urls