# Generated by Django 4.1.5 on 2023-02-28 08:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("shippers", "0004_tracking_shipperspage_estado"),
    ]

    operations = [
        migrations.AddField(
            model_name="tracking_shipperspage",
            name="timestamp",
            field=models.CharField(max_length=200, null=True),
        ),
    ]
