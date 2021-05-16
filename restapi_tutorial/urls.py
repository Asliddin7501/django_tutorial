from django.urls import path

from restapi_tutorial.views import BookView

app_name = 'restapi'
urlpatterns = [
    path('book-data/', BookView.as_view(), name='book-data')
]