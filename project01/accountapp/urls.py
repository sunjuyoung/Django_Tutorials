from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path

from accountapp.views import hello_world, AccountCreateView

app_name = 'accountapp'
# 127.0.0.1/accountapp/hello_world -> accountapp:hello_world

urlpatterns = [
    path('login/', LoginView.as_view(template_name='accountapp/login.html'), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),

    path('hello_world/',hello_world, name='hello_world'),
    path('create/',AccountCreateView.as_view(), name='create'),

]