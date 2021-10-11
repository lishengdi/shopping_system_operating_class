from django.urls import path
from . import views
urlpatterns = [

    path('userLogin',views.check_in,name='login')
]
