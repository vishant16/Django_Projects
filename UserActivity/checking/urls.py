from django.urls import path,include
from .views import UserDetailsList

#router.register('viewset',HelloViewSet,base_name='viewset')

urlpatterns = [
    path('check/', UserDetailsList.as_view()),]