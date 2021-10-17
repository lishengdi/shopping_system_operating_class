from django.db.models import Q
from django.shortcuts import render
from Models.models import ShoppingCar
from Models.models import Goods
from Models.models import User
from django.urls import reverse
from django.http import HttpResponse,HttpResponseRedirect
# Create your views here.
def add(request,goodsID):
    UID=request.session.get('uid','-1')
    if UID=='-1':
        return HttpResponseRedirect(reverse("login")) #防止恶意链接

    '''ID 验证'''

    try:
        goods=Goods.objects.get(GoodsID__exact=goodsID)
    except Exception as e:
        print("购物车：货物不存在")
        return HttpResponse("购物车：该货物不存在或已下架")

    try:
        ShoppingCar.objects.create(UID=UID,GoodsID=goodsID)
    except Exception as e :
        print(e)
        return HttpResponse("购物车：添加失败")

def delete(request,goodsID):
    UID = request.session.get('uid', '-1')
    if UID == '-1':
        return HttpResponseRedirect(reverse('login.html'))  # 防止恶意链接

    if goodsID == '':
        return HttpResponse('非法请求！')

    '''ID 验证'''

    try:
        target=ShoppingCar.objects.filter(Q(UID__exact=UID),Q(GoodsID__exact=goodsID))
        target.delete()
    except Exception as e:
        print(e)
        return HttpResponse("收藏：删除失败")