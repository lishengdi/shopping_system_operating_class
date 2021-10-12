from django.shortcuts import render


from Models.models import Order
from Models.models import Goods
from django.urls import reverse
from django.http import HttpResponse,HttpResponseRedirect
# Create your views here.

def Buy(request):

    UID=request.session.get('uid','-1')
    if UID=='-1':
        return HttpResponseRedirect(reverse("login"))

    if request.method=='GET':
        # return render(request,reverse('null'))
        return HttpResponse("ok")
    if request.method=='POST':
        GoodsID=request.POST.get('goodsid')

        try:
            goods=Goods.objects.get(GoodsID__exact=GoodsID)
            SID = goods.UID
            Total = goods.Price
        except Exception as e:
            print(e)
        GuestPhone=request.POST.get('guestphone')
        GuestName =request.POST.get('guestname')
        GuestADD =request.POST.get('guestadd')
        ExpressNumber=""
        DepartADD =""
        PayMethod =1
        Status =1
        Comment =""

        try:
            order=Order.objects.create(CID=UID,GoodsID=GoodsID,SID=SID,Total=Total,GuestADD=GuestADD,GuestPhone=GuestPhone,
                                       GuestName=GuestName,DepartADD=DepartADD,PayMethod=PayMethod,Status=Status,Comment=Comment,ExpressNumber=ExpressNumber)
        except Exception as e:
            print(e)