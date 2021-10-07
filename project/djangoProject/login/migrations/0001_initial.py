# Generated by Django 3.2.7 on 2021-10-07 15:22

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('UID', models.IntegerField(primary_key=True, serialize=False, verbose_name='用户ID')),
                ('UName', models.CharField(default='unnamed', max_length=30, verbose_name='用户名')),
                ('UPhone', models.CharField(default='', max_length=15, verbose_name='用户电话')),
                ('Passwd', models.CharField(default='', max_length=20, verbose_name='密码')),
                ('DefaultADD', models.CharField(default='未指定', max_length=255, verbose_name='默认收货地址')),
            ],
        ),
    ]