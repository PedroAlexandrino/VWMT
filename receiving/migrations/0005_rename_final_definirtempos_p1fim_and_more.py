# Generated by Django 4.1.5 on 2023-04-03 08:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("receiving", "0004_receiving_supplypages_refresh_estado"),
    ]

    operations = [
        migrations.RenameField(
            model_name="definirtempos",
            old_name="final",
            new_name="p1Fim",
        ),
        migrations.RenameField(
            model_name="definirtempos",
            old_name="inicio",
            new_name="p1Inicio",
        ),
        migrations.AddField(
            model_name="definirtempos",
            name="p2Fim",
            field=models.CharField(blank="true", max_length=150, null=True),
        ),
        migrations.AddField(
            model_name="definirtempos",
            name="p2Inicio",
            field=models.CharField(blank="true", max_length=150, null=True),
        ),
    ]