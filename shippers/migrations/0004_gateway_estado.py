# Generated by Django 2.1.15 on 2022-03-03 11:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("shippers", "0003_gateway_contacto"),
    ]

    operations = [
        migrations.AddField(
            model_name="gateway",
            name="estado",
            field=models.CharField(max_length=100, null=True),
        ),
    ]