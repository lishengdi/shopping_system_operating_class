from django.urls import path, include
from . import views

urlpatterns = [
    path('comment/',views.comment,name="makeComment"),
    path('deliver/',views.deliver,name="makeDeliver"),
    path('cancel/',views.cancel,name="orderCancel"),
]