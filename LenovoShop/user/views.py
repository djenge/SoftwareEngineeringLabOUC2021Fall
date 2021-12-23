from django.http.response import HttpResponse
from django.shortcuts import redirect, render
from user.models import UserModel ,UserTicketModel
from django.contrib.auth.hashers import make_password, check_password
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth import logout as auth_logout, authenticate, login as auth_login
from django.contrib.auth.models import User

# Create your views here.
# 个人主页
def home(request):
    if request.user.is_authenticated:
        return render(request, 'profile/profile.html')
    else:    
        date = "you are not login in"
        return HttpResponseRedirect('/user/login')
        

# 注册
def register(request):
    if request.method == 'GET':
        return render(request, 'register/register.html')

    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        password_c = request.POST.get('password_c')
        # 验证参数都不能为空
        if not all([username, password, password_c, email]):
            data = {
                'msg': '请填写完整的信息'
            }
            return render(request, 'register/register.html', {'data':data})
        # 加密password
        if(password != password_c):
            data = { 'msg': '两次密码不同' }
            return render(request, 'register/register.html', {'data':data})
        if UserModel.objects.filter(username=username).exists():
            data = {'msg':'该用户名已被注册'}
            return render(request, 'register/register.html', {'data':data})
        if UserModel.objects.filter(email=email).exists():
            data = {'msg':'该邮箱已被注册'}
            return render(request, 'register/register.html', {'data':data})            
            
        # 创建用户并添加到数据库
        UserModel.objects.create(username=username,
                                 password=password,
                                 password_c=password_c,
                                 email=email)
        User.objects.create_user(username, email, password)
        # 注册成功跳转到登陆页面
        return HttpResponseRedirect('/user/login')

# 登陆
def login(request):
    if request.method == 'GET':
        return render(request, 'login/login.html')

    if request.method == 'POST':
        username1 = request.POST.get('username')
        password1 = request.POST.get('password')
        data = {}
        
        # 验证信息是否填写完整
        if not all([username1, password1]):
            data['msg'] = '请填写完整的用户名或密码'
            return render(request, 'login/login.html', {'data':data})
        user = authenticate(request, username=username1, password=password1)
        print(username1 + password1)
        
        if user is not None:    
            auth_login(request, user)
            return HttpResponseRedirect('/user/home')
        
        else:
            data['msg']  = '用户名不存在,请注册后在登陆'
            return render(request, 'login/login.html', {'data':data})
            

# 退出
def logout(request):
    auth_logout(request)
