from django.urls import path, include
from . import views

urlpatterns = [
    path('<int:orderID>',views.modify),
]