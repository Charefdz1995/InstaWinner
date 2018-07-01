from django.urls import path
from . import views

urlpatterns = [
    path('',views.main,name='Main'),
    path('followers',views.followers , name = "Followers"),
    path('likers',views.likers,name="Likers"),
    path('get_likers',views.populate_likers,name ="GetLikers")
]
