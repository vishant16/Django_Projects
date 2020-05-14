
from django.contrib import admin
from django.urls import path
from signinup.views import Login,Register

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/',Login),
    path('register/',Register)
]
