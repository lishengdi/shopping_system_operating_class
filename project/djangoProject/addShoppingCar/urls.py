from django.urls import path, include
from . import views
urlpatterns = [
    path('add/<int:goodsID>',views.add,name="addShoppingCar"),
    path('delete/<int:goodsID>', views.delete, name="deleteShoppingCar"),
    path('show/',views.show,name="showMyShoppingCar")
]
