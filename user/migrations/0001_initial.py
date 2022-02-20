# Generated by Django 3.2.12 on 2022-02-19 14:08

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import user.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('email', models.EmailField(max_length=254, unique=True, verbose_name='이메일 주소')),
                ('nickName', models.CharField(max_length=30, verbose_name='닉네임')),
                ('password', models.CharField(max_length=128, verbose_name='패스워드')),
                ('gender', models.CharField(choices=[('여성', '여성'), ('남성', '남성'), ('기타', '기타')], max_length=10, verbose_name='성별')),
                ('birth', models.DateField(null=True, verbose_name='출생년도')),
                ('userImg', models.ImageField(blank=True, null=True, upload_to='userImg')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            managers=[
                ('objects', user.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='HashTag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, verbose_name='해쉬태그 종류')),
            ],
        ),
        migrations.CreateModel(
            name='Feed',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('music', models.CharField(max_length=100, verbose_name='피드 음악')),
                ('artist', models.CharField(max_length=100, verbose_name='피드 가수')),
                ('createdDate', models.DateTimeField(auto_now_add=True, verbose_name='피드 생성일')),
                ('content', models.TextField(blank=True, null=True, verbose_name='피드 내용')),
                ('feedImg', models.ImageField(blank=True, null=True, upload_to='feedImg')),
                ('like_users', models.ManyToManyField(blank=True, related_name='like_feeds', to=settings.AUTH_USER_MODEL)),
                ('tags', models.ManyToManyField(blank=True, to='user.HashTag')),
                ('userId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='유저 id')),
            ],
        ),
        migrations.CreateModel(
            name='Certification',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('createdDate', models.DateField(default=datetime.date.today, verbose_name='인증 날짜')),
                ('music', models.CharField(max_length=100, verbose_name='인증서 음악')),
                ('artist', models.CharField(max_length=100, verbose_name='인증서 가수')),
                ('albumImg', models.ImageField(blank=True, null=True, upload_to='albumImg')),
                ('userId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='유저 id')),
            ],
        ),
    ]
