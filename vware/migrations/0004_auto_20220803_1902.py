# Generated by Django 3.0.7 on 2022-08-03 19:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vware', '0003_auto_20220803_0836'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='produtos',
            name='cliente',
        ),
        migrations.AddField(
            model_name='produtos',
            name='cliente',
            field=models.ManyToManyField(to='vware.ClientesOEM'),
        ),
    ]