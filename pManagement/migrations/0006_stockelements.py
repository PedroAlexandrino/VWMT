# Generated by Django 3.0.7 on 2022-04-27 18:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pManagement', '0005_auto_20210922_1133'),
    ]

    operations = [
        migrations.CreateModel(
            name='StockElements',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('partNumber', models.CharField(max_length=150, null=True)),
                ('descricao', models.CharField(max_length=150, null=True)),
                ('link', models.CharField(max_length=150, null=True)),
                ('expendable', models.CharField(max_length=150, null=True)),
                ('returnable', models.CharField(max_length=150, null=True)),
                ('quantidadeStock', models.CharField(max_length=150, null=True)),
            ],
            options={
                'verbose_name': 'Stock',
                'verbose_name_plural': 'Stock',
            },
        ),
    ]