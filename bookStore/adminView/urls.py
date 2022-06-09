from django.urls import path
from . import views

urlpatterns = [
    path('home',views.Home),
    path('newUser',views.NewUser.as_view())


]
