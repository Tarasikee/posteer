from django.contrib.auth import views as auth_view
from django.urls import path

from . import views

urlpatterns = [
    path('sign_up/', views.sign_up, name='users-sign-up'),
    path('profile/', views.profile, name='users-profile'),
    path('', views.login, name='users-login'),
    path('logout/', auth_view.LogoutView.as_view(template_name='users/logout.html'), name='users-logout'),
]
