from django.shortcuts import render
from Models.models import Order
from Models.models import Goods
from django.urls import reverse
from django.http import HttpResponse,HttpResponseRedirect
from Models.models import Goods
# Create your views here.

def modify(request):
    UID=request.session.get('uid','-1')
    try:
        GID = request.get('goodsID')
    except Exception as e:
        print(e)
        return HttpResponse("修改商品：GID传递错误，请求非法")

    if UID == '-1':
        return HttpResponseRedirect(reverse("login"))

    try:
        target = Goods.objects.get(GoodsID__exact=GID)
    except Exception as e:
        print(e)
        return HttpResponse("修改商品：查询失败！")

    if request.method=='GET':

        if target.UID==UID:
            return render(request,reverse("modifyGoods.html"),target)
        else:
            return HttpResponse("修改商品：请求非法，您不是该商品的持有者")


    if request.method=='POST':
        GoodsName = request.POST.get('goodsname')
        IMG = request.POST.get('img')
        Category = request.POST.get('category')
        OriginalPrice = request.POST.get('originalprice')
        Price = request.POST.get('price')
        Detail = request.POST.get('detail')
        Status=request.POST.get('status')
        try:
            target.GoodsName=GoodsName
            target.Category=Category
            target.IMG=IMG
            target.OriginalPrice=OriginalPrice
            target.Price=Price
            target.Detail=Detail
            target.Status=Status
            target.save()
        except Exception as e:
            print(e)
            return HttpResponse("修改商品：发布失败！")

        return HttpResponseRedirect(reverse("myGoods.html"))