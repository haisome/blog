from django.contrib.auth.models import AbstractUser
from django.db import models
from utils.default_model import random_nick_name
from blog.models import Article

__all__ = [
    'UserProfile',
    'MideaUserProfile',
    'MideaUserGroup',
    'EffCard',
    'EmailVerifyCode',
    'Message',
    'Comment',
    'Reply'
]


# Create your models here.

class UserProfile(AbstractUser):
    gender_choices = (
        ('male', '男'),
        ('female', '女'),
        ('unknown', '未知')
    )
    nick_name = models.CharField(max_length=100, default=random_nick_name)
    gender = models.CharField(choices=gender_choices, default='unknown', max_length=20)
    image = models.ImageField(upload_to='avatar/%Y/%m', max_length=100, default='avatar/avatar.png')
    midea_user = models.CharField(max_length=100,default='default')
    midea_password = models.CharField(max_length=100,default='default')
    midea_authenticated = models.CharField(max_length=100,default=False)
    midea_ssotoken = models.CharField(max_length=100,default=False)
    midea_cardnum = models.CharField(max_length=100,default=False)

class MideaUserProfile(models.Model):
    groupid = models.CharField(max_length=100, default='default')
    jid = models.CharField(max_length=100,default='default',unique= True)
    name = models.CharField(max_length=100,default='default')
    sex = models.CharField(max_length=100,default='default')
    email = models.CharField(max_length=100,default='default')
    position = models.CharField(max_length=100,default='default')
    number = models.CharField(max_length=100,default='default')
    py = models.CharField(max_length=100,default='default')
    pyinitials = models.CharField(max_length=100,default='default')
class MideaUserGroup(models.Model):
    parentid = models.CharField(max_length=100, default='default')
    groupid = models.CharField(max_length=100,default='default',unique =True)
    weight = models.CharField(max_length=100,default='default')
    title = models.CharField(max_length=100,default='default')
class EffCard(models.Model):
    oid = models.CharField(max_length=100, default='default',unique =True)
    cardName = models.CharField(max_length=100,default='default')

class EmailVerifyCode(models.Model):
    code = models.CharField(max_length=20, unique=True)
    email = models.EmailField(max_length=50)
    send_time = models.DateTimeField(auto_now_add=True)


class Message(models.Model):
    add_time = models.DateTimeField(auto_now_add=True)
    body = models.CharField(max_length=200)
    status = models.BooleanField(default=False)


class Comment(models.Model):
    user = models.ForeignKey(UserProfile)
    article = models.ForeignKey(Article, related_name='article_comment')
    body = models.TextField()
    add_time = models.DateTimeField(auto_now_add=True)
    status = models.BooleanField(default=False)

    def get_reply(self):
        return Reply.objects.filter(comment=self.pk)


class Reply(models.Model):
    user = models.ForeignKey(UserProfile)
    comment = models.ForeignKey(Comment)
    body = models.TextField()
    add_time = models.DateTimeField(auto_now_add=True)
