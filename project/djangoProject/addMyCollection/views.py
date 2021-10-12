from django.shortcuts import render
from Models.models import UserCollect
from Models.models import Goods
from Models.models import User
from django.http import HttpResponse,HttpResponseRedirect
from django.urls import reverse
# Create your views here.
def add(request):
    UID=request.session.get('uid','-1')
    if UID=='-1':
        return HttpResponseRedirect(reverse('login.html')) #防止恶意链接

    GID=request.GET.get('goodsID','-1')
    if GID=='-1':
        return HttpResponse('非法请求！')

    '''ID 验证'''

    try:
        goods=Goods.objects.get(GoodsID__exact=GID)
    except Exception as e:
        print("购物车：货物不存在")
        return HttpResponse("该货物不存在")

    try:
        usr = User.objects.get(UID__exact=UID)
    except Exception as e:
        print("购物车：非法用户")
        return HttpResponse("非法用户操作")

    try:
        UserCollect.objects.create(UID=UID,GoodsID=GID)
    except Exception as e :
        print(e)
        return HttpResponse("添加失败")