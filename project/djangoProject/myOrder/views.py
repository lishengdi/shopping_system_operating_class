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
    a={};b={};c={}

    try:
        waitDeliver=Order.objects.filter(Q(CID__exact=UID),Q(Status__exact=1))
        for i in waitDeliver:
            a[i]=Goods.objects.get(GoodsID__exact=i.GoodsID)
        alreadyDelivered=Order.objects.filter(Q(CID__exact=UID),Q(Status__exact=2))
        for i in alreadyDelivered:
            b[i]=Goods.objects.get(GoodsID__exact=i.GoodsID)
        completed=Order.objects.filter(Q(CID__exact=UID),Q(Status__exact=3))
        for i in completed:
            c[i]=Goods.objects.get(GoodsID__exact=i.GoodsID)

    except Exception as e:
        print(e)

    return render(request,'showMyOrder.html',locals())
