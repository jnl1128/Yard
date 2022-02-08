from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
GENDER_CHOICES = (('여성', '여성'), ('남성', '남성'))

class User(AbstractUser):
  userId = models.CharField(verbose_name = '아이디', max_length=30)
  name = models.CharField(verbose_name = '이름', max_length=20)
  password = models.CharField(verbose_name = "패스워드", max_length=20)
  email = models.CharField(verbose_name='이메일', max_length=50)
  nickName = models.CharField(verbose_name='닉네임', max_length=30)
  gender = models.CharField(verbose_name='성별', max_length=10, choices=GENDER_CHOICES)
  age = models.IntegerField(verbose_name='나이', null=True)
  imageUrl = models.ImageField(upload_to="user_image", null=True, blank=True)

class Music(models.Model):
  artist = models.CharField(verbose_name='가수', max_length=20)
  title = models.CharField(verbose_name='제목', max_length=50)
  albumTitle = models.CharField(verbose_name='앨범 이름', max_length = 50)
  releaseDate = models.DateField(verbose_name='출시일')
  lyrics = models.TextField(verbose_name='가사')
  albumCoverUrl = models.ImageField(upload_to ='album_image', null=True, blank=True)

class Certificate(models.Model):
  createdDate = models.DateField(verbose_name='인증 날짜')
  userId = models.ForeignKey(User, on_delete=models.CASCADE,  verbose_name="유저 아이디")
  musicId = models.ForeignKey(Music, on_delete=models.CASCADE,  verbose_name="음악 아이디")

  def year(self):
    return self.createdDate.strftime('%Y')

class Community(models.Model):
  communityName = models.CharField(verbose_name='커뮤니티 이름', max_length=70)
  createdDate = models.DateField(verbose_name='커뮤니티 생성일')
  userId = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="유저 아이디")
  musicId = models.ForeignKey(Music, on_delete=models.CASCADE,  verbose_name='음악 아이디')



  