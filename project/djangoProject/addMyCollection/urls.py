from django.urls import path, include
from . import views
urlpatterns = [
    path('add/<int:goodsID>',views.add,name="addMyCollection"),
    path('delete/<int:goodsID>',views.delete,name="deleteMyCollection"),
    path('show/',views.show,name="showMyCollection")
    ]
