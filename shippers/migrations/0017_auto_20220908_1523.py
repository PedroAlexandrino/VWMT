# Generated by Django 3.0.7 on 2022-09-08 15:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shippers', '0016_auto_20220908_1427'),
    ]

    operations = [
        migrations.AlterField(
            model_name='trackingpage',
            name='confirmacao',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='trackingpage',
            name='data',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='trackingpage',
            name='fimPrep',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='trackingpage',
            name='incioPrep',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]