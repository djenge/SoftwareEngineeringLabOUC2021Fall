from django.db import models
from user.models import UserModel
from store.models import GoodsValue
# Create your models here.




class CartInfo(models.Model):
    # 关联用户
    user = models.ForeignKey(UserModel,on_delete=models.CASCADE)
    # 关联商品
    goods = models.ForeignKey(GoodsValue,on_delete=models.CASCADE)
    # 购买的数量
    count = models.IntegerField(default=1)
