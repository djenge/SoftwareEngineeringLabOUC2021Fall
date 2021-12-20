from django.http.response import HttpResponse
from django.shortcuts import redirect, render
from datetime import datetime, timedelta
from user.models import UserTicketModel
from user.models import UserModel ,UserTicketModel
from django.contrib.auth.hashers import make_password, check_password
from django.http import HttpResponseRedirect
from django.urls import reverse
# Create your views here.


# 个人主页
def home(request):
    if request.user.is_authenticated:
        return render(request, 'home/index.html')
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
        if(password != password):
            data = { 'msg': '两次密码不同' }
            return render(request, 'register/register.html', {'data':data})
        password = make_password(password)
        password_c = make_password(password_c)
        # 创建用户并添加到数据库
        UserModel.objects.create(username=username,
                                 password=password,
                                 password_c=password_c,
                                 email=email)
        # 注册成功跳转到登陆页面
        return HttpResponseRedirect('/user/login')

# 登陆
def login(request):
    if request.method == 'GET':
        return render(request, 'login/login.html')

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        data = {}
        
        # 验证信息是否填写完整
        if not all([username, password]):
            data['msg'] = '请填写完整的用户名或密码'
            print(data)
            return render(request, 'login/login.html', {'data':data})
            
            
        # 验证用户是否注册
        if UserModel.objects.filter(username=username).exists():
            user = UserModel.objects.get(username=username)
            # 验证密码是否正确
            if check_password(password, user.password):
                # 如果密码正确将ticket值保存在cookie中
                ticket = get_ticket()
                response = HttpResponseRedirect(reverse('store'))
                out_time = datetime.now() + timedelta(days=2)
                response.set_cookie('ticket', ticket, expires=out_time)
                # 保存ticket值到数据库user_ticket表中
                UserTicketModel.objects.create(user=user,
                                               out_time=out_time,
                                               )
                return HttpResponseRedirect('/user/home')
            # 验证错误
            else:
                data['msg'] = '用户名或密码错误'
                return render(request, 'login/login.html', {'data':data})
        else:
            data['msg']  = '用户名不存在,请注册后在登陆'
            return render(request, 'login/login.html', {'data':data})


# 退出
def logout(request):
    if request.method == 'GET':
        # 退出则删除数据库中的ticket值
        ticket = request.COOKIES.get('ticket')
        user_ticket = UserTicketModel.objects.filter(ticket=ticket).first()
        UserTicketModel.objects.filter(user=user_ticket.user).delete()
        return HttpResponseRedirect(reverse('user:login'))


def get_ticket():
    pass