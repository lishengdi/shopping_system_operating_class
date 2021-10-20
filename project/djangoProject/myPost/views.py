from django.db.models import Q
from django.shortcuts import render

# Create your views here.
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from Models.models import Order, Goods


def show(request):
    UID = request.session.get('uid', '-1')
    if UID == '-1':
        return HttpResponseRedirect(reverse("login"))
    a=dict();b={};c={}
    try:
        waitBuylist=Goods.objects.filter(Q(UID__exact=UID),Q(Status__exact=1))

        waitDeliverlist = Order.objects.filter(Q(SID__exact=UID), Q(Status__exact=1))
        for i in waitDeliverlist:
            a[i]=Goods.objects.get(GoodsID__exact=i.GoodsID)
        waitReceive = Order.objects.filter(Q(SID__exact=UID), Q(Status__exact=2))
        for i in waitReceive:
            b[i]=Goods.objects.get(GoodsID__exact=i.GoodsID)
        completelist=Order.objects.filter(Q(SID__exact=UID),Q(Status__exact=3))
        for i in completelist:
            c[i]=Goods.objects.get(GoodsID__exact=i.GoodsID)
    except Exception as e:
        print(e)
    return render(request,'showMyPost.html',locals())

