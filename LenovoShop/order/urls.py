from django.urls import re_path

from order import views


urlpatterns = [
    # 提交订单
    re_path(r'^place_order/', views.place_order, name='place_order'),
    # 用户中心 - 用户信息页
    re_path(r'^user_center_info/', views.user_center_info, name='user_center_info'),
    # 用户中心 - 用户订单页
    re_path(r'^user_center_order/', views.user_center_order, name='user_center_order'),
    # 用户中心 - 用户收货地址页
    re_path(r'^user_center_site/', views.user_center_site, name='user_center_site'),
]