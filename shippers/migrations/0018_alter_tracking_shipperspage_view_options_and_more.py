# Generated by Django 4.1.5 on 2023-05-05 15:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("shippers", "0017_tracking_shipperspage_sub_items_and_more"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="tracking_shipperspage_view",
            options={"managed": False},
        ),
        migrations.AddField(
            model_name="tracking_shipperspage",
            name="sub_item_flag",
            field=models.CharField(max_length=50, null=True),
        ),
    ]