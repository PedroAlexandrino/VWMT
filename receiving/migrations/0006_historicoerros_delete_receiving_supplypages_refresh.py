# Generated by Django 4.1.5 on 2023-04-06 08:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("receiving", "0005_rename_final_definirtempos_p1fim_and_more"),
    ]

    operations = [
        migrations.CreateModel(
            name="HistoricoErros",
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
                ("pagina", models.CharField(max_length=100, null=True)),
                ("erro", models.CharField(max_length=200, null=True)),
                ("timestamp", models.CharField(max_length=100, null=True)),
            ],
        ),
        migrations.DeleteModel(
            name="Receiving_SupplyPages_Refresh",
        ),
    ]