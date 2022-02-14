from user import views
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

app_name = 'user'
urlpatterns = [
  path('', view=views.mainSearch, name="main"),
  path('mypage/', view=views.myPage, name="myPage"),
  path('myInfo/', view=views.myInfo, name="myInfo"),
  path('register/', views.certificationRegister, name='certificationRegister'),
  path('register/musicsearch/', views.musicSearch, name='musicSearch'),
  path('register/addMusicAjax/', views.addMusicAjax, name='addMusicAjax'),
  path('search/',views.searchResult, name='search'),
  path('createFeed/', views.createFeed, name="createFeed"),
  path('createFeed/addMusicAjax/', views.addMusicAjax, name='addMusicAjax'),
  path('feed/<int:pk>/', views.feedDetail, name="feedDetail"),
  path('mypage/<int:pk>/', views.certDetail, name='certDetail'),
  path('mypage/<int:pk>/update/', views.certUpdate, name='certUpdate'),
  path('mypage/<int:pk>/delete/', views.certDelete, name='certDelete'),
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)