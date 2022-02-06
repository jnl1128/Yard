from django.urls import path
from . import views

app_name = "user"

urlpatterns = [
	path('<int:pk>/', views.musicDetail, name='musicDetail'),
]