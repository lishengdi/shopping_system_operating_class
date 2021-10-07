from django.http import  HttpResponse

def page_lsd(request):
    html="<h2>hello world</h2>"
    return HttpResponse(html)