from django.db import models


# Create your models here.

class User(models.Model):
    # 用户名
    user_name = models.CharField(max_length=20)
    # 密码
    user_password = models.CharField(max_length=15)
    # 用户绑定的电子邮箱，注册时需要使用
    user_email = models.EmailField(max_length=254)
    # 用户头像
    user_avatar = models.ImageField(blank=True, null=True)
    # 用户注册时间
    user_joined_time = models.DateTimeField(default="")
