from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path

urlpatterns=[
    path(
        'login/', 
        LoginView.as_view(template_name='users/login.html'),
        name='user_login'
    ),
    path( 'logout/', LogoutView.as_view(), name='user_logout'),
]