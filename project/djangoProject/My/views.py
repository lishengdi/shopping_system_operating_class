from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse


def show(request):
    UID = request.session.get('uid', '-1')
    if UID == '-1':
        return HttpResponseRedirect(reverse("login"))
    return render(request,'My.html')