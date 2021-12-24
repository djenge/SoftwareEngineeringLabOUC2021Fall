from django.urls import include, re_path

from shopping import views

app_name = "shopping"
urlpatterns = [
    # 商品详情
    re_path(r'^test/', views.test, name='test'),
    re_path(r'^store/', include('store.urls')),
    re_path(r'^detail/', views.detail, name='detail'),
    # 增加商品数量
    re_path(r'^addgoods/', views.add_goods, name='addgoods'),
    # 减少商品数量
    re_path(r'^subgoods/', views.sub_goods, name='subgoods'),
    # 刷新增添与减少商品数量
    re_path(r'^goodsnum/', views.goods_num, name='goodsnum'),
    # 加入购物车
    re_path(r'^addcart/', views.add_cart, name='addcart'),
    # 立即购买
    re_path(r'^buycart/', views.buy_cart, name='buycart'),
    # 计算商品总价
    re_path(r'^totalprice/', views.total_price, name='totalprice'),
    # 删除购物车商品
    re_path(r'^delgoodscart/', views.del_goods_cart, name='delgoodscart'),
    # 所有商品展示
    re_path(r'^list/', views.GoodsListView.as_view(), name='list'),
    # 展示个人购物车
    re_path(r'^mycart', views.my_cart, name='my_cart'),
]
