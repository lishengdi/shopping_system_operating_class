from django.urls import path
from . import views
urlpatterns = [
    path('buy/<int:goodsID>',views.Buy,name='buy'),
    path('showDetail/<int:goodsID>',views.showDetail,name='showDetail')
]
