# Generated by Django 3.0.7 on 2022-09-12 11:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shippers', '0019_auto_20220909_2005'),
    ]

    operations = [
        migrations.AlterField(
            model_name='trackingpage',
            name='data',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]