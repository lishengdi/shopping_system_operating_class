from django.db.models import Q
from django.shortcuts import render
from Models.models import UserCollect
from Models.models import Goods
from Models.models import User
from django.http import HttpResponse,HttpResponseRedirect
from django.urls import reverse
# Create your views here.
def add(request,goodsID):
    UID=request.session.get('uid','-1')
    if UID=='-1':
        return HttpResponseRedirect(reverse('login.html')) #防止恶意链接

    if goodsID=='':
        return HttpResponse('非法请求！')

    '''ID 验证'''
    try:
        goods=Goods.objects.get(GoodsID__exact=goodsID)
    except Exception as e:
        print("收藏：货物不存在")
        return HttpResponse("该货物不存在或已下架")

    if goods.Status!=1:
        return HttpResponse("收藏：该货物不存在或已下架")

    try:
        UserCollect.objects.create(UID=UID,GoodsID=goodsID)
    except Exception as e :
        print(e)
        return HttpResponse("收藏：添加失败")

    return HttpResponse("Added")

def delete(request,goodsID):
    UID = request.session.get('uid', '-1')
    if UID == '-1':
        return HttpResponseRedirect(reverse('login.html'))  # 防止恶意链接

    if goodsID == '':
        return HttpResponse('非法请求！')

    '''ID 验证'''

    try:
        target=UserCollect.objects.filter(Q(UID__exact=UID),Q(GoodsID__exact=goodsID))
        target.delete()
    except Exception as e:
        print(e)
        return HttpResponse("收藏：删除失败")
    return HttpResponse("Deleted")

def show(request):
    UID = request.session.get('uid', '-1')
    if UID == '-1':
        return HttpResponseRedirect(reverse("login"))  # 防止恶意链接
    collections=UserCollect.objects.filter(UID__exact=UID)
    goodslist = [];count=0
    try:
        for i in collections:
            cargo=Goods.objects.get(GoodsID__exact=i.GoodsID)
            goodslist.append(cargo)
            count+=1

    except Exception as e:
        print(e)
        return HttpResponse("我的收藏：查询错误")
    if request.method=='GET':
        return render(request,'showMyCollection.html',locals())