from django.shortcuts import render
from Models.models import Order, Goods, User
from django.urls import reverse
from django.http import HttpResponse,HttpResponseRedirect,HttpRequest
# Create your views here.

def comment (request):
    UID = request.session.get('uid', '-1')
    if UID == '-1':
        return HttpResponseRedirect(reverse("login"))


    OID = request.GET.get('orderID','-1')
    if OID=='-1':
        return HttpResponse("评论：订单号传递错误，请求非法")

    try:
        target = Order.objects.get(OrderID__exact=OID)
        goods = Goods.objects.get(GoodsID__exact=target.GoodsID)
    except Exception as e:
        print(e)
        return HttpResponse("评论：查询失败！")

    if request.method=='GET':

        if target.Status!=2:
            return HttpResponse("评论:该订单目前状态不支持评论")

        if target.CID==UID:
            return render(request,'makeComment.html',locals())
        else:
            return HttpResponse("评论:您不是购买者")

    if request.method=='POST':

        if target.CID != UID:
            return HttpResponse("评论:您不是购买者")

        if target.Status!=2:
            return HttpResponse("评论:该订单目前状态不支持评论")

        value=request.POST.get('comment')
        target.Comment=value
        target.Status = 3
        try:
            target.save()
        except Exception as e:
            print(e)

        result="收货评价"
        return render(request,'Success_comment.html',locals())

def deliver (request):
    UID = request.session.get('uid', '-1')
    if UID == '-1':
        return HttpResponseRedirect(reverse("login"))

    OID = request.GET.get('orderID', '-1')
    if OID == '-1':
        return HttpResponse("发货：订单号传递错误，请求非法")

    try:
        target = Order.objects.get(OrderID__exact=OID)
        goods=Goods.objects.get(GoodsID__exact=target.GoodsID)

    except Exception as e:
        print(e)
        return HttpResponse("发货：查询失败！")

    if target.Status!=1:
        return HttpResponse("发货：订单状态错误")


    if request.method == 'GET':
        if target.SID == UID:
            return render(request, 'deliver.html', locals())
        else:
            return HttpResponse("发货:您不是该订单的双方")
    if request.method == 'POST':
        if target.SID != UID:
            return HttpResponse("发货:您不是该订单的双方")
        DepartADD = request.POST.get('departadd')
        ExpressNumber=request.POST.get('expressnumber')
        target.DepartADD=DepartADD;target.Status=2;target.ExpressNumber=ExpressNumber
        try:
            target.save()
        except Exception as e:
            print(e)
        result="发货"
        return render(request,'Success_deliver.html',locals())


def cancel (request):
    UID = request.session.get('uid', '-1')
    if UID == '-1':
        return HttpResponseRedirect(reverse("login"))


    OID = request.GET.get('orderID','-1')
    if OID =='-1':
        return HttpResponse("取消订单：订单号传递错误，请求非法")
    try:
        target = Order.objects.get(OrderID__exact=OID)
        goods=Goods.objects.get(GoodsID__exact=target.GoodsID)
    except Exception as e:
        print(e)
        return HttpResponse("取消订单：查询失败！")

    if target.Status!=1:
        return HttpResponse("取消订单：该订单目前状态不支持取消！")

    if request.method == 'GET':
        if target.CID==UID:
            try:
                target.delete()
                goods.Status=1
                goods.save()
            except Exception as e:
                print(e)
        else:
            return HttpResponse("取消订单:您不是该订单的购买方")
        return HttpResponse("ok")
