from django.conf.urls import url

from shopping import views

app_name = "shopping"
urlpatterns = [
    # 商品详情
    url(r'^detail/', views.detail, name='detail'),
    # 增加商品数量
    url(r'^addgoods/', views.add_goods, name='addgoods'),
    # 减少商品数量
    url(r'^subgoods/', views.sub_goods, name='subgoods'),
    # 刷新增添与减少商品数量
    url(r'^goodsnum/', views.goods_num, name='goodsnum'),
    # 加入购物车
    url(r'^addcart/', views.add_cart, name='addcart'),
    # 立即购买
    url(r'^buycart/', views.buy_cart, name='buycart'),
    # 计算商品总价
    url(r'^totalprice/', views.total_price, name='totalprice'),
    # 删除购物车商品
    url(r'^delgoodscart/', views.del_goods_cart, name='delgoodscart'),
    # 所有商品展示
    url(r'^list/', views.display_list, name='list'),
    # 展示个人购物车
    url(r'^mycart', views.my_cart, name='cart'),
]