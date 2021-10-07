from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
# Create your views here.
def check_in(request):
    if request.method=='GET':
        return render(request,'login.html')
    if request.method=='POST':
        ID=request.POST.get('username','')
        Passwd=request.POST.get('password','')
        print(ID+"  "+Passwd)
    return HttpResponse('ok')