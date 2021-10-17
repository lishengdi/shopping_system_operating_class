from django.db.models import Q
from django.shortcuts import render


from Models.models import Order
from Models.models import Goods
from Models.models import goodsPic
from Models.models import UserCollect
from Models.models import ShoppingCar
from Models.models import User
from django.urls import reverse
from django.http import HttpResponse,HttpResponseRedirect
# Create your views here.

def Buy(request,goodsID):

    UID=request.session.get('uid','-1')
    if UID=='-1':
        return HttpResponseRedirect(reverse("login"))

    if request.method=='GET':
        GID=goodsID
        try:
            goods=Goods.objects.get(GoodsID__exact=GID)
            usr=User.objects.get(UID__exact=UID)
        except Exception as e:
            print(e)
            return HttpResponse("购买：查询失败，无此商品或用户非法")
        try:
            pics=goodsPic.objects.filter(goodsID__exact=GID)
            print(pics)
            pic=pics[0].img.url

        except Exception as e:
            print(e)
            nopic="yes"
            if goods.Status == 1:
                return render(request,'order.html',locals())
            else:
                return HttpResponse("购买失败：该商品已下架或已卖出")

        if goods.UID==usr.UID:
            return HttpResponse("购买：您无法购买自己发布的商品！")

        if goods.Status==1:
            return render(request,'order.html',locals())
        else:
            return HttpResponse("购买失败：该商品已下架或已卖出")


    if request.method=='POST':

        goods = Goods.objects.get(GoodsID__exact=goodsID)
        SID = goods.UID
        Total = goods.Price
        if goods.Status != 1 :
            return HttpResponse("购买失败：该商品已下架或已卖出")


        GuestPhone=request.POST.get('guestphone')
        GuestName =request.POST.get('guestname')
        GuestADD =request.POST.get('guestadd')
        ExpressNumber=""
        DepartADD =""
        PayMethod =1
        Status =1
        Comment =""

        try:
            order=Order.objects.create(CID=UID,GoodsID=goods.GoodsID,SID=SID,Total=Total,GuestADD=GuestADD,GuestPhone=GuestPhone,
                                       GuestName=GuestName,DepartADD=DepartADD,PayMethod=PayMethod,Status=Status,Comment=Comment,ExpressNumber=ExpressNumber)
            goods.Status = 0
            goods.save()
            dropTarget=ShoppingCar.objects.filter(Q(UID__exact=UID),Q(GoodsID__exact=goods.GoodsID))
            if dropTarget:
                dropTarget.delete()

        except Exception as e:
            print(e)

        return render(request,'Success_purchase.html')


def showDetail(request,goodsID):

    UID = request.session.get('uid', '-1')
    if UID == '-1':
        return HttpResponseRedirect(reverse("login"))

    try:
        username=User.objects.get(UID__exact=UID).UName
        goods=Goods.objects.get(GoodsID__exact=goodsID)
        sname=User.objects.get(UID__exact=goods.UID).UName
    except Exception as e :
        print(e)
        return HttpResponse("商品详情：查询失败，无此商品,或非法用户")

    try:
        pics = goodsPic.objects.filter(goodsID__exact=goodsID)
    except Exception as e:
        nopic = "yes"
        if goods.Status == 1:
            return render(request, 'order.html', locals())
        else:
            return HttpResponse("购买失败：该商品已下架或已卖出")
    try:
        star=UserCollect.objects.filter(Q(UID__exact=UID),Q(GoodsID__exact=goodsID))
        if star:
            ifstar=True
        else:
            ifstar=False
    except Exception as e:
        print(e)
        print("查询是否收藏：查询失败")


    if request.method == 'GET':

        if goods.Status==1:
            return render(request, 'detail.html',locals())
        else:
            return HttpResponse("商品详情：抱歉，该商品已下架或已卖出！")

