from django.urls import path,include
from rest_framework.routers import DefaultRouter

from .views import HelloViewSet,HelloApiView,UserProfileViewset,UserLoginApiView,UserProfileFeedViewSet


router=DefaultRouter()
router.register('hello_viewset',HelloViewSet,base_name='hello_viewset')
router.register('profile',UserProfileViewset)
router.register('feed',UserProfileFeedViewSet)

urlpatterns = [
    path('hello_view/',HelloApiView.as_view()),
    path('login/',UserLoginApiView.as_view()),
    path('',include(router.urls))

]
