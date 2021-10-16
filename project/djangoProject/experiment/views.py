from django.shortcuts import render
from Models.models import goodsPic
from django.http import HttpResponse
def file_upload_test(request):
    if request.method=='GET':
        return render(request,'file_upload_test.html')
    elif request.method=='POST':
        gid=1233133
        files=request.FILES.getlist('myfile')
        try:
            for f in files:
                goodsPic.objects.create(goodsID=gid,img=f)
            return HttpResponse("ok")
        except Exception as e:
            print("xxxxxxx")
            print(e)

# Create your views here.
