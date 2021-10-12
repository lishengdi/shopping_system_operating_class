from django.urls import path, include
from . import views

urlpatterns = [
    path('comment/<int:orderID>',views.comment),
    path('deliver/<int:orderID>',views.deliver),
    path('cancel/<int:orderID>',views.cancel),
]