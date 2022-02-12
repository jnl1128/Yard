from django.db import models
from django.contrib.auth.models import AbstractUser
import datetime

# Create your models here.
GENDER_CHOICES= (('여성', '여성'), ('남성', '남성'), ('기타', '기타'))
class User(AbstractUser):
    email = models.EmailField(('이메일 주소'), unique=True)
    nickName = models.CharField(verbose_name="닉네임", max_length=30)
    password = models.CharField(verbose_name="패스워드", max_length=128)
    gender = models.CharField(verbose_name="성별", max_length=10, choices=GENDER_CHOICES)
    birth = models.DateField(verbose_name="출생년도", null=True)
    userImg = models.ImageField(upload_to="userImg", null=True, blank=True)
    username = None
    first_name = None
    last_name = None

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.email


class Certification(models.Model):
    createdDate = models.DateField(verbose_name="인증 날짜", default=datetime.date.today)
    userId = models.ForeignKey(User, on_delete=models.CASCADE,verbose_name="유저 id")
    music = models.CharField(verbose_name="인증서 음악", max_length=100)
    artist = models.CharField(verbose_name="인증서 가수", max_length=100)
    albumImg = models.ImageField(upload_to="albumImg", null=True, blank=True)
    
    def __str__(self):
        return self.musicId.title
    
    def year(self):
        return self.createdDate.strftime('%Y')

class HashTag(models.Model):
    name = models.CharField(verbose_name="해쉬태그 종류", max_length=20)
    
    def __str__(self):
        return self.name
   
class Feed(models.Model):
    music = models.CharField(verbose_name="피드 음악", max_length=100)
    artist = models.CharField(verbose_name="피드 가수", max_length=100)
    createdDate = models.DateTimeField(verbose_name="피드 생성일",auto_now_add=True)
    userId = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="유저 id")
    tags = models.ManyToManyField('HashTag', blank=True)
    content = models.TextField(verbose_name="피드 내용", blank=True, null=True)
    feedImg = models.ImageField(upload_to="feedImg", null=True, blank=True)
    
    def __str__(self):
        return self.music