from django.shortcuts import render
from Models.models import Goods
from django.urls import reverse
from django.http import HttpResponse,HttpResponseRedirect
from Models.models import goodsPic
# Create your views here.

def create(request):
    # if valid
    UID = request.session.get('uid', '-1')
    if UID == '-1':
        return HttpResponseRedirect(reverse("login"))

    if request.method=='GET':
       return  render(request,'createGoods.html')


    if request.method=='POST':
        GoodsName=request.POST.get('goodsname')
        Category=request.POST.get('category')
        OriginalPrice=request.POST.get('originalprice')
        Price=request.POST.get('price')
        Detail=request.POST.get('detail')

        try:
            goods=Goods.objects.create(GoodsName=GoodsName,Category=Category,Status=1,OriginalPrice=OriginalPrice,
                             Price=Price,Detail=Detail,UID=UID)
        except Exception as e:
            print(e)
            return HttpResponse("发布闲置：发布失败！")
        pics=request.FILES.getlist('img')
        try:
            for f in pics:
                goodsPic.objects.create(goodsID=goods.GoodsID,img=f)

            pics = goodsPic.objects.filter(goodsID__exact=goods.GoodsID)
            goods.mainPic=pics[0].img.url
            goods.save()
        except Exception as e:
            print("发布商品：保存图片失败！")
            print(e)

        result="发布"
        return render(request,'Success_createGoods.html',locals())
