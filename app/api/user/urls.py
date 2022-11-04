from django.urls import path

from api.user import views

urlpatterns = [
    path('', views.home, name="home"),
]