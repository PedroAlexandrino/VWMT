# Generated by Django 3.0.7 on 2022-09-05 15:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vware', '0005_produtos_cliente'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stockpackage',
            name='link',
            field=models.FileField(null=True, upload_to='StockPackage/'),
        ),
        migrations.AlterField(
            model_name='supplypackage',
            name='link',
            field=models.FileField(blank='true', null='true', upload_to='SupplyPackage/'),
        ),
    ]