from django.urls import path
from . import views


app_name='user'

urlpatterns = [
    path('', views.mainSearch, name="main"),
    path('search/',views.searchResult, name='search'),
    path('createCommunity/', views.createCommunity, name="createCommunity"),
]