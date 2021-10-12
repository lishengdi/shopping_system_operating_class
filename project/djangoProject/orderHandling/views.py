from django.shortcuts import render
from Models.models import Order
from django.urls import reverse
from django.http import HttpResponse,HttpResponseRedirect,HttpRequest
# Create your views here.

def comment (request):
    UID = request.session.get('uid', '-1')
    try:
        OID = request.get('orderID')
    except Exception as e:
        print(e)
        return HttpResponse("评论：订单号传递错误，请求非法")

    if UID == '-1':
        return HttpResponseRedirect(reverse("login"))
    try:
        target = Order.objects.get(OrderID__exact=OID)
    except Exception as e:
        print(e)
        return HttpResponse("评论：查询失败！")
    if request.method=='GET':
        if target.CID==UID:
            return render(request,reverse('startcomment.html'),target)
        else:
            return HttpResponse("评论:您不是购买者")
    if request.method=='POST':
        value=request.POST.get('comment')
        target.Comment=value
        try:
            target.save()
        except Exception as e:
            print(e)

def deliver (request):
    UID = request.session.get('uid', '-1')
    try:
        OID = request.get('orderID')
    except Exception as e:
        print(e)
        return HttpResponse("发货：订单号传递错误，请求非法")

    if UID == '-1':
        return HttpResponseRedirect(reverse("login"))
    try:
        target = Order.objects.get(OrderID__exact=OID)
    except Exception as e:
        print(e)
        return HttpResponse("发货：查询失败！")
    if request.method == 'GET':
        if target.SID == UID:
            return render(request, reverse('deliver.html'), target)
        else:
            return HttpResponse("发货:您不是该订单的双方")
    if request.method == 'POST':
        DepartADD = request.POST.get('departadd')
        ExpressNumber=request.POST.get('expressnumber')
        target.DepartADD=DepartADD;target.Status=2;target.ExpressNumber=ExpressNumber
        try:
            target.save()
        except Exception as e:
            print(e)

def cancel (request):
    UID = request.session.get('uid', '-1')
    try:
        OID = request.get('orderID')
    except Exception as e:
        print(e)
        return HttpResponse("取消订单：订单号传递错误，请求非法")

    if UID == '-1':
        return HttpResponseRedirect(reverse("login"))
    try:
        target = Order.objects.get(OrderID__exact=OID)
    except Exception as e:
        print(e)
        return HttpResponse("取消订单：查询失败！")
    if request.method == 'GET':
        if target.SID == UID or target.CID==UID:
            try:
                target.Status = 4
                target.save()
            except Exception as e:
                print(e)
        else:
            return HttpResponse("取消订单:您不是该订单的双方")

