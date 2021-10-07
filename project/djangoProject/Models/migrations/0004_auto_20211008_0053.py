# Generated by Django 3.2.7 on 2021-10-07 16:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Models', '0003_auto_20211008_0030'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('OrderID', models.AutoField(primary_key=True, serialize=False, verbose_name='订单号')),
                ('GoodsID', models.IntegerField(verbose_name='商品号')),
                ('SID', models.IntegerField(verbose_name='商家ID')),
                ('CID', models.IntegerField(verbose_name='购买者ID')),
                ('Total', models.DecimalField(decimal_places=2, max_digits=10)),
                ('Time', models.DateTimeField(verbose_name='购买时间')),
                ('GuestPhone', models.CharField(max_length=15, verbose_name='收件人电话')),
                ('GuestName', models.CharField(max_length=30, verbose_name='收件人姓名')),
                ('GuestADD', models.TextField(verbose_name='收件人地址')),
                ('DepartADD', models.TextField(verbose_name='商家发货地址')),
                ('PayMethod', models.IntegerField(verbose_name='付款方式')),
                ('Status', models.IntegerField(verbose_name='订单状态')),
                ('Comment', models.TextField(verbose_name='订单评价')),
            ],
            options={
                'db_table': 'Order',
            },
        ),
        migrations.AlterField(
            model_name='user',
            name='DefaultADD',
            field=models.TextField(default='未指定', verbose_name='默认收货地址'),
        ),
    ]