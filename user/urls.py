from django.urls import path
from . import views

app_name = "user"

urlpatterns = [
	path('', views.mainSearch, name="main"),
	path('<int:pk>/', views.certDetail, name='certDetail'),
]