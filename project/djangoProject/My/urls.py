from django.urls import path
from . import views
urlpatterns = [
    path('center/',views.show,name='myCenter'),

]
