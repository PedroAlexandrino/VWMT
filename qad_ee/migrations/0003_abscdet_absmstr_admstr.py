# Generated by Django 2.1.15 on 2022-03-08 08:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('qad_ee', '0002_auto_20220307_1609'),
    ]

    operations = [
        migrations.CreateModel(
            name='AbscDet',
            fields=[
                ('prrowid', models.CharField(max_length=36, primary_key=True, serialize=False)),
                ('absc_abs_id', models.CharField(blank=True, max_length=30, null=True)),
                ('absc_seq', models.IntegerField(blank=True, null=True)),
                ('absc_carrier', models.CharField(blank=True, max_length=80, null=True)),
                ('absc_user1', models.CharField(blank=True, max_length=80, null=True)),
                ('absc_user2', models.CharField(blank=True, max_length=80, null=True)),
                ('absc_qadc01', models.CharField(blank=True, db_column='absc__qadc01', max_length=80, null=True)),
                ('absc_domain', models.CharField(blank=True, max_length=8, null=True)),
                ('oid_absc_det', models.DecimalField(blank=True, decimal_places=10, max_digits=38, null=True)),
                ('pro2srcpdb', models.CharField(blank=True, db_column='Pro2SrcPDB', max_length=12, null=True)),
                ('pro2created', models.DateTimeField(blank=True, null=True)),
                ('pro2modified', models.DateTimeField(blank=True, null=True)),
            ],
            options={
                'db_table': 'absc_det',
            },
        ),
        migrations.CreateModel(
            name='AbsMstr',
            fields=[
                ('prrowid', models.CharField(max_length=36, primary_key=True, serialize=False)),
                ('abs_shipfrom', models.CharField(blank=True, max_length=80, null=True)),
                ('abs_id', models.TextField(blank=True, null=True)),
                ('abs_par_id', models.CharField(blank=True, max_length=80, null=True)),
                ('abs_shipto', models.CharField(blank=True, max_length=80, null=True)),
                ('abs_type', models.CharField(blank=True, max_length=30, null=True)),
                ('abs_status', models.CharField(blank=True, max_length=80, null=True)),
                ('abs_timezone', models.CharField(blank=True, max_length=30, null=True)),
                ('abs_shp_date', models.DateTimeField(blank=True, null=True)),
                ('abs_shp_time', models.IntegerField(blank=True, null=True)),
                ('abs_arr_date', models.DateTimeField(blank=True, null=True)),
                ('abs_arr_time', models.IntegerField(blank=True, null=True)),
                ('abs_crt_date', models.DateTimeField(blank=True, null=True)),
                ('abs_crt_time', models.IntegerField(blank=True, null=True)),
                ('abs_apr_date', models.DateTimeField(blank=True, null=True)),
                ('abs_apr_time', models.IntegerField(blank=True, null=True)),
                ('abs_apr_userid', models.CharField(blank=True, max_length=80, null=True)),
                ('abs_gwt', models.DecimalField(blank=True, decimal_places=10, max_digits=25, null=True)),
                ('abs_nwt', models.DecimalField(blank=True, decimal_places=10, max_digits=25, null=True)),
                ('abs_vol', models.DecimalField(blank=True, decimal_places=10, max_digits=38, null=True)),
                ('abs_wt_um', models.CharField(blank=True, max_length=30, null=True)),
                ('abs_vol_um', models.CharField(blank=True, max_length=30, null=True)),
                ('abs_dim_um', models.CharField(blank=True, max_length=30, null=True)),
                ('abs_fr_class', models.CharField(blank=True, max_length=80, null=True)),
                ('abs_est_fcst', models.DecimalField(blank=True, decimal_places=10, max_digits=38, null=True)),
                ('abs_act_fcst', models.DecimalField(blank=True, decimal_places=10, max_digits=38, null=True)),
                ('abs_fr_curr', models.CharField(blank=True, max_length=30, null=True)),
                ('abs_doc_data_1', models.TextField(blank=True, db_column='abs_doc_data##1', null=True)),
                ('abs_doc_data_2', models.TextField(blank=True, db_column='abs_doc_data##2', null=True)),
                ('abs_doc_data_3', models.TextField(blank=True, db_column='abs_doc_data##3', null=True)),
                ('abs_doc_data_4', models.TextField(blank=True, db_column='abs_doc_data##4', null=True)),
                ('abs_doc_data_5', models.TextField(blank=True, db_column='abs_doc_data##5', null=True)),
                ('abs_dataset', models.CharField(blank=True, max_length=30, null=True)),
                ('abs_order', models.CharField(blank=True, max_length=80, null=True)),
                ('abs_line', models.CharField(blank=True, max_length=80, null=True)),
                ('abs_inv_nbr', models.CharField(blank=True, max_length=80, null=True)),
                ('abs_item', models.CharField(blank=True, max_length=30, null=True)),
                ('abs_lotser', models.CharField(blank=True, max_length=30, null=True)),
                ('abs_ref', models.CharField(blank=True, max_length=80, null=True)),
                ('abs_qty', models.DecimalField(blank=True, decimal_places=10, max_digits=38, null=True)),
                ('abs_ship_qty', models.DecimalField(blank=True, decimal_places=10, max_digits=38, null=True)),
                ('abs_cum_qty', models.DecimalField(blank=True, decimal_places=10, max_digits=38, null=True)),
                ('abs_site', models.CharField(blank=True, max_length=80, null=True)),
                ('abs_loc', models.CharField(blank=True, max_length=80, null=True)),
                ('abs_cust_ref', models.CharField(blank=True, max_length=30, null=True)),
                ('abs_cmtindx', models.IntegerField(blank=True, null=True)),
                ('abs_chr01', models.CharField(blank=True, db_column='abs__chr01', max_length=80, null=True)),
                ('abs_chr02', models.CharField(blank=True, db_column='abs__chr02', max_length=80, null=True)),
                ('abs_chr03', models.CharField(blank=True, db_column='abs__chr03', max_length=80, null=True)),
                ('abs_chr04', models.CharField(blank=True, db_column='abs__chr04', max_length=80, null=True)),
                ('abs_chr05', models.CharField(blank=True, db_column='abs__chr05', max_length=80, null=True)),
                ('abs_chr06', models.CharField(blank=True, db_column='abs__chr06', max_length=80, null=True)),
                ('abs_chr07', models.CharField(blank=True, db_column='abs__chr07', max_length=80, null=True)),
                ('abs_chr08', models.CharField(blank=True, db_column='abs__chr08', max_length=80, null=True)),
                ('abs_chr09', models.CharField(blank=True, db_column='abs__chr09', max_length=80, null=True)),
                ('abs_chr10', models.CharField(blank=True, db_column='abs__chr10', max_length=80, null=True)),
                ('abs_dec01', models.DecimalField(blank=True, db_column='abs__dec01', decimal_places=10, max_digits=38, null=True)),
                ('abs_dec02', models.DecimalField(blank=True, db_column='abs__dec02', decimal_places=10, max_digits=38, null=True)),
                ('abs_dec03', models.DecimalField(blank=True, db_column='abs__dec03', decimal_places=10, max_digits=38, null=True)),
                ('abs_dec04', models.DecimalField(blank=True, db_column='abs__dec04', decimal_places=10, max_digits=38, null=True)),
                ('abs_dec05', models.DecimalField(blank=True, db_column='abs__dec05', decimal_places=10, max_digits=38, null=True)),
                ('abs_dec06', models.DecimalField(blank=True, db_column='abs__dec06', decimal_places=10, max_digits=38, null=True)),
                ('abs_dec07', models.DecimalField(blank=True, db_column='abs__dec07', decimal_places=10, max_digits=38, null=True)),
                ('abs_dec08', models.DecimalField(blank=True, db_column='abs__dec08', decimal_places=10, max_digits=38, null=True)),
                ('abs_dec09', models.DecimalField(blank=True, db_column='abs__dec09', decimal_places=10, max_digits=38, null=True)),
                ('abs_dec10', models.DecimalField(blank=True, db_column='abs__dec10', decimal_places=10, max_digits=38, null=True)),
                ('abs_qad01', models.CharField(blank=True, db_column='abs__qad01', max_length=230, null=True)),
                ('abs_qad02', models.CharField(blank=True, db_column='abs__qad02', max_length=80, null=True)),
                ('abs_qad03', models.CharField(blank=True, db_column='abs__qad03', max_length=80, null=True)),
                ('abs_qad04', models.CharField(blank=True, db_column='abs__qad04', max_length=80, null=True)),
                ('abs_qad05', models.CharField(blank=True, db_column='abs__qad05', max_length=80, null=True)),
                ('abs_qad06', models.CharField(blank=True, db_column='abs__qad06', max_length=80, null=True)),
                ('abs_qad07', models.CharField(blank=True, db_column='abs__qad07', max_length=80, null=True)),
                ('abs_qad08', models.CharField(blank=True, db_column='abs__qad08', max_length=80, null=True)),
                ('abs_qad09', models.CharField(blank=True, db_column='abs__qad09', max_length=80, null=True)),
                ('abs_qad10', models.CharField(blank=True, db_column='abs__qad10', max_length=80, null=True)),
                ('abs_user1', models.CharField(blank=True, max_length=80, null=True)),
                ('abs_user2', models.CharField(blank=True, max_length=80, null=True)),
                ('abs_master_id', models.CharField(blank=True, max_length=80, null=True)),
                ('abs_inv_mov', models.CharField(blank=True, max_length=80, null=True)),
                ('abs_nr_id', models.CharField(blank=True, max_length=80, null=True)),
                ('abs_format', models.CharField(blank=True, max_length=80, null=True)),
                ('abs_cons_ship', models.CharField(blank=True, max_length=80, null=True)),
                ('abs_qadc01', models.CharField(blank=True, db_column='abs__qadc01', max_length=80, null=True)),
                ('abs_lang', models.CharField(blank=True, max_length=30, null=True)),
                ('abs_canceled', models.BooleanField(blank=True, null=True)),
                ('abs_qadd01', models.DecimalField(blank=True, db_column='abs__qadd01', decimal_places=10, max_digits=38, null=True)),
                ('abs_trl_cmtindx', models.IntegerField(blank=True, null=True)),
                ('abs_eff_date', models.DateTimeField(blank=True, null=True)),
                ('abs_cancel_date', models.DateTimeField(blank=True, null=True)),
                ('abs_preship_nr_id', models.CharField(blank=True, max_length=80, null=True)),
                ('abs_preship_id', models.CharField(blank=True, max_length=30, null=True)),
                ('abs_fa_lot', models.CharField(blank=True, max_length=80, null=True)),
                ('abs_asn_crt_date', models.DateTimeField(blank=True, null=True)),
                ('abs_asn_crt_time', models.IntegerField(blank=True, null=True)),
                ('abs_export_batch', models.IntegerField(blank=True, null=True)),
                ('abs_export_date', models.DateTimeField(blank=True, null=True)),
                ('abs_export_time', models.IntegerField(blank=True, null=True)),
                ('abs_charge_type', models.CharField(blank=True, max_length=80, null=True)),
                ('abs_price', models.DecimalField(blank=True, decimal_places=10, max_digits=38, null=True)),
                ('abs_desc', models.CharField(blank=True, max_length=80, null=True)),
                ('abs_master_shipfrom', models.CharField(blank=True, max_length=80, null=True)),
                ('abs_domain', models.CharField(blank=True, max_length=8, null=True)),
                ('oid_abs_mstr', models.DecimalField(blank=True, decimal_places=10, max_digits=38, null=True)),
                ('abs_consigned_return', models.BooleanField(blank=True, null=True)),
                ('abs_vend_lot', models.CharField(blank=True, max_length=30, null=True)),
                ('abs_rcpt_qty', models.DecimalField(blank=True, decimal_places=10, max_digits=20, null=True)),
                ('abs_routing', models.CharField(blank=True, max_length=30, null=True)),
                ('abs_bom_code', models.CharField(blank=True, max_length=30, null=True)),
                ('abs_production_line', models.CharField(blank=True, max_length=80, null=True)),
                ('abs_complete', models.BooleanField(blank=True, null=True)),
                ('abs_scrap_qty', models.DecimalField(blank=True, decimal_places=10, max_digits=20, null=True)),
                ('abs_combined_invoice', models.BooleanField(blank=True, null=True)),
                ('abs_act_qty', models.DecimalField(blank=True, decimal_places=10, max_digits=38, null=True)),
                ('abs_bulk_qty', models.DecimalField(blank=True, decimal_places=10, max_digits=38, null=True)),
                ('abs_tax_in', models.BooleanField(blank=True, null=True)),
                ('abs_tax_env', models.CharField(blank=True, max_length=30, null=True)),
                ('abs_tax_usage', models.CharField(blank=True, max_length=80, null=True)),
                ('abs_taxc', models.CharField(blank=True, max_length=30, null=True)),
                ('abs_taxable', models.BooleanField(blank=True, null=True)),
                ('abs_acct', models.CharField(blank=True, max_length=20, null=True)),
                ('abs_sub', models.CharField(blank=True, max_length=20, null=True)),
                ('abs_cc', models.CharField(blank=True, max_length=20, null=True)),
                ('abs_proj', models.CharField(blank=True, max_length=20, null=True)),
                ('abs_qadc02', models.CharField(blank=True, db_column='abs__qadc02', max_length=80, null=True)),
                ('abs_qadc03', models.CharField(blank=True, db_column='abs__qadc03', max_length=80, null=True)),
                ('abs_qadi01', models.IntegerField(blank=True, db_column='abs__qadi01', null=True)),
                ('abs_qadl01', models.BooleanField(blank=True, db_column='abs__qadl01', null=True)),
                ('abs_qadt01', models.DateTimeField(blank=True, db_column='abs__qadt01', null=True)),
                ('abs_ship_type', models.CharField(blank=True, max_length=30, null=True)),
                ('oid_lgdd_det', models.DecimalField(blank=True, decimal_places=10, max_digits=38, null=True)),
                ('pro2srcpdb', models.CharField(blank=True, db_column='Pro2SrcPDB', max_length=12, null=True)),
                ('pro2created', models.DateTimeField(blank=True, null=True)),
                ('pro2modified', models.DateTimeField(blank=True, null=True)),
            ],
            options={
                'db_table': 'abs_mstr',
            },
        ),
        migrations.CreateModel(
            name='AdMstr',
            fields=[
                ('prrowid', models.CharField(max_length=36, primary_key=True, serialize=False)),
                ('ad_addr', models.CharField(blank=True, max_length=80, null=True)),
                ('ad_name', models.CharField(blank=True, max_length=80, null=True)),
                ('ad_line1', models.CharField(blank=True, max_length=36, null=True)),
                ('ad_line2', models.CharField(blank=True, max_length=36, null=True)),
                ('ad_city', models.CharField(blank=True, max_length=30, null=True)),
                ('ad_state', models.CharField(blank=True, max_length=30, null=True)),
                ('ad_zip', models.CharField(blank=True, max_length=30, null=True)),
                ('ad_type', models.CharField(blank=True, max_length=80, null=True)),
                ('ad_attn', models.CharField(blank=True, max_length=30, null=True)),
                ('ad_phone', models.CharField(blank=True, max_length=30, null=True)),
                ('ad_ext', models.CharField(blank=True, max_length=30, null=True)),
                ('ad_ref', models.CharField(blank=True, max_length=80, null=True)),
                ('ad_sort', models.CharField(blank=True, max_length=80, null=True)),
                ('ad_country', models.CharField(blank=True, max_length=30, null=True)),
                ('ad_attn2', models.CharField(blank=True, max_length=30, null=True)),
                ('ad_phone2', models.CharField(blank=True, max_length=30, null=True)),
                ('ad_ext2', models.CharField(blank=True, max_length=30, null=True)),
                ('ad_fax', models.CharField(blank=True, max_length=30, null=True)),
                ('ad_fax2', models.CharField(blank=True, max_length=30, null=True)),
                ('ad_line3', models.CharField(blank=True, max_length=36, null=True)),
                ('ad_user1', models.CharField(blank=True, max_length=80, null=True)),
                ('ad_user2', models.CharField(blank=True, max_length=80, null=True)),
                ('ad_lang', models.CharField(blank=True, max_length=30, null=True)),
                ('ad_pst_id', models.CharField(blank=True, max_length=30, null=True)),
                ('ad_date', models.DateTimeField(blank=True, null=True)),
                ('ad_county', models.CharField(blank=True, max_length=30, null=True)),
                ('ad_temp', models.BooleanField(blank=True, null=True)),
                ('ad_bk_acct1', models.CharField(blank=True, max_length=30, null=True)),
                ('ad_bk_acct2', models.CharField(blank=True, max_length=30, null=True)),
                ('ad_format', models.IntegerField(blank=True, null=True)),
                ('ad_vat_reg', models.CharField(blank=True, max_length=30, null=True)),
                ('ad_coc_reg', models.CharField(blank=True, max_length=80, null=True)),
                ('ad_gst_id', models.CharField(blank=True, max_length=30, null=True)),
                ('ad_tax_type', models.CharField(blank=True, max_length=30, null=True)),
                ('ad_taxc', models.CharField(blank=True, max_length=30, null=True)),
                ('ad_taxable', models.BooleanField(blank=True, null=True)),
                ('ad_tax_in', models.BooleanField(blank=True, null=True)),
                ('ad_edi_tpid', models.CharField(blank=True, max_length=30, null=True)),
                ('ad_timezone', models.CharField(blank=True, max_length=80, null=True)),
                ('ad_mod_date', models.DateTimeField(blank=True, null=True)),
                ('ad_userid', models.CharField(blank=True, max_length=80, null=True)),
                ('ad_edi_id', models.CharField(blank=True, max_length=30, null=True)),
                ('ad_edi_ctrl_1', models.TextField(blank=True, db_column='ad_edi_ctrl##1', null=True)),
                ('ad_edi_ctrl_2', models.TextField(blank=True, db_column='ad_edi_ctrl##2', null=True)),
                ('ad_edi_ctrl_3', models.TextField(blank=True, db_column='ad_edi_ctrl##3', null=True)),
                ('ad_edi_ctrl_4', models.TextField(blank=True, db_column='ad_edi_ctrl##4', null=True)),
                ('ad_edi_ctrl_5', models.TextField(blank=True, db_column='ad_edi_ctrl##5', null=True)),
                ('ad_conrep', models.CharField(blank=True, max_length=30, null=True)),
                ('ad_barlbl_prt', models.TextField(blank=True, null=True)),
                ('ad_barlbl_val', models.CharField(blank=True, max_length=30, null=True)),
                ('ad_calendar', models.CharField(blank=True, max_length=80, null=True)),
                ('ad_edi_std', models.CharField(blank=True, max_length=80, null=True)),
                ('ad_edi_level', models.CharField(blank=True, max_length=80, null=True)),
                ('ad_qad01', models.CharField(blank=True, db_column='ad__qad01', max_length=80, null=True)),
                ('ad_qad02', models.CharField(blank=True, db_column='ad__qad02', max_length=80, null=True)),
                ('ad_qad03', models.CharField(blank=True, db_column='ad__qad03', max_length=80, null=True)),
                ('ad_qad04', models.CharField(blank=True, db_column='ad__qad04', max_length=80, null=True)),
                ('ad_qad05', models.CharField(blank=True, db_column='ad__qad05', max_length=80, null=True)),
                ('ad_chr01', models.CharField(blank=True, db_column='ad__chr01', max_length=80, null=True)),
                ('ad_chr02', models.CharField(blank=True, db_column='ad__chr02', max_length=80, null=True)),
                ('ad_chr03', models.CharField(blank=True, db_column='ad__chr03', max_length=80, null=True)),
                ('ad_chr04', models.CharField(blank=True, db_column='ad__chr04', max_length=80, null=True)),
                ('ad_chr05', models.CharField(blank=True, db_column='ad__chr05', max_length=80, null=True)),
                ('ad_tp_loc_code', models.CharField(blank=True, max_length=30, null=True)),
                ('ad_ctry', models.CharField(blank=True, max_length=30, null=True)),
                ('ad_tax_zone', models.CharField(blank=True, max_length=30, null=True)),
                ('ad_tax_usage', models.CharField(blank=True, max_length=80, null=True)),
                ('ad_misc1_id', models.CharField(blank=True, max_length=30, null=True)),
                ('ad_misc2_id', models.CharField(blank=True, max_length=30, null=True)),
                ('ad_misc3_id', models.CharField(blank=True, max_length=30, null=True)),
                ('ad_wk_offset', models.IntegerField(blank=True, null=True)),
                ('ad_inv_mthd', models.CharField(blank=True, max_length=30, null=True)),
                ('ad_sch_mthd', models.CharField(blank=True, max_length=30, null=True)),
                ('ad_po_mthd', models.CharField(blank=True, max_length=30, null=True)),
                ('ad_asn_data', models.TextField(blank=True, null=True)),
                ('ad_intr_division', models.CharField(blank=True, max_length=30, null=True)),
                ('ad_tax_report', models.BooleanField(blank=True, null=True)),
                ('ad_name_control', models.CharField(blank=True, max_length=30, null=True)),
                ('ad_last_file', models.BooleanField(blank=True, null=True)),
                ('ad_domain', models.CharField(blank=True, max_length=8, null=True)),
                ('oid_ad_mstr', models.DecimalField(blank=True, decimal_places=10, max_digits=38, null=True)),
                ('ad_email', models.CharField(blank=True, max_length=48, null=True)),
                ('ad_email2', models.CharField(blank=True, max_length=48, null=True)),
                ('ad_bus_relation', models.CharField(blank=True, max_length=20, null=True)),
                ('ad_priority', models.CharField(blank=True, max_length=16, null=True)),
                ('ad_route', models.CharField(blank=True, max_length=16, null=True)),
                ('ad_loadseq', models.CharField(blank=True, max_length=16, null=True)),
                ('ad_pick_by_date', models.BooleanField(blank=True, null=True)),
                ('ad_profile', models.CharField(blank=True, max_length=16, null=True)),
                ('ad_address_id', models.BigIntegerField(blank=True, null=True)),
                ('ad_tax_in_city', models.BooleanField(blank=True, null=True)),
                ('ad_ns_pr_list', models.CharField(blank=True, max_length=16, null=True)),
                ('ad_alt_um', models.CharField(blank=True, max_length=4, null=True)),
                ('ad_city_code', models.CharField(blank=True, max_length=20, null=True)),
                ('pro2srcpdb', models.CharField(blank=True, db_column='Pro2SrcPDB', max_length=12, null=True)),
                ('pro2created', models.DateTimeField(blank=True, null=True)),
                ('pro2modified', models.DateTimeField(blank=True, null=True)),
            ],
            options={
                'db_table': 'ad_mstr',
            },
        ),
    ]
