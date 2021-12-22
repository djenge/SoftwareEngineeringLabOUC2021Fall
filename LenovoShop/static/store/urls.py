from typing import ValuesView
from django.urls import path

from store import views

urlpatterns = [
    # 商城首页
    path('index/', views.index, name='index'),
    # 商城商品列表页
    path('list/', views.list, name='list'),
    # 为了一开始路由
    path('', views.store, name='store'),
    path('index/home', views.home, name='home')
]