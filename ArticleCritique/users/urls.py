from django.urls import path
from .views import login_page, sign_up, logout_user, test

urlpatterns = [
    path('', login_page, name='login'),
    path('signup', sign_up, name='sign-up'),
    path('logout', logout_user, name='logout'),
    path('test', test, name='test'),
]
