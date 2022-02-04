from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.
GENDER_CHOICES= (('여성', '여성'), ('남성', '남성'))
class User(AbstractUser):
    user_id = models.CharField(verbose_name="아이디", max_length=30)
    name = models.CharField(verbose_name="이름", max_length=20)
    password = models.CharField(verbose_name="패스워드", max_length=20)
    email = models.CharField(verbose_name="이메일",max_length=50)
    nickName = models.CharField(verbose_name="닉네임", max_length=30)
    gender = models.CharField(verbose_name="성별", max_length=10, choices=GENDER_CHOICES)
    age = models.IntegerField(verbose_name="나이")
    imageUrl = models.ImageField(upload_to="user_image", null=True, blank=True)
    
class Music(models.Model):
    artist = models.CharField(verbose_name="가수", max_length=20)
    title = models.CharField(verbose_name="제목", max_length=50)
    albumTitle = models.CharField(verbose_name="앨범 이름", max_length=50)
    releasedDate = models.DateField(verbose_name="출시일")
    lyric = models.TextField(verbose_name="가사")
    albumCoverUrl = models.ImageField(upload_to="album_image", null=True, blank=True)    


class Certification(models.Model):
    createdDate = models.DateField(verbose_name="인증 날짜")
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, related_name="user", verbose_name="유저 id")
    music_id = models.ForeignKey(Music, on_delete=models.CASCADE, related_name="music", verbose_name="music id")
    
class Community(models.Model):
    communityName = models.CharField(verbose_name="커뮤니티 이름", max_length=50)
    createdDate = models.DateTimeField(verbose_name="커뮤니티 생성일")
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, related_name="user", verbose_name="유저 id")
    music_id = models.ForeignKey(Music, on_delete=models.CASCADE, related_name="music", verbose_name="music id")