from django.shortcuts import render
from Models.models import Order
from django.urls import reverse
from django.http import HttpResponse,HttpResponseRedirect
# Create your views here.

def modify(request):
    UID=request.session.get('uid','-1')
    try:
        OID = request.GET.get('orderID', '-1')
    except Exception as e:
        print(e)
        return HttpResponse("修改订单：订单号传递错误，请求非法")

    if UID=='-1':
        return HttpResponseRedirect(reverse("login"))

    try:
        target = Order.objects.get(OrderID__exact=OID)
    except Exception as e:
        print(e)
        return HttpResponse("修改订单：查询失败！")

    if request.method=='GET':

        if target.CID==UID:
            return render(request,reverse("modifyOrder.html"),target)
        else:
            return HttpResponse("修改订单：请求非法，您不是该订单用户")


    if request.method=='POST':
        GuestPhone = request.POST.get('guestphone')
        GuestName = request.POST.get('guestname')
        GuestADD = request.POST.get('guestadd')

        try:
            target.GuestName=GuestName
            target.GuestADD=GuestADD
            target.GuestPhone=GuestPhone

        except Exception as e:
            print(e)
            return HttpResponse("修改订单：修改失败！")

        return HttpResponseRedirect(reverse("myOrder.html"))