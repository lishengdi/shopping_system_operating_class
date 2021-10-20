from django.shortcuts import render
from Models.models import Order, goodsPic
from Models.models import Goods
from django.urls import reverse
from django.http import HttpResponse,HttpResponseRedirect
from Models.models import Goods
# Create your views here.

def modify(request):
    UID=request.session.get('uid','-1')
    if UID=='-1':
        return HttpResponseRedirect(reverse("login"))


    GID = request.GET.get('goodsID','-1')
    if GID =='-1':
        return HttpResponse("修改商品：GID传递错误，请求非法")

    try:
        target = Goods.objects.get(GoodsID__exact=GID)
    except Exception as e:
        print(e)
        return HttpResponse("修改商品：查询失败！")

    if request.method=='GET':

        if target.UID==UID:
            return render(request,'modifyGoods.html',locals())
        else:
            return HttpResponse("修改商品：请求非法，您不是该商品的持有者")


    if request.method=='POST':
        GoodsName = request.POST.get('goodsname')
        Category = request.POST.get('category')
        OriginalPrice = request.POST.get('originalprice')
        Price = request.POST.get('price')
        Detail = request.POST.get('detail')

        try:
            # 先删除原有图片
            piclist=goodsPic.objects.filter(goodsID__exact=target.GoodsID)
            piclist.delete()

            target.GoodsName=GoodsName
            target.Category=Category
            target.OriginalPrice=OriginalPrice
            target.Price=Price
            target.Detail=Detail
            picsUPload = request.FILES.getlist('img')

            # 发布新的图片
            try:
                for f in picsUPload:
                    goodsPic.objects.create(goodsID=target.GoodsID, img=f)

                pics = goodsPic.objects.filter(goodsID__exact=target.GoodsID)
                target.mainPic = pics[0].img.url
            except Exception as e:
                print("发布商品：保存图片失败！")
                print(e)
            target.save()
        except Exception as e:
            print(e)
            return HttpResponse("修改商品：发布失败！")

        result="修改商品"
        return render(request,'Success_modifyGoods.html',locals())



def deleteGoods(request):

    UID = request.session.get('uid', '-1')
    if UID == '-1':
        return HttpResponseRedirect(reverse("login"))

    GID = request.GET.get('goodsID', '-1')
    if GID == '-1':
        return HttpResponse("修改商品：商品ID传递错误，请求非法")

    try:
        goods=Goods.objects.get(GoodsID__exact=GID)
        goods.Status=0
        goods.save()
    except Exception as e:
        print(e)
    return HttpResponse("ok")