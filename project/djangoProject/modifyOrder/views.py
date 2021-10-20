from django.shortcuts import render
from Models.models import Order, Goods
from django.urls import reverse
from django.http import HttpResponse,HttpResponseRedirect
# Create your views here.

def modify(request):
    UID=request.session.get('uid','-1')
    if UID == '-1':
        return HttpResponseRedirect(reverse("login"))


    OID = request.GET.get('orderID', '-1')

    if OID == '-1':

        return HttpResponse("修改订单：订单号传递错误，请求非法")


    try:
        target = Order.objects.get(OrderID__exact=OID)
        goods=Goods.objects.get(GoodsID__exact=target.GoodsID)
    except Exception as e:
        print(e)
        return HttpResponse("修改订单：查询失败！")

    if request.method=='GET':

        if target.Status!=1:
            return HttpResponse("修改订单：请求非法，目前订单状态不支持修改")

        if target.CID==UID:
            return render(request,"modifyOrder.html",locals())
        else:
            return HttpResponse("修改订单：请求非法，您不是该订单用户")


    if request.method=='POST':

        if target.Status!=1:
            return HttpResponse("修改订单：请求非法，目前订单状态不支持修改")

        GuestPhone = request.POST.get('guestphone')
        GuestName = request.POST.get('guestname')
        GuestADD = request.POST.get('guestadd')

        try:
            target.GuestName=GuestName
            target.GuestADD=GuestADD
            target.GuestPhone=GuestPhone
            target.save()

        except Exception as e:
            print(e)
            return HttpResponse("修改订单：修改失败！")

        # return HttpResponseRedirect(reverse("myOrder.html"))
        result="修改订单"
        return render(request,'Success_modifyOrder.html',locals())


