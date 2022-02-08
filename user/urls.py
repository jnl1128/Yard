from user import views
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

app_name = 'user'
urlpatterns = [
  path('', view=views.main, name = "main"),
  path('mypage/', view=views.myPage, name="myPage"),
  path('register/', views.musicRegister, name='musicRegister'),
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
