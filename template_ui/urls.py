from django.urls import path
from .views import crud

urlpatterns = [
    path('', crud, name='crud_uri')
]

