from django.db import models
from django.contrib.auth.models import AbstractUser
import datetime

# Create your models here.
GENDER_CHOICES= (('여성', '여성'), ('남성', '남성'), ('기타', '기타'))
class User(AbstractUser):
    userId = models.CharField(verbose_name="아이디", max_length=30)
    name = models.CharField(verbose_name="이름", max_length=20)
    password = models.CharField(verbose_name="패스워드", max_length=20)
    email = models.CharField(verbose_name="이메일",max_length=50)
    nickName = models.CharField(verbose_name="닉네임", max_length=30)
    gender = models.CharField(verbose_name="성별", max_length=10, choices=GENDER_CHOICES)
    birth = models.DateField(verbose_name="출생년도", null=True)
    userImg = models.ImageField(upload_to="userImg", null=True, blank=True)
    
    def __str__(self):
        return self.userId

class Artist(models.Model):
    name = models.CharField(verbose_name="가수", max_length=20)
    birth = models.DateField(verbose_name="출생년도")
    
    def __str__(self):
        return self.name

class Music(models.Model):
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE, verbose_name="artistId")
    title = models.CharField(verbose_name="제목", max_length=50)
    albumTitle = models.CharField(verbose_name="앨범 이름", max_length=50)
    releasedDate = models.DateField(verbose_name="출시일")
    lyric = models.TextField(verbose_name="가사")
    albumImg = models.ImageField(upload_to="albumImg", null=True, blank=True)
    
    def __str__(self):
        return self.title


class Certification(models.Model):
    createdDate = models.DateField(verbose_name="인증 날짜", default=datetime.date.today)
    userId = models.ForeignKey(User, on_delete=models.CASCADE,verbose_name="유저 id")
    musicId = models.ForeignKey(Music, on_delete=models.CASCADE, verbose_name="music id")
    
    def __int__(self):
        return self.createdDate
    
    def year(self):
        return self.createdDate.strftime('%Y')
    
class Community(models.Model):
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE, verbose_name="artist id", null=True)
    communityName = models.CharField(verbose_name="커뮤니티 이름", max_length=50)
    createdDate = models.DateField(verbose_name="커뮤니티 생성일")
    userId = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="유저 id")
    musicId = models.ForeignKey(Music, on_delete=models.CASCADE, verbose_name="music id")
    
    def __str__(self):
        return self.communityName