from django.contrib import admin
from . import models
admin.site.register(models.Goods)
admin.site.register(models.Order)
admin.site.register(models.User)
admin.site.register(models.goodsPic)
admin.site.register(models.UserCollect)
admin.site.register(models.ShoppingCar)
# Register your models here.
admin.site.site_title = "闲趣-后台管理"
admin.site.site_header = "闲趣-后台管理"