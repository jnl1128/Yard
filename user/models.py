from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager
import datetime

# Create your models here.
class UserManager(BaseUserManager):
    def create_user(self, email, password, **extra_fields):
        if not email:
            raise ValueError('Enter an email address')

        email = self.normalize_email(email)

        user = self.model(
            email=email,
            password=password,
            **extra_fields
        )
        user.set_password(password)
        user.save(using=self._db)

        return user
    
    def create_superuser(self, email, password):       
        user = self.create_user(            
            email,
            password=password,
        )
        user.is_admin = True
        user.is_superuser = True        
        user.is_staff = True
        user.save(using=self._db)

        return user


GENDER_CHOICES= (('여성', '여성'), ('남성', '남성'), ('기타', '기타'))
class User(AbstractUser):
    email = models.EmailField(verbose_name="이메일 주소")
    nickName = models.CharField(verbose_name="닉네임", max_length=30)
    password = models.CharField(verbose_name="패스워드", max_length=128)
    gender = models.CharField(verbose_name="성별", max_length=10, choices=GENDER_CHOICES)
    birth = models.DateField(verbose_name="출생년도", null=True)
    userImg = models.ImageField(upload_to="userImg", null=True, blank=True)
    first_name = None
    last_name = None

    
    REQUIRED_FIELDS = ['username']
    USERNAME_FIELD = 'email'

    def __str__(self):
        return self.email

class Artist(models.Model):
    name = models.CharField(verbose_name="가수", max_length=20)
    birth = models.DateField(verbose_name="출생년도", null=True, blank=True)
    
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
    
    def __str__(self):
        return self.musicId.title
    
    def year(self):
        return self.createdDate.strftime('%Y')

class HashTag(models.Model):
    name = models.CharField(verbose_name="해쉬태그 종류", max_length=20)
    
    def __str__(self):
        return self.name
   
class Feed(models.Model):
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE, verbose_name="artist id", null=True)
    feedName = models.CharField(verbose_name="피드 이름", max_length=50)
    createdDate = models.DateField(verbose_name="피드 생성일")
    userId = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="유저 id")
    musicId = models.ForeignKey(Music, on_delete=models.CASCADE, verbose_name="music id")
    tags = models.ManyToManyField('HashTag', blank=True)
    content = models.TextField(verbose_name="피드 내용", blank=True, null=True)
    
    def __str__(self):
        return self.feedName