from rest_framework import routers

from restapi_tutorial.views import BookViewSet, AuthorViewSet

router = routers.DefaultRouter()

router.register(r'books', viewset=BookViewSet)
router.register(r'authors', viewset=AuthorViewSet)