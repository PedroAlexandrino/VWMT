# Generated by Django 2.1.15 on 2022-03-11 09:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("shippers", "0006_auto_20220310_1159"),
    ]

    operations = [
        migrations.CreateModel(
            name="GatewayInfoCondutor",
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
                (
                    "condutor",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="shippers.GatewayCondutor",
                    ),
                ),
                (
                    "condutorID",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="shippers.GatewayCondutorID",
                    ),
                ),
                (
                    "contacto",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="shippers.GatewayContactoCondutor",
                    ),
                ),
            ],
        ),
    ]