from datetime import datetime

import django.contrib.auth
from PIL.Image import Image
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
from login.models import User


# 简单过滤器，验证是否已经登录
def verification(request):
    login_session = request.session['IS_LOGIN']
    if login_session is not None and login_session:
        return True
    else:
        return False


def index(request):
    return render(request, './index/index.html')


def login(request):
    if request.method == 'POST':
        user_name = request.POST.get('username', '')
        pass_word = request.POST.get('password', '')
        user = User.objects.filter(user_name=user_name)  # 查看数据库里是否有该用户名
        if user:  # 如果存在
            user = User.objects.get(user_name=user_name)  # 读取该用户信息
            if pass_word == user.password:  # 检查密码是否匹配
                request.session['IS_LOGIN'] = True  # 记录浏览器cookie
                request.session['username'] = user_name
                return render(request, 'index.html', {'user': user})
            else:
                return render(request, 'login.html', {'error': '密码错误!'})
        else:
            return render(request, 'login.html', {'error': '用户名不存在!'})
    else:
        return render(request, 'login.html')


def register(request):
    if request.method == 'POST':
        user_name = request.POST.get('username', '')
        pass_word_1 = request.POST.get('password_1', '')
        pass_word_2 = request.POST.get('password_2', '')
        email = request.POST.get('email', '')
        avatar = request.FILES.get('avatar')
        if User.objects.filter(user_name=user_name):
            return render(request, 'register.html', {'error': '用户已存在'})
            # 将表单写入数据库
        if (pass_word_1 != pass_word_2):
            return render(request, 'register.html', {'error': '两次密码请输入一致'})
        user = User()
        if avatar:
            user.user_avatar = 'media/' + user_name + '.png'  # 保存用户头像
            img = Image.open(avatar)
            size = img.size
            print(size)
            # 因为是要圆形，所以需要正方形的图片
            r2 = min(size[0], size[1])
            if size[0] != size[1]:
                img = img.resize((r2, r2), Image.ANTIALIAS)
            # 最后生成圆的半径
            r3 = int(r2 / 2)
            img_circle = Image.new('RGBA', (r3 * 2, r3 * 2), (255, 255, 255, 0))
            pima = img.load()  # 像素的访问对象
            pimb = img_circle.load()
            r = float(r2 / 2)  # 圆心横坐标
            for i in range(r2):
                for j in range(r2):
                    lx = abs(i - r)  # 到圆心距离的横坐标
                    ly = abs(j - r)  # 到圆心距离的纵坐标
                    l = (pow(lx, 2) + pow(ly, 2)) ** 0.5  # 三角函数 半径

                    if l < r3:
                        pimb[i - (r - r3), j - (r - r3)] = pima[i, j]
            img_circle.save('LenovoShop/static/media/' + user_name + '.png')
        user.user_name = user_name
        user.user_password = pass_word_1
        user.user_email = email
        user.user_joined_time = datetime.datetime().now()
        user.save()
        # 返回注册成功页面
        return render(request, 'index.html')
    else:
        return render(request, 'register.html')


def reset_password(request):
    if not verification(request):
        return render(request, 'login.html', {'error': '未登录'})
    if request.method == 'POST':
        user_name = request.POST.get('username')
        old_password = request.POST.get('old_password')
        new_password = request.POST.get('new_password')
        repeat_password = request.POST.get('repeat_password')
        user = User.objects.get(user_name=user_name)  # 读取该用户信息
        if old_password == user.password:  # 检查密码是否匹配
            if new_password == repeat_password:
                user.user_password = new_password
            else:
                return render(request, 'reset.html', {'error': '两次输入密码不一致'})
        else:
            render(request, 'reset.html', {'error': '原始密码不正确'})
        user.save()
        return render(request, 'reset.html')
    return render(request, 'reset.html')


def logout(requst):
    django.contrib.auth.logout()  # 清除所有session
    return render(requst, 'index.html')
