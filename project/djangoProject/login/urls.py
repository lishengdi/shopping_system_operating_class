from django.urls import path
from . import views
urlpatterns = [

    path('userLogin',views.check_in,name='login'),
    path('userLogout',views.check_out,name="logout")

]
