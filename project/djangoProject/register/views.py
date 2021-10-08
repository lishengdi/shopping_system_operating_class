from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from django.urls import reverse
from Models.models import User
# Create your views here.
def sign_up(request):
    if request.method=='GET':
        return render(request,'register.html')
    if request.method=='POST':
        UserName=request.POST.get('username','')
        Passwd=request.POST.get('passwd','')
        tel=request.POST.get('tel','')
        loc=request.POST.get('location','')

        try:
            User.objects.create(UName=UserName,Passwd=Passwd,DefaultADD=loc,UPhone=tel)
        except Exception as e:
            print(e)
        return HttpResponse('OK!')