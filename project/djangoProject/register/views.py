from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from django.urls import reverse
from Models.models import User
# Create your views here.
def sign_up(request):
    result=""
    if request.method=='GET':
        return render(request,'register.html')
    if request.method=='POST':
        UserName=request.POST.get('username','')
        Passwd=request.POST.get('passwd','')
        tel=request.POST.get('tel','')
        loc=request.POST.get('location','')
        check=User.objects.filter(UName__exact=UserName)
        if check:
            result="该用户名已存在，注册失败"
            return render(request,'register.html',locals())
        else:
            try:
                User.objects.create(UName=UserName,Passwd=Passwd,DefaultADD=loc,UPhone=tel)
            except Exception as e:
                print(e)
            # usr = User.objects.get(UName__exact=UserName)
            # request.session['uid']=usr.UID
            # return render(request, 'index.html')
            result = "注册"
            stored_id = request.session.get('uid', '-1')
            if (stored_id == '-1'):
                return render(request, 'showResultSuccess.html', locals())
            else:
                try:
                    del request.session['uid']
                    return HttpResponseRedirect(reverse('login'))
                except Exception as e:
                    print(e)
                return render(request, 'showResultSuccess.html', locals())



def modify(request):
    UID = request.session.get('uid', '-1')
    if UID == '-1':
        return HttpResponseRedirect(reverse('login'))
    try:
        usr = User.objects.get(UID__exact=UID)
    except Exception as e:
        print(e)
        return HttpResponse("个人信息修改：不存在该用户")
    if request.method == "GET":
        return render(request, 'modifyPersonalInfo.html', locals())
    if request.method == 'POST':
        UName = request.POST.get('username')
        UPhone = request.POST.get('tel')
        DefaultADD = request.POST.get('location')
        Passwd = request.POST.get('passwd')

        if UName != usr.UName:
            check = User.objects.filter(UName__exact=UName)
            if check:
                return (HttpResponse("修改用户名失败：该用户已存在！"))
        try:
            usr.UName = UName
            usr.Passwd = Passwd
            usr.DefaultADD = DefaultADD
            usr.UPhone = UPhone
            usr.save()
        except Exception as e:
            print(e)
            return HttpResponse("保存个人信息修改失败！")

        result="修改个人信息"
        return render(request, 'showResultSuccess.html', locals())
