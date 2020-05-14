from django.urls import path,include
from .views import Userlist


urlpatterns = [
    path('user_activity/', Userlist.as_view()),
    ]
