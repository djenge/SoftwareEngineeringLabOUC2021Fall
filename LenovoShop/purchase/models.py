from django.db import models

# Create your models here.
from ..login.models import User
from ..comment.models import Comment


# 处理器模型
class Processor(models.Model):
    # 型号名称
    name = models.CharField(max_length=100)
    # 该型号价格
    price = models.FloatField()
    # 速度，用字符串表示
    speed = models.CharField(max_length=100)


# 显卡模型
class GraphicCard(models.Model):
    # 型号名称
    name = models.CharField(max_length=100)
    # 该型号价格
    price = models.FloatField()
    # 速度，用字符串表示
    speed = models.CharField(max_length=100)


# 显示屏模型
class Monitor(models.Model):
    # 型号名称
    name = models.CharField(max_length=100)
    # 该型号价格
    price = models.FloatField()
    # 速度，用字符串表示
    speed = models.CharField(max_length=100)


# 商品模型
class Item(models.Model):
    # 商品ID，方便与评论关联
    id = models.IntegerField()
    # 商品名称
    name = models.CharField(max_length=200)
    # 商品价格
    price = models.FloatField()
    # 处理器
    processor = models.ForeignKey(Processor, on_delete=models.DO_NOTHING)
    # 显卡
    graphic_card = models.ForeignKey(GraphicCard, on_delete=models.DO_NOTHING)
    # 显示器
    monitor = models.ForeignKey(Monitor, on_delete=models.DO_NOTHING)
    # 商品样本图片
    sample_pic = models.ImageField(blank=True, null=True)
    # 关联评论
    item_comments = models.ForeignKey(Comment, on_delete=models.DO_NOTHING)


# 交易模型
class Transaction(models.Model):
    # 收货地址
    deliver_address = models.TextField()
    # 交易用户
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    # 购买的商品
    item = models.ForeignKey(Item, on_delete=models.DO_NOTHING)
    # 交易时间
    transaction_time = models.DateTimeField()
    # 运费, 默认0
    delivery_fees = models.FloatField()
    # 最后成交的价格
    final_price = models.FloatField()
