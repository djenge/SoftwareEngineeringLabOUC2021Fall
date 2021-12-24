from typing import ValuesView
from django.urls import path,re_path

from store import views

app_name = 'store'
urlpatterns = [
    # 商城首页
    path('index/', views.index, name='index'),
    # 商城商品列表页, 这个就是shopping的商品列表，在shopping的urls和views里可以看到对应路由，你可以改一下这里
    re_path(r'^list/', views.list, name='list'),

    path('list/', views.list, name='list'),
    # 为了一开始路由
    path('', views.store, name='store'),
    path('index/home', views.home, name='home')
]
