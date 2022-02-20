from email.policy import default
from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager
import datetime

# Create your models here.
class UserManager(BaseUserManager):
    """Define a model manager for User model with no username field."""

    use_in_migrations = True

    def _create_user(self, email, password, **extra_fields):
        """Create and save a User with the given email and password."""
        if not email:
            raise ValueError('The given email must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password=None, **extra_fields):
        """Create and save a regular User with the given email and password."""
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password, **extra_fields):
        """Create and save a SuperUser with the given email and password."""
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self._create_user(email, password, **extra_fields)


GENDER_CHOICES= (('여성', '여성'), ('남성', '남성'), ('기타', '기타'))
class User(AbstractUser):
    """User model."""

    username = None
    email = models.EmailField(verbose_name="이메일 주소", unique=True)
    nickName = models.CharField(verbose_name="닉네임", max_length=7)
    password = models.CharField(verbose_name="패스워드", max_length=128)
    gender = models.CharField(verbose_name="성별", max_length=10, choices=GENDER_CHOICES)
    birth = models.DateField(verbose_name="출생년도", null=True)
    userImg = models.ImageField(upload_to="userImg", null=True, blank=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = UserManager()


class Certification(models.Model):
    createdDate = models.DateField(verbose_name="인증 날짜", default=datetime.date.today)
    userId = models.ForeignKey(User, on_delete=models.CASCADE,verbose_name="유저 id")
    music = models.CharField(verbose_name="인증서 음악", max_length=100)
    artist = models.CharField(verbose_name="인증서 가수", max_length=100)
    albumImg = models.ImageField(upload_to="albumImg", null=True, blank=True)
    
    def __str__(self):
        return self.music
    
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
    inputTags = models.CharField(verbose_name="나만의 해시태그를 작성해보세요 ex)#Yar:d 짱 #야드핫플", max_length=50, blank=True ,null=True)
    content = models.TextField(verbose_name="피드 내용", blank=True, null=True)
    feedImg = models.ImageField(upload_to="feedImg", null=True, blank=True)
    like_users = models.ManyToManyField(User, blank=True, related_name='like_feeds')

    def __str__(self):
        return self.music