from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from Models.models import User
from django.urls import reverse

# Create your views here.
def check_in(request):
    if request.method=='GET':
        stored_id=request.session.get('uid','-1')
        if(stored_id=='-1'):
            return render(request,'login.html')
        else:
            # return render(request,'index.html')
            return HttpResponse("index")

    if request.method=='POST':
        uname=request.POST.get('username','')
        Passwd=request.POST.get('password','')
        try:
            usr=User.objects.get(UName__exact=uname)
        except Exception as e:
            print('user not exit')
            return HttpResponse('user not exit')
        if (Passwd == usr.Passwd):
            request.session['uid'] = usr.UID
            return HttpResponse('check passed')
        else:
            return HttpResponse('password error')

def check_out(request):
    try:
        del request.session['uid']
        return HttpResponseRedirect(reverse('login'))
    except Exception as e:
        print(e)
