# Generated by Django 4.1.5 on 2023-02-06 12:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("shippers", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Tracking_ShippersPage",
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
                ("ship_date", models.CharField(max_length=200, null=True)),
                ("ship_time", models.CharField(max_length=200, null=True)),
                ("city", models.CharField(max_length=200, null=True)),
                ("country", models.CharField(max_length=200, null=True)),
                ("carrier", models.CharField(max_length=200, null=True)),
                ("fob", models.CharField(max_length=200, null=True)),
                ("mode_of_transport", models.CharField(max_length=200, null=True)),
                ("total_master_packs", models.CharField(max_length=200, null=True)),
                ("confirmed", models.CharField(max_length=200, null=True)),
                (
                    "vehicle_id",
                    models.ForeignKey(
                        default=None,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="shippers.gateway",
                    ),
                ),
            ],
        ),
    ]