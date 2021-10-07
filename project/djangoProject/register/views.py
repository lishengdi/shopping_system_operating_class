from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from django.urls import reverse
# Create your views here.
def sign_up(request):
    if request.method=='GET':
        return render(request,'register.html')
    if request.method=='POST':
        ID=request.POST.get('username','')
        Passwd=request.POST.get('passwd','')
        tel=request.POST.get('tel','')
        loc=request.POST.get('location','')
        print(locals())
    return HttpResponseRedirect(reverse('login_path'))