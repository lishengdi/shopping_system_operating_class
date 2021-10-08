from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from Models.models import User

# Create your views here.
def check_in(request):
    if request.method=='GET':
        return render(request,'login.html')
    if request.method=='POST':
        ID=(int)(request.POST.get('username',''))
        Passwd=request.POST.get('password','')

        try:
            usr=User.objects.get(UID__exact=ID)
            if(Passwd==usr.Passwd):
                return HttpResponse('check passed')
            else:
                return HttpResponse('password error')
        except Exception as e:
            print('user not exit')
            return HttpResponse('user not exit')

