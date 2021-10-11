from django.urls import path
from . import views
urlpatterns = [
    path('addGoods',views.create,name='createGoods')
]
