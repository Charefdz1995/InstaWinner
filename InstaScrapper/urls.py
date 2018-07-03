from django.urls import path
from . import views

urlpatterns = [
    path('',views.main,name='Main'),
    path('followers',views.followers , name = "Followers"),
    path('get_followers',views.populate_followers,name="GetFollowers"),
    path('likers',views.likers,name="Likers"),
    path('get_likers',views.populate_likers,name ="GetLikers"),
    path('settings',views.settings,name = "Settings"),
    path('login',views.login_settings,name = "Login"),
    path('code',views.code,name = "Code"),
    path('log',views.log_in, name = "Login"),
    path('home',views.home,name='Home')
]
