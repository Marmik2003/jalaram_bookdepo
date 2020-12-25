from django.urls import path
from . import views


urlpatterns = [
    path('',views.index_view, name='index'),
    path('public/home',views.public_home, name='home'),
    path('public/login',views.public_login, name='login'),
    path('logout_request', views.logout_view, name='logout')
]