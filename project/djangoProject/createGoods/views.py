from django.shortcuts import render
from Models.models import Goods
from django.urls import reverse
from django.http import HttpResponse,HttpResponseRedirect
# Create your views here.

def create(request):
    # if valid
    UID = request.session.get('uid', '-1')
    if UID == '-1':
        return HttpResponseRedirect('login.html')

    if request.method=='GET':
       return  render(request,'createGoods.html')


    if request.method=='POST':
        GoodsName=request.POST.get('goodsname')
        IMG=request.POST.get('img')
        Category=request.POST.get('category')
        OriginalPrice=request.POST.get('originalprice')
        Price=request.POST.get('price')
        Detail=request.POST.get('detail')

        try:
            Goods.objects.create(GoodsName=GoodsName,IMG=IMG,Category=Category,Status=1,OriginalPrice=OriginalPrice,
                             Price=Price,Detail=Detail,UID=UID)
        except Exception as e:
            print(e)
            return HttpResponse("发布闲置：发布失败！")
