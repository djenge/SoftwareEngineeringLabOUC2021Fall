from django.db import models
from ..login.models import User
from ..purchase.models import Item


# Create your models here.

# 定义评论的模型
class Comment(models.Model):
    # 评论用户的用户名
    user_name = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    # 评论内容
    comment_body = models.TextField()
    # 评论的时间
    comment_time = models.DateTimeField()
    # 上一条回复，类型也是评论，这时需要使用继承
    # latest_reply =
