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

def index(request):
    keywords=""
    UID = request.session.get('uid', '-1')
    if UID == '-1':
        return HttpResponseRedirect(reverse("login"))

    try:
        usrname=User.objects.get(UID__exact=UID).UName

    except Exception as e:
        print(e)
        return HttpResponse("非法用户")


    action = request.GET.get('action', '-1')
    if action=='-1':      #默认展示所有商品
        try:
            goodslist=Goods.objects.filter(Status__exact=1)
            return render(request,'index.html',locals())
        except Exception as e:
            print(e)

    elif action=='search':
        try:
            keywords=request.GET.get('keywords')
            goodslist=Goods.objects.filter(Q(GoodsName__contains=keywords),Q(Status__exact=1))
            return render(request,'index.html',locals())
        except Exception as e:
            print(e)

    elif action=='select':
        try:
            type=request.GET.get('type')
            goodslist=Goods.objects.filter(Q(Category__exact=type),Q(Status__exact=1))
            return render(request, 'index.html', locals())
        except Exception as e:
            print(e)