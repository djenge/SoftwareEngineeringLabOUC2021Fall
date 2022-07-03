from django.urls import path
from user import views

urlpatterns = [
    # 注册
    path('register/', views.register, name='register'),
    # 登陆
    path('login/', views.login, name='login'),
    # 退出
    path('logout/', views.logout, name='logout'),
    path('home', views.home, name='home')
    
]