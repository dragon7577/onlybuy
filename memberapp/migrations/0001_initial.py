# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2018-10-26 02:16
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Banner',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bannerimg', models.ImageField(default='normal.png', upload_to='static/img/banner', verbose_name='论波图')),
            ],
        ),
        migrations.CreateModel(
            name='Goods',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='商品名称', max_length=30, verbose_name='商品名称')),
                ('price', models.DecimalField(decimal_places=2, max_digits=8, verbose_name='商品价格')),
                ('desc', models.CharField(max_length=1000, null=True, verbose_name='描述')),
                ('goodsimg', models.ImageField(default='normal.png', upload_to='static/img/goods', verbose_name='产品图')),
                ('isDelete', models.BooleanField(default=False, verbose_name='是否下架')),
            ],
        ),
        migrations.CreateModel(
            name='GoodsDetail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('specifice', models.CharField(default='规格', max_length=30, verbose_name='规格')),
                ('stock', models.IntegerField(default=0, verbose_name='库存')),
                ('goods', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='memberapp.Goods')),
            ],
        ),
        migrations.CreateModel(
            name='GoodsType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='分类名称', max_length=30, verbose_name='分类名称')),
                ('desc', models.CharField(default='商品描述', max_length=200, verbose_name='描述')),
                ('isDelete', models.BooleanField(default=False, verbose_name='是否下架')),
            ],
            options={
                'db_table': 'goods_type',
            },
        ),
        migrations.CreateModel(
            name='Promise',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='承诺', max_length=30, verbose_name='承诺')),
                ('desc', models.CharField(default='承诺商品描述', max_length=200, verbose_name='承诺描述')),
            ],
            options={
                'db_table': 'sale_promise',
            },
        ),
        migrations.AddField(
            model_name='goods',
            name='promise',
            field=models.ManyToManyField(to='memberapp.Promise'),
        ),
        migrations.AddField(
            model_name='goods',
            name='type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='memberapp.GoodsType'),
        ),
        migrations.AddField(
            model_name='banner',
            name='type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='memberapp.GoodsType'),
        ),
    ]
