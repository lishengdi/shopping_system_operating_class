# Generated by Django 3.2.7 on 2021-10-11 09:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Models', '0007_auto_20211011_1625'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='Time',
            field=models.DateTimeField(auto_now_add=True, verbose_name='购买时间'),
        ),
    ]
