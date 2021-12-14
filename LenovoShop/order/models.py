from django.db import models


from user.models import UserTicketModel
from store.models import GoodsValue
from user.models import UserModel
# Create your models here.

# 创建订单表模型
class OrderModel(models.Model):
    o_id = models.CharField(max_length=20, primary_key=True)        # 订单id
    o_user = models.ForeignKey(UserModel,on_delete=models.CASCADE)                           # 关联用户
    o_date = models.DateTimeField(auto_now=True)                    # 购买日期
    o_pay = models.BooleanField(default=False)                      # 付款属性
    o_total = models.DecimalField(max_digits=6, decimal_places=2)   # 总价
    o_address = models.CharField(max_length=150)                    # 收货地址

    class Meta:
        db_table = "order"



# 创建订单详情表模型
class OrderDetailModel(models.Model):
    goods = models.ForeignKey(GoodsValue,on_delete=models.CASCADE)        # 关联商品
    order = models.ForeignKey(OrderModel,on_delete=models.CASCADE)        # 关联商品
    price = models.DecimalField(max_digits=5, decimal_places=2)  # 总价
    count = models.IntegerField()                # 数量
    isTrue = models.BooleanField(default=False)  # 统计销量是否统计进去

    class Meta:
        db_table = "order_detail"


# 创建销量统计表模型
class Sales(models.Model):
    goods = models.ForeignKey(GoodsValue,on_delete=models.CASCADE)    # 管理商品名称
    count = models.IntegerField()            # 销量
    total_price = models.DecimalField(max_digits=5, decimal_places=2)  # 销售额

    class Meta:
        db_table = "sales"