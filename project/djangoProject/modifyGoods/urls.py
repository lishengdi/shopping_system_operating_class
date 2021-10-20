from django.urls import path, include
from . import views

urlpatterns = [
    path('modify/',views.modify,name="modifyGoods"),
    path('delete/',views.deleteGoods,name="deleteGoods")
]