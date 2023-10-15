from django.urls import path
from .views import *

urlpatterns = [

    path('', HomePageViwe.as_view(), name='home'),
]
