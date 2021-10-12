from django.urls import path
from . import views
urlpatterns = [

    path('userRegister',views.sign_up,name="register"),
    path('modifyPersonalInfo',views.modify,name="modifyPersonalInfo")
]
