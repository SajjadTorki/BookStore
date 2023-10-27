from django.urls import path
from .views import SignupView, home_view

urlpatterns = [

    path("signup", SignupView.as_view(), name='signup'),
    path("", home_view, name='home'),

]
