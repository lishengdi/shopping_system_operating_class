from django.urls import path, include
from . import views

urlpatterns = [
    path('modify/<int:goodsID>',views.modify),
    path('delete/<int:goodsID>',views.deleteGoods),

]