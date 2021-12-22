from django.http.request import HttpRequest
from django.http.response import HttpResponse
from django.shortcuts import render
from store.models import GoodsValue, ArticleCategory
from django.http import HttpResponseRedirect
# Create your views here.



#商城首页

#to do it 
# 不用在意
def store(request):
    return HttpResponseRedirect('/store/index')

def home(request):
    return HttpResponse("this is my home")
# 主页
def index(request):
    return render(request, 'store/index.html')


# 商品列表
def list(request):
    pass




