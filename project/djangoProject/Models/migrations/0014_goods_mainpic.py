# Generated by Django 3.2.7 on 2021-10-18 08:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Models', '0013_remove_user_userhead'),
    ]

    operations = [
        migrations.AddField(
            model_name='goods',
            name='mainPic',
            field=models.CharField(default='/static/img/default.png', max_length=255, verbose_name='商品首图'),
        ),
    ]
