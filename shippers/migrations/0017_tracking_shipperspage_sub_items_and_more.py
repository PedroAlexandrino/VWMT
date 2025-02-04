# Generated by Django 4.1.5 on 2023-05-05 09:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("shippers", "0016_tracking_shipperspage_total_master_packs"),
    ]

    operations = [
        migrations.CreateModel(
            name="Tracking_ShippersPage_Sub_Items",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("abs_id", models.CharField(max_length=200, null=True)),
                ("abs_status", models.CharField(max_length=200, null=True)),
                ("abs_shipfrom", models.CharField(max_length=200, null=True)),
                ("abs_item", models.CharField(max_length=200, null=True)),
                ("abs_qty", models.CharField(max_length=200, null=True)),
                ("abs_ship_qty", models.CharField(max_length=200, null=True)),
            ],
        ),
        migrations.AlterModelOptions(
            name="tracking_shipperspage_view",
            options={},
        ),
        migrations.AddField(
            model_name="tracking_shipperspage",
            name="tracking_shipperspage_sub_items",
            field=models.ManyToManyField(to="shippers.tracking_shipperspage_sub_items"),
        ),
    ]
