# Generated by Django 2.1.15 on 2022-02-25 14:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Abs2Priv",
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
                ("abs_par_id_2", models.CharField(max_length=100, null=True)),
                ("abs_item_2", models.CharField(max_length=100, null=True)),
                ("abs_qty_2", models.CharField(max_length=100, null=True)),
                ("abs_ship_qty_2", models.CharField(max_length=100, null=True)),
            ],
            options={
                "verbose_name": "Abs2 copy",
                "verbose_name_plural": "Abs2 copy",
                "managed": True,
            },
        ),
        migrations.CreateModel(
            name="AbscPriv",
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
                ("absc_carrier_2", models.CharField(max_length=100, null=True)),
                (
                    "absc_abs_id_2",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="shippers.Abs2Priv",
                    ),
                ),
            ],
            options={
                "verbose_name": "Absc copy",
                "verbose_name_plural": "Absc copy",
                "managed": True,
            },
        ),
        migrations.CreateModel(
            name="AbsMstrPriv",
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
                ("abs_id_2", models.CharField(max_length=100, null=True)),
                ("abs_shp_date_2", models.CharField(max_length=100, null=True)),
                ("abs_shp_time_2", models.CharField(max_length=100, null=True)),
                ("abs_qad01_2", models.CharField(max_length=150, null=True)),
                ("oid_abs_mstr_2", models.CharField(max_length=100, null=True)),
                ("abs_status_2", models.CharField(max_length=100, null=True)),
                ("abs_shipto_2", models.CharField(max_length=100, null=True)),
                ("abs_item_2", models.CharField(max_length=100, null=True)),
                ("abs_domain_2", models.CharField(max_length=100, null=True)),
            ],
            options={
                "verbose_name": "Abs mstr copy",
                "verbose_name_plural": "Abs mstr copy",
                "managed": True,
            },
        ),
        migrations.CreateModel(
            name="AdPriv",
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
                ("ad_city_2", models.CharField(max_length=100, null=True)),
                ("ad_country_2", models.CharField(max_length=100, null=True)),
                (
                    "ad_addr_2",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="shippers.AbsMstrPriv",
                    ),
                ),
            ],
            options={
                "verbose_name": "Ad copy",
                "verbose_name_plural": "Ad copy",
                "managed": True,
            },
        ),
        migrations.CreateModel(
            name="ficheiroShippers",
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
                ("masterSerialID", models.CharField(max_length=50, null=True)),
                ("preShipperShipper", models.CharField(max_length=50, null=True)),
                ("packItem", models.CharField(max_length=50, null=True)),
                ("numberOfPacks", models.CharField(max_length=50, null=True)),
            ],
            options={
                "verbose_name": "Tabela Shippers CONFIRMATION",
                "verbose_name_plural": "Tabela Shippers CONFIRMATION",
            },
        ),
        migrations.CreateModel(
            name="filteredTable",
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
                ("idComum", models.CharField(max_length=50, null=True)),
                ("shipDate", models.CharField(max_length=50, null=True)),
                ("shipTime", models.CharField(max_length=50, null=True)),
                ("name", models.CharField(max_length=50, null=True)),
                ("city", models.CharField(max_length=50, null=True)),
                ("carrier", models.CharField(max_length=50, null=True)),
                ("modeOfTransport", models.CharField(max_length=50, null=True)),
                ("vehicleID", models.CharField(max_length=50, null=True)),
                ("itemNumber", models.CharField(max_length=50, null=True)),
                ("description", models.CharField(max_length=150, null=True)),
                ("quantityToShip", models.CharField(max_length=150, null=True)),
                ("quantityShipped", models.CharField(max_length=150, null=True)),
                ("inProcess", models.CharField(max_length=150, null=True)),
                ("confirmed", models.CharField(max_length=150, null=True)),
            ],
            options={
                "verbose_name": "Tabela Shippers Filtrada",
                "verbose_name_plural": "Tabela Shippers Filtrada",
            },
        ),
        migrations.CreateModel(
            name="finalFicheiroShippers",
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
                ("masterSerialID", models.CharField(max_length=50, null=True)),
                ("preShipperShipper", models.CharField(max_length=50, null=True)),
                ("packItem", models.CharField(max_length=50, null=True)),
                ("numberOfPacks", models.CharField(max_length=50, null=True)),
            ],
            options={
                "verbose_name": "Tabela Shippers CONFIRMATION",
                "verbose_name_plural": "Tabela Shippers CONFIRMATION",
            },
        ),
        migrations.CreateModel(
            name="Gateway",
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
                ("dataHoraChegada", models.CharField(max_length=100, null=True)),
                ("empresa", models.CharField(max_length=100, null=True)),
                ("condutor", models.CharField(max_length=100, null=True)),
                ("primeiraMatricula", models.CharField(max_length=100, null=True)),
                ("segundaMatricula", models.CharField(max_length=100, null=True)),
                ("cargaDescarga", models.CharField(max_length=100, null=True)),
                ("doca", models.CharField(max_length=100, null=True)),
                ("destinoCarga", models.CharField(max_length=100, null=True)),
                ("tipoViatura", models.CharField(max_length=100, null=True)),
                ("dataHoraCarga", models.CharField(max_length=100, null=True)),
                ("dataHoraEntrada", models.CharField(max_length=100, null=True)),
                ("abandono", models.CharField(max_length=100, null=True)),
                ("comentEntrada", models.CharField(max_length=300, null=True)),
                ("dataHoraSaida", models.CharField(max_length=100, null=True)),
                ("comentSaida", models.CharField(max_length=300, null=True)),
            ],
            options={
                "verbose_name": "Gateway histórico",
                "verbose_name_plural": "Gateway histórico",
                "managed": True,
            },
        ),
        migrations.CreateModel(
            name="GatewayCargaDescarga",
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
                ("nome", models.CharField(max_length=100, null=True)),
            ],
        ),
        migrations.CreateModel(
            name="GatewayCondutor",
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
                ("nome", models.CharField(max_length=100, null=True)),
            ],
        ),
        migrations.CreateModel(
            name="GatewayDestinoCarga",
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
                ("nome", models.CharField(max_length=100, null=True)),
            ],
        ),
        migrations.CreateModel(
            name="GatewayDoca",
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
                ("nome", models.CharField(max_length=100, null=True)),
            ],
        ),
        migrations.CreateModel(
            name="GatewayEmpresa",
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
                ("nome", models.CharField(max_length=100, null=True)),
            ],
            options={
                "verbose_name": "Gateway Empresas",
                "verbose_name_plural": "Gateway Empresas",
                "managed": True,
            },
        ),
        migrations.CreateModel(
            name="GatewayPrimeiraMatricula",
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
                ("nome", models.CharField(max_length=100, null=True)),
            ],
        ),
        migrations.CreateModel(
            name="GatewaySegundaMatricula",
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
                ("nome", models.CharField(max_length=100, null=True)),
            ],
        ),
        migrations.CreateModel(
            name="GatewayTipoViatura",
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
                ("nome", models.CharField(max_length=100, null=True)),
            ],
        ),
        migrations.CreateModel(
            name="PreShipperBrowse",
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
                ("shipFrom", models.CharField(max_length=50, null=True)),
                ("type", models.CharField(max_length=50, null=True)),
                ("idShipper", models.CharField(max_length=50, null=True)),
                ("shipTo", models.CharField(max_length=50, null=True)),
                ("name", models.CharField(max_length=50, null=True)),
                ("city", models.CharField(max_length=50, null=True)),
                ("state", models.CharField(max_length=50, null=True)),
                ("country", models.CharField(max_length=50, null=True)),
                ("shipDate", models.CharField(max_length=50, null=True)),
                ("shipTime", models.CharField(max_length=50, null=True)),
                ("carrier", models.CharField(max_length=50, null=True)),
                ("shipVia", models.CharField(max_length=50, null=True)),
                ("fob", models.CharField(max_length=150, null=True)),
                ("transportMode", models.CharField(max_length=150, null=True)),
                ("vehicleId", models.CharField(max_length=150, null=True)),
                ("mbol", models.CharField(max_length=150, null=True)),
                ("preShipper", models.CharField(max_length=150, null=True)),
                ("totalMasterPacks", models.CharField(max_length=150, null=True)),
                ("loadedMasterPacks", models.CharField(max_length=150, null=True)),
                ("inProcess", models.CharField(max_length=150, null=True)),
                ("confirmed", models.CharField(max_length=150, null=True)),
                ("cancelled", models.CharField(max_length=150, null=True)),
                ("invMov", models.CharField(max_length=150, null=True)),
            ],
            options={
                "verbose_name": "Pre-Shipper Browse",
                "verbose_name_plural": "Pre-Shipper Browse",
            },
        ),
        migrations.CreateModel(
            name="PreShipperDetailBrowse",
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
                ("shipFrom", models.CharField(max_length=50, null=True)),
                ("type", models.CharField(max_length=50, null=True)),
                ("idShipper", models.CharField(max_length=50, null=True)),
                ("sortName", models.CharField(max_length=50, null=True)),
                ("shipTo", models.CharField(max_length=50, null=True)),
                ("shipToDock", models.CharField(max_length=50, null=True)),
                ("shipDate", models.CharField(max_length=50, null=True)),
                ("itemNumber", models.CharField(max_length=50, null=True)),
                ("description", models.CharField(max_length=50, null=True)),
                ("quantityToShip", models.CharField(max_length=50, null=True)),
                ("quantityShipped", models.CharField(max_length=50, null=True)),
                ("um", models.CharField(max_length=50, null=True)),
                ("site", models.CharField(max_length=50, null=True)),
                ("location", models.CharField(max_length=50, null=True)),
                ("lotSerial", models.CharField(max_length=150, null=True)),
                ("reference", models.CharField(max_length=150, null=True)),
                ("order", models.CharField(max_length=150, null=True)),
                ("line", models.CharField(max_length=150, null=True)),
                ("mbol", models.CharField(max_length=150, null=True)),
                ("confirmed", models.CharField(max_length=150, null=True)),
                ("invMov", models.CharField(max_length=150, null=True)),
                ("idGrande", models.CharField(max_length=150, null=True)),
            ],
            options={
                "verbose_name": "Pre-Shipper Detail Browse",
                "verbose_name_plural": "Pre-Shipper Detail Browse",
            },
        ),
        migrations.CreateModel(
            name="PtPriv",
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
                ("pt_desc1_2", models.CharField(max_length=100, null=True)),
                ("pt_desc2_2", models.CharField(max_length=100, null=True)),
                (
                    "pt_part_2",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="shippers.Abs2Priv",
                    ),
                ),
            ],
            options={
                "verbose_name": "Pt copy",
                "verbose_name_plural": "Pt copy",
                "managed": True,
            },
        ),
        migrations.CreateModel(
            name="Security",
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
                ("shipper", models.CharField(max_length=100, null=True)),
                ("masterSerials", models.CharField(max_length=100, null=True)),
                ("validacao", models.CharField(max_length=100, null=True)),
                ("dataHoraSaida", models.CharField(max_length=100, null=True)),
                ("comentarios", models.CharField(max_length=100, null=True)),
            ],
            options={
                "verbose_name": "Security histórico",
                "verbose_name_plural": "Security histórico",
                "managed": True,
            },
        ),
        migrations.CreateModel(
            name="SecurityShipper",
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
                ("nome", models.CharField(max_length=100, null=True)),
            ],
        ),
        migrations.CreateModel(
            name="Teste_browse",
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
                ("shipFrom", models.CharField(max_length=50, null=True)),
                ("type", models.CharField(max_length=50, null=True)),
                ("idBrowse", models.CharField(max_length=50, null=True)),
                ("shipTo", models.CharField(max_length=50, null=True)),
                ("name", models.CharField(max_length=50, null=True)),
                ("city", models.CharField(max_length=50, null=True)),
                ("state", models.CharField(max_length=50, null=True)),
                ("country", models.CharField(max_length=50, null=True)),
                ("shipDate", models.CharField(max_length=50, null=True)),
                ("shipTime", models.CharField(max_length=50, null=True)),
                ("carrier", models.CharField(max_length=50, null=True)),
                ("shipVia", models.CharField(max_length=50, null=True)),
                ("fob", models.CharField(max_length=50, null=True)),
                ("modeOfTransport", models.CharField(max_length=50, null=True)),
                ("vehicleID", models.CharField(max_length=50, null=True)),
                ("mbol", models.CharField(max_length=50, null=True)),
                ("preShipperID", models.CharField(max_length=50, null=True)),
                ("totalMasterPacks", models.CharField(max_length=50, null=True)),
                ("loadedMasterPacks", models.CharField(max_length=50, null=True)),
                ("inProcess", models.CharField(max_length=50, null=True)),
                ("confirmed", models.CharField(max_length=150, null=True)),
                ("cancelled", models.CharField(max_length=150, null=True)),
                ("invMov", models.CharField(max_length=150, null=True)),
            ],
            options={
                "verbose_name": "Teste Browse",
                "verbose_name_plural": "Teste Browse",
            },
        ),
        migrations.CreateModel(
            name="Teste_detail",
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
                ("shipFrom", models.CharField(max_length=50, null=True)),
                ("type", models.CharField(max_length=50, null=True)),
                ("preShipperShipper", models.CharField(max_length=50, null=True)),
                ("sortName", models.CharField(max_length=50, null=True)),
                ("shipTo", models.CharField(max_length=50, null=True)),
                ("shipToDock", models.CharField(max_length=50, null=True)),
                ("shipDate", models.CharField(max_length=50, null=True)),
                ("itemNumber", models.CharField(max_length=50, null=True)),
                ("description", models.CharField(max_length=100, null=True)),
                ("quantityToShip", models.CharField(max_length=50, null=True)),
                ("quantityShipped", models.CharField(max_length=50, null=True)),
                ("um", models.CharField(max_length=50, null=True)),
                ("site", models.CharField(max_length=50, null=True)),
                ("location", models.CharField(max_length=50, null=True)),
                ("lotSerial", models.CharField(max_length=50, null=True)),
                ("reference", models.CharField(max_length=50, null=True)),
                ("order", models.CharField(max_length=50, null=True)),
                ("line", models.CharField(max_length=150, null=True)),
                ("mbol", models.CharField(max_length=150, null=True)),
                ("confirmed", models.CharField(max_length=150, null=True)),
                ("invMov", models.CharField(max_length=150, null=True)),
                ("idDetail", models.CharField(max_length=100, null=True)),
            ],
            options={
                "verbose_name": "Teste Detail",
                "verbose_name_plural": "Teste Detail",
            },
        ),
    ]