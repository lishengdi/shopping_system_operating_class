from django.db import models

# Create your models here.
class User(models.Model):
    UID=models.AutoField("用户ID",primary_key=True)
    UName=models.CharField("用户名",max_length=50,default='unnamed')
    UPhone=models.CharField("用户电话",max_length=15,default='')
    Passwd=models.CharField("密码",max_length=20,default='')
    DefaultADD=models.TextField("默认收货地址",default='未指定')


    class Meta:
        db_table='User'

    def __str__(self):
        return 'ID:%s Name:%s Phone:%s Passwd:%s Address:%s'%(self.UID,self.UName,self.UPhone,self.Passwd,self.DefaultADD)

class Goods(models.Model):
    GoodsID=models.AutoField("商品号",primary_key=True)
    GoodsName=models.CharField("商品名",max_length=255,default='')
    Category=models.IntegerField("商品类型索引",default=0)
    OriginalPrice=models.DecimalField("商品原价",max_digits=10,decimal_places=2)
    Price=models.DecimalField("价格",max_digits=10,decimal_places=2)
    Status=models.IntegerField("商品状态") #1在售 0下架
    Detail=models.TextField("商品描述")
    UID=models.IntegerField("商家ID",default='',)
    mainPic=models.CharField("商品首图",default='/static/img/default.png',max_length=255)

    class Meta:
        db_table='Goods'

    def __str__(self):
        return 'GoodsID:%s GoodsName:%s Category:%s Status:%s UID:%s'%(self.GoodsID,self.GoodsName,self.Category,self.Status,self.UID)

class Order(models.Model):
    class Meta:
        db_table='Order'

    OrderID=models.AutoField("订单号",primary_key=True)
    GoodsID=models.IntegerField("商品号")
    SID=models.IntegerField("商家ID")
    CID=models.IntegerField("购买者ID")
    Total=models.DecimalField(max_digits=10,decimal_places=2)
    Time=models.DateTimeField("购买时间",auto_now_add=True)
    GuestPhone=models.CharField("收件人电话",max_length=15)
    GuestName=models.CharField("收件人姓名",max_length=50,default='null')
    GuestADD=models.TextField("收件人地址")
    DepartADD = models.TextField("商家发货地址")
    ExpressNumber = models.CharField("快递单号",max_length=25,default='')
    PayMethod=models.IntegerField("付款方式")  # 0 WeiChat 1 Alipay 2 ApplePay 3 Uni
    Status=models.IntegerField("订单状态") # 0 待支付 1 待发货 2 已发货 3 完成 4 售后
    Comment=models.TextField("订单评价")

    def __str__(self):
        return 'OrderID:%s GoodsID:%s SID:%s CID:%s Time:%s Status:%s'\
               %(self.OrderID,self.GoodsID,self.SID,self.CID,self.Time,self.Status)

class ShoppingCar(models.Model):
    UID=models.IntegerField("用户ID")
    GoodsID=models.IntegerField("商品ID")
    Time=models.DateTimeField("添加时间",auto_now_add=True)

    class Meta:
        db_table='ShoppingCar'

    def __str__(self):
        return 'UID:%s GoodsID:%s Time:%s'%(self.UID,self.GoodsID,self.Time)

class UserCollect(models.Model):
    UID=models.IntegerField("用户ID")
    GoodsID=models.IntegerField("商品ID")
    Time=models.DateTimeField("添加时间",auto_now_add=True)

    class Meta:
        db_table='UserCollect'
    def __str__(self):
        return 'UID:%s GoodsID:%s Time:%s'%(self.UID,self.GoodsID,self.Time)

class goodsPic(models.Model):
    goodsID=models.IntegerField("商品ID")
    img=models.ImageField("图片地址",upload_to='goodsIMG',default='/static/img/default.png')

    class Meta:
        db_table='goodsPIC'
