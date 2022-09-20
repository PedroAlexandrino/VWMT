# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class AbsMstr(models.Model):
    prrowid = models.CharField(primary_key=True, max_length=36)
    abs_shipfrom = models.CharField(max_length=80, blank=True, null=True)
    abs_id = models.TextField(blank=True, null=True)
    abs_par_id = models.CharField(max_length=80, blank=True, null=True)
    abs_shipto = models.CharField(max_length=80, blank=True, null=True)
    abs_type = models.CharField(max_length=30, blank=True, null=True)
    abs_status = models.CharField(max_length=80, blank=True, null=True)
    abs_timezone = models.CharField(max_length=30, blank=True, null=True)
    abs_shp_date = models.DateTimeField(blank=True, null=True)
    abs_shp_time = models.IntegerField(blank=True, null=True)
    abs_arr_date = models.DateTimeField(blank=True, null=True)
    abs_arr_time = models.IntegerField(blank=True, null=True)
    abs_crt_date = models.DateTimeField(blank=True, null=True)
    abs_crt_time = models.IntegerField(blank=True, null=True)
    abs_apr_date = models.DateTimeField(blank=True, null=True)
    abs_apr_time = models.IntegerField(blank=True, null=True)
    abs_apr_userid = models.CharField(max_length=80, blank=True, null=True)
    abs_gwt = models.DecimalField(
        max_digits=25, decimal_places=10, blank=True, null=True
    )
    abs_nwt = models.DecimalField(
        max_digits=25, decimal_places=10, blank=True, null=True
    )
    abs_vol = models.DecimalField(
        max_digits=38, decimal_places=10, blank=True, null=True
    )
    abs_wt_um = models.CharField(max_length=30, blank=True, null=True)
    abs_vol_um = models.CharField(max_length=30, blank=True, null=True)
    abs_dim_um = models.CharField(max_length=30, blank=True, null=True)
    abs_fr_class = models.CharField(max_length=80, blank=True, null=True)
    abs_est_fcst = models.DecimalField(
        max_digits=38, decimal_places=10, blank=True, null=True
    )
    abs_act_fcst = models.DecimalField(
        max_digits=38, decimal_places=10, blank=True, null=True
    )
    abs_fr_curr = models.CharField(max_length=30, blank=True, null=True)
    abs_doc_data_1 = models.TextField(
        db_column="abs_doc_data##1", blank=True, null=True
    )  # Field renamed to remove unsuitable characters.
    abs_doc_data_2 = models.TextField(
        db_column="abs_doc_data##2", blank=True, null=True
    )  # Field renamed to remove unsuitable characters.
    abs_doc_data_3 = models.TextField(
        db_column="abs_doc_data##3", blank=True, null=True
    )  # Field renamed to remove unsuitable characters.
    abs_doc_data_4 = models.TextField(
        db_column="abs_doc_data##4", blank=True, null=True
    )  # Field renamed to remove unsuitable characters.
    abs_doc_data_5 = models.TextField(
        db_column="abs_doc_data##5", blank=True, null=True
    )  # Field renamed to remove unsuitable characters.
    abs_dataset = models.CharField(max_length=30, blank=True, null=True)
    abs_order = models.CharField(max_length=80, blank=True, null=True)
    abs_line = models.CharField(max_length=80, blank=True, null=True)
    abs_inv_nbr = models.CharField(max_length=80, blank=True, null=True)
    abs_item = models.CharField(max_length=30, blank=True, null=True)
    abs_lotser = models.CharField(max_length=30, blank=True, null=True)
    abs_ref = models.CharField(max_length=80, blank=True, null=True)
    abs_qty = models.DecimalField(
        max_digits=38, decimal_places=10, blank=True, null=True
    )
    abs_ship_qty = models.DecimalField(
        max_digits=38, decimal_places=10, blank=True, null=True
    )
    abs_cum_qty = models.DecimalField(
        max_digits=38, decimal_places=10, blank=True, null=True
    )
    abs_site = models.CharField(max_length=80, blank=True, null=True)
    abs_loc = models.CharField(max_length=80, blank=True, null=True)
    abs_cust_ref = models.CharField(max_length=30, blank=True, null=True)
    abs_cmtindx = models.IntegerField(blank=True, null=True)
    abs_chr01 = models.CharField(
        db_column="abs__chr01", max_length=80, blank=True, null=True
    )  # Field renamed because it contained more than one '_' in a row.
    abs_chr02 = models.CharField(
        db_column="abs__chr02", max_length=80, blank=True, null=True
    )  # Field renamed because it contained more than one '_' in a row.
    abs_chr03 = models.CharField(
        db_column="abs__chr03", max_length=80, blank=True, null=True
    )  # Field renamed because it contained more than one '_' in a row.
    abs_chr04 = models.CharField(
        db_column="abs__chr04", max_length=80, blank=True, null=True
    )  # Field renamed because it contained more than one '_' in a row.
    abs_chr05 = models.CharField(
        db_column="abs__chr05", max_length=80, blank=True, null=True
    )  # Field renamed because it contained more than one '_' in a row.
    abs_chr06 = models.CharField(
        db_column="abs__chr06", max_length=80, blank=True, null=True
    )  # Field renamed because it contained more than one '_' in a row.
    abs_chr07 = models.CharField(
        db_column="abs__chr07", max_length=80, blank=True, null=True
    )  # Field renamed because it contained more than one '_' in a row.
    abs_chr08 = models.CharField(
        db_column="abs__chr08", max_length=80, blank=True, null=True
    )  # Field renamed because it contained more than one '_' in a row.
    abs_chr09 = models.CharField(
        db_column="abs__chr09", max_length=80, blank=True, null=True
    )  # Field renamed because it contained more than one '_' in a row.
    abs_chr10 = models.CharField(
        db_column="abs__chr10", max_length=80, blank=True, null=True
    )  # Field renamed because it contained more than one '_' in a row.
    abs_dec01 = models.DecimalField(
        db_column="abs__dec01", max_digits=38, decimal_places=10, blank=True, null=True
    )  # Field renamed because it contained more than one '_' in a row.
    abs_dec02 = models.DecimalField(
        db_column="abs__dec02", max_digits=38, decimal_places=10, blank=True, null=True
    )  # Field renamed because it contained more than one '_' in a row.
    abs_dec03 = models.DecimalField(
        db_column="abs__dec03", max_digits=38, decimal_places=10, blank=True, null=True
    )  # Field renamed because it contained more than one '_' in a row.
    abs_dec04 = models.DecimalField(
        db_column="abs__dec04", max_digits=38, decimal_places=10, blank=True, null=True
    )  # Field renamed because it contained more than one '_' in a row.
    abs_dec05 = models.DecimalField(
        db_column="abs__dec05", max_digits=38, decimal_places=10, blank=True, null=True
    )  # Field renamed because it contained more than one '_' in a row.
    abs_dec06 = models.DecimalField(
        db_column="abs__dec06", max_digits=38, decimal_places=10, blank=True, null=True
    )  # Field renamed because it contained more than one '_' in a row.
    abs_dec07 = models.DecimalField(
        db_column="abs__dec07", max_digits=38, decimal_places=10, blank=True, null=True
    )  # Field renamed because it contained more than one '_' in a row.
    abs_dec08 = models.DecimalField(
        db_column="abs__dec08", max_digits=38, decimal_places=10, blank=True, null=True
    )  # Field renamed because it contained more than one '_' in a row.
    abs_dec09 = models.DecimalField(
        db_column="abs__dec09", max_digits=38, decimal_places=10, blank=True, null=True
    )  # Field renamed because it contained more than one '_' in a row.
    abs_dec10 = models.DecimalField(
        db_column="abs__dec10", max_digits=38, decimal_places=10, blank=True, null=True
    )  # Field renamed because it contained more than one '_' in a row.
    abs_qad01 = models.CharField(
        db_column="abs__qad01", max_length=230, blank=True, null=True
    )  # Field renamed because it contained more than one '_' in a row.
    abs_qad02 = models.CharField(
        db_column="abs__qad02", max_length=80, blank=True, null=True
    )  # Field renamed because it contained more than one '_' in a row.
    abs_qad03 = models.CharField(
        db_column="abs__qad03", max_length=80, blank=True, null=True
    )  # Field renamed because it contained more than one '_' in a row.
    abs_qad04 = models.CharField(
        db_column="abs__qad04", max_length=80, blank=True, null=True
    )  # Field renamed because it contained more than one '_' in a row.
    abs_qad05 = models.CharField(
        db_column="abs__qad05", max_length=80, blank=True, null=True
    )  # Field renamed because it contained more than one '_' in a row.
    abs_qad06 = models.CharField(
        db_column="abs__qad06", max_length=80, blank=True, null=True
    )  # Field renamed because it contained more than one '_' in a row.
    abs_qad07 = models.CharField(
        db_column="abs__qad07", max_length=80, blank=True, null=True
    )  # Field renamed because it contained more than one '_' in a row.
    abs_qad08 = models.CharField(
        db_column="abs__qad08", max_length=80, blank=True, null=True
    )  # Field renamed because it contained more than one '_' in a row.
    abs_qad09 = models.CharField(
        db_column="abs__qad09", max_length=80, blank=True, null=True
    )  # Field renamed because it contained more than one '_' in a row.
    abs_qad10 = models.CharField(
        db_column="abs__qad10", max_length=80, blank=True, null=True
    )  # Field renamed because it contained more than one '_' in a row.
    abs_user1 = models.CharField(max_length=80, blank=True, null=True)
    abs_user2 = models.CharField(max_length=80, blank=True, null=True)
    abs_master_id = models.CharField(max_length=80, blank=True, null=True)
    abs_inv_mov = models.CharField(max_length=80, blank=True, null=True)
    abs_nr_id = models.CharField(max_length=80, blank=True, null=True)
    abs_format = models.CharField(max_length=80, blank=True, null=True)
    abs_cons_ship = models.CharField(max_length=80, blank=True, null=True)
    abs_qadc01 = models.CharField(
        db_column="abs__qadc01", max_length=80, blank=True, null=True
    )  # Field renamed because it contained more than one '_' in a row.
    abs_lang = models.CharField(max_length=30, blank=True, null=True)
    abs_canceled = models.BooleanField(blank=True, null=True)
    abs_qadd01 = models.DecimalField(
        db_column="abs__qadd01", max_digits=38, decimal_places=10, blank=True, null=True
    )  # Field renamed because it contained more than one '_' in a row.
    abs_trl_cmtindx = models.IntegerField(blank=True, null=True)
    abs_eff_date = models.DateTimeField(blank=True, null=True)
    abs_cancel_date = models.DateTimeField(blank=True, null=True)
    abs_preship_nr_id = models.CharField(max_length=80, blank=True, null=True)
    abs_preship_id = models.CharField(max_length=30, blank=True, null=True)
    abs_fa_lot = models.CharField(max_length=80, blank=True, null=True)
    abs_asn_crt_date = models.DateTimeField(blank=True, null=True)
    abs_asn_crt_time = models.IntegerField(blank=True, null=True)
    abs_export_batch = models.IntegerField(blank=True, null=True)
    abs_export_date = models.DateTimeField(blank=True, null=True)
    abs_export_time = models.IntegerField(blank=True, null=True)
    abs_charge_type = models.CharField(max_length=80, blank=True, null=True)
    abs_price = models.DecimalField(
        max_digits=38, decimal_places=10, blank=True, null=True
    )
    abs_desc = models.CharField(max_length=80, blank=True, null=True)
    abs_master_shipfrom = models.CharField(max_length=80, blank=True, null=True)
    abs_domain = models.CharField(max_length=8, blank=True, null=True)
    oid_abs_mstr = models.DecimalField(
        max_digits=38, decimal_places=10, blank=True, null=True
    )
    abs_consigned_return = models.BooleanField(blank=True, null=True)
    abs_vend_lot = models.CharField(max_length=30, blank=True, null=True)
    abs_rcpt_qty = models.DecimalField(
        max_digits=20, decimal_places=10, blank=True, null=True
    )
    abs_routing = models.CharField(max_length=30, blank=True, null=True)
    abs_bom_code = models.CharField(max_length=30, blank=True, null=True)
    abs_production_line = models.CharField(max_length=80, blank=True, null=True)
    abs_complete = models.BooleanField(blank=True, null=True)
    abs_scrap_qty = models.DecimalField(
        max_digits=20, decimal_places=10, blank=True, null=True
    )
    abs_combined_invoice = models.BooleanField(blank=True, null=True)
    abs_act_qty = models.DecimalField(
        max_digits=38, decimal_places=10, blank=True, null=True
    )
    abs_bulk_qty = models.DecimalField(
        max_digits=38, decimal_places=10, blank=True, null=True
    )
    abs_tax_in = models.BooleanField(blank=True, null=True)
    abs_tax_env = models.CharField(max_length=30, blank=True, null=True)
    abs_tax_usage = models.CharField(max_length=80, blank=True, null=True)
    abs_taxc = models.CharField(max_length=30, blank=True, null=True)
    abs_taxable = models.BooleanField(blank=True, null=True)
    abs_acct = models.CharField(max_length=20, blank=True, null=True)
    abs_sub = models.CharField(max_length=20, blank=True, null=True)
    abs_cc = models.CharField(max_length=20, blank=True, null=True)
    abs_proj = models.CharField(max_length=20, blank=True, null=True)
    abs_qadc02 = models.CharField(
        db_column="abs__qadc02", max_length=80, blank=True, null=True
    )  # Field renamed because it contained more than one '_' in a row.
    abs_qadc03 = models.CharField(
        db_column="abs__qadc03", max_length=80, blank=True, null=True
    )  # Field renamed because it contained more than one '_' in a row.
    abs_qadi01 = models.IntegerField(
        db_column="abs__qadi01", blank=True, null=True
    )  # Field renamed because it contained more than one '_' in a row.
    abs_qadl01 = models.BooleanField(
        db_column="abs__qadl01", blank=True, null=True
    )  # Field renamed because it contained more than one '_' in a row.
    abs_qadt01 = models.DateTimeField(
        db_column="abs__qadt01", blank=True, null=True
    )  # Field renamed because it contained more than one '_' in a row.
    abs_ship_type = models.CharField(max_length=30, blank=True, null=True)
    oid_lgdd_det = models.DecimalField(
        max_digits=38, decimal_places=10, blank=True, null=True
    )
    pro2srcpdb = models.CharField(
        db_column="Pro2SrcPDB", max_length=12, blank=True, null=True
    )  # Field name made lowercase.
    pro2created = models.DateTimeField(blank=True, null=True)
    pro2modified = models.DateTimeField(blank=True, null=True)

    class Meta:
        db_table = "abs_mstr"


class AdMstr(models.Model):
    prrowid = models.CharField(primary_key=True, max_length=36)
    ad_addr = models.CharField(max_length=80, blank=True, null=True)
    ad_name = models.CharField(max_length=80, blank=True, null=True)
    ad_line1 = models.CharField(max_length=36, blank=True, null=True)
    ad_line2 = models.CharField(max_length=36, blank=True, null=True)
    ad_city = models.CharField(max_length=30, blank=True, null=True)
    ad_state = models.CharField(max_length=30, blank=True, null=True)
    ad_zip = models.CharField(max_length=30, blank=True, null=True)
    ad_type = models.CharField(max_length=80, blank=True, null=True)
    ad_attn = models.CharField(max_length=30, blank=True, null=True)
    ad_phone = models.CharField(max_length=30, blank=True, null=True)
    ad_ext = models.CharField(max_length=30, blank=True, null=True)
    ad_ref = models.CharField(max_length=80, blank=True, null=True)
    ad_sort = models.CharField(max_length=80, blank=True, null=True)
    ad_country = models.CharField(max_length=30, blank=True, null=True)
    ad_attn2 = models.CharField(max_length=30, blank=True, null=True)
    ad_phone2 = models.CharField(max_length=30, blank=True, null=True)
    ad_ext2 = models.CharField(max_length=30, blank=True, null=True)
    ad_fax = models.CharField(max_length=30, blank=True, null=True)
    ad_fax2 = models.CharField(max_length=30, blank=True, null=True)
    ad_line3 = models.CharField(max_length=36, blank=True, null=True)
    ad_user1 = models.CharField(max_length=80, blank=True, null=True)
    ad_user2 = models.CharField(max_length=80, blank=True, null=True)
    ad_lang = models.CharField(max_length=30, blank=True, null=True)
    ad_pst_id = models.CharField(max_length=30, blank=True, null=True)
    ad_date = models.DateTimeField(blank=True, null=True)
    ad_county = models.CharField(max_length=30, blank=True, null=True)
    ad_temp = models.BooleanField(blank=True, null=True)
    ad_bk_acct1 = models.CharField(max_length=30, blank=True, null=True)
    ad_bk_acct2 = models.CharField(max_length=30, blank=True, null=True)
    ad_format = models.IntegerField(blank=True, null=True)
    ad_vat_reg = models.CharField(max_length=30, blank=True, null=True)
    ad_coc_reg = models.CharField(max_length=80, blank=True, null=True)
    ad_gst_id = models.CharField(max_length=30, blank=True, null=True)
    ad_tax_type = models.CharField(max_length=30, blank=True, null=True)
    ad_taxc = models.CharField(max_length=30, blank=True, null=True)
    ad_taxable = models.BooleanField(blank=True, null=True)
    ad_tax_in = models.BooleanField(blank=True, null=True)
    ad_edi_tpid = models.CharField(max_length=30, blank=True, null=True)
    ad_timezone = models.CharField(max_length=80, blank=True, null=True)
    ad_mod_date = models.DateTimeField(blank=True, null=True)
    ad_userid = models.CharField(max_length=80, blank=True, null=True)
    ad_edi_id = models.CharField(max_length=30, blank=True, null=True)
    ad_edi_ctrl_1 = models.TextField(
        db_column="ad_edi_ctrl##1", blank=True, null=True
    )  # Field renamed to remove unsuitable characters.
    ad_edi_ctrl_2 = models.TextField(
        db_column="ad_edi_ctrl##2", blank=True, null=True
    )  # Field renamed to remove unsuitable characters.
    ad_edi_ctrl_3 = models.TextField(
        db_column="ad_edi_ctrl##3", blank=True, null=True
    )  # Field renamed to remove unsuitable characters.
    ad_edi_ctrl_4 = models.TextField(
        db_column="ad_edi_ctrl##4", blank=True, null=True
    )  # Field renamed to remove unsuitable characters.
    ad_edi_ctrl_5 = models.TextField(
        db_column="ad_edi_ctrl##5", blank=True, null=True
    )  # Field renamed to remove unsuitable characters.
    ad_conrep = models.CharField(max_length=30, blank=True, null=True)
    ad_barlbl_prt = models.TextField(blank=True, null=True)
    ad_barlbl_val = models.CharField(max_length=30, blank=True, null=True)
    ad_calendar = models.CharField(max_length=80, blank=True, null=True)
    ad_edi_std = models.CharField(max_length=80, blank=True, null=True)
    ad_edi_level = models.CharField(max_length=80, blank=True, null=True)
    ad_qad01 = models.CharField(
        db_column="ad__qad01", max_length=80, blank=True, null=True
    )  # Field renamed because it contained more than one '_' in a row.
    ad_qad02 = models.CharField(
        db_column="ad__qad02", max_length=80, blank=True, null=True
    )  # Field renamed because it contained more than one '_' in a row.
    ad_qad03 = models.CharField(
        db_column="ad__qad03", max_length=80, blank=True, null=True
    )  # Field renamed because it contained more than one '_' in a row.
    ad_qad04 = models.CharField(
        db_column="ad__qad04", max_length=80, blank=True, null=True
    )  # Field renamed because it contained more than one '_' in a row.
    ad_qad05 = models.CharField(
        db_column="ad__qad05", max_length=80, blank=True, null=True
    )  # Field renamed because it contained more than one '_' in a row.
    ad_chr01 = models.CharField(
        db_column="ad__chr01", max_length=80, blank=True, null=True
    )  # Field renamed because it contained more than one '_' in a row.
    ad_chr02 = models.CharField(
        db_column="ad__chr02", max_length=80, blank=True, null=True
    )  # Field renamed because it contained more than one '_' in a row.
    ad_chr03 = models.CharField(
        db_column="ad__chr03", max_length=80, blank=True, null=True
    )  # Field renamed because it contained more than one '_' in a row.
    ad_chr04 = models.CharField(
        db_column="ad__chr04", max_length=80, blank=True, null=True
    )  # Field renamed because it contained more than one '_' in a row.
    ad_chr05 = models.CharField(
        db_column="ad__chr05", max_length=80, blank=True, null=True
    )  # Field renamed because it contained more than one '_' in a row.
    ad_tp_loc_code = models.CharField(max_length=30, blank=True, null=True)
    ad_ctry = models.CharField(max_length=30, blank=True, null=True)
    ad_tax_zone = models.CharField(max_length=30, blank=True, null=True)
    ad_tax_usage = models.CharField(max_length=80, blank=True, null=True)
    ad_misc1_id = models.CharField(max_length=30, blank=True, null=True)
    ad_misc2_id = models.CharField(max_length=30, blank=True, null=True)
    ad_misc3_id = models.CharField(max_length=30, blank=True, null=True)
    ad_wk_offset = models.IntegerField(blank=True, null=True)
    ad_inv_mthd = models.CharField(max_length=30, blank=True, null=True)
    ad_sch_mthd = models.CharField(max_length=30, blank=True, null=True)
    ad_po_mthd = models.CharField(max_length=30, blank=True, null=True)
    ad_asn_data = models.TextField(blank=True, null=True)
    ad_intr_division = models.CharField(max_length=30, blank=True, null=True)
    ad_tax_report = models.BooleanField(blank=True, null=True)
    ad_name_control = models.CharField(max_length=30, blank=True, null=True)
    ad_last_file = models.BooleanField(blank=True, null=True)
    ad_domain = models.CharField(max_length=8, blank=True, null=True)
    oid_ad_mstr = models.DecimalField(
        max_digits=38, decimal_places=10, blank=True, null=True
    )
    ad_email = models.CharField(max_length=48, blank=True, null=True)
    ad_email2 = models.CharField(max_length=48, blank=True, null=True)
    ad_bus_relation = models.CharField(max_length=20, blank=True, null=True)
    ad_priority = models.CharField(max_length=16, blank=True, null=True)
    ad_route = models.CharField(max_length=16, blank=True, null=True)
    ad_loadseq = models.CharField(max_length=16, blank=True, null=True)
    ad_pick_by_date = models.BooleanField(blank=True, null=True)
    ad_profile = models.CharField(max_length=16, blank=True, null=True)
    ad_address_id = models.BigIntegerField(blank=True, null=True)
    ad_tax_in_city = models.BooleanField(blank=True, null=True)
    ad_ns_pr_list = models.CharField(max_length=16, blank=True, null=True)
    ad_alt_um = models.CharField(max_length=4, blank=True, null=True)
    ad_city_code = models.CharField(max_length=20, blank=True, null=True)
    pro2srcpdb = models.CharField(
        db_column="Pro2SrcPDB", max_length=12, blank=True, null=True
    )  # Field name made lowercase.
    pro2created = models.DateTimeField(blank=True, null=True)
    pro2modified = models.DateTimeField(blank=True, null=True)

    class Meta:
        db_table = "ad_mstr"


class AbscDet(models.Model):
    prrowid = models.CharField(primary_key=True, max_length=36)
    absc_abs_id = models.CharField(max_length=30, blank=True, null=True)
    absc_seq = models.IntegerField(blank=True, null=True)
    absc_carrier = models.CharField(max_length=80, blank=True, null=True)
    absc_user1 = models.CharField(max_length=80, blank=True, null=True)
    absc_user2 = models.CharField(max_length=80, blank=True, null=True)
    absc_qadc01 = models.CharField(
        db_column="absc__qadc01", max_length=80, blank=True, null=True
    )  # Field renamed because it contained more than one '_' in a row.
    absc_domain = models.CharField(max_length=8, blank=True, null=True)
    oid_absc_det = models.DecimalField(
        max_digits=38, decimal_places=10, blank=True, null=True
    )
    pro2srcpdb = models.CharField(
        db_column="Pro2SrcPDB", max_length=12, blank=True, null=True
    )  # Field name made lowercase.
    pro2created = models.DateTimeField(blank=True, null=True)
    pro2modified = models.DateTimeField(blank=True, null=True)

    class Meta:
        db_table = "absc_det"


class PtMstr(models.Model):
    prrowid = models.CharField(primary_key=True, max_length=36)
    pt_part = models.CharField(max_length=30, blank=True, null=True)
    pt_desc1 = models.CharField(max_length=80, blank=True, null=True)
    pt_desc2 = models.CharField(max_length=80, blank=True, null=True)
    pt_um = models.CharField(max_length=30, blank=True, null=True)
    pt_qad13 = models.CharField(
        db_column="pt__qad13", max_length=30, blank=True, null=True
    )  # Field renamed because it contained more than one '_' in a row.
    pt_qad12 = models.DecimalField(
        db_column="pt__qad12", max_digits=38, decimal_places=10, blank=True, null=True
    )  # Field renamed because it contained more than one '_' in a row.
    pt_draw = models.CharField(max_length=30, blank=True, null=True)
    pt_prod_line = models.CharField(max_length=30, blank=True, null=True)
    pt_group = models.CharField(max_length=80, blank=True, null=True)
    pt_part_type = models.CharField(max_length=80, blank=True, null=True)
    pt_status = models.CharField(max_length=80, blank=True, null=True)
    pt_abc = models.CharField(max_length=30, blank=True, null=True)
    pt_iss_pol = models.BooleanField(blank=True, null=True)
    pt_phantom = models.BooleanField(blank=True, null=True)
    pt_loc = models.CharField(max_length=80, blank=True, null=True)
    pt_qad01 = models.DecimalField(
        db_column="pt__qad01", max_digits=38, decimal_places=10, blank=True, null=True
    )  # Field renamed because it contained more than one '_' in a row.
    pt_qad02 = models.DecimalField(
        db_column="pt__qad02", max_digits=38, decimal_places=10, blank=True, null=True
    )  # Field renamed because it contained more than one '_' in a row.
    pt_abc_amt = models.DecimalField(
        max_digits=38, decimal_places=10, blank=True, null=True
    )
    pt_qad03 = models.DecimalField(
        db_column="pt__qad03", max_digits=38, decimal_places=10, blank=True, null=True
    )  # Field renamed because it contained more than one '_' in a row.
    pt_qad04 = models.DecimalField(
        db_column="pt__qad04", max_digits=38, decimal_places=10, blank=True, null=True
    )  # Field renamed because it contained more than one '_' in a row.
    pt_avg_int = models.IntegerField(blank=True, null=True)
    pt_qad05 = models.DateTimeField(
        db_column="pt__qad05", blank=True, null=True
    )  # Field renamed because it contained more than one '_' in a row.
    pt_cyc_int = models.IntegerField(blank=True, null=True)
    pt_qad06 = models.DateTimeField(
        db_column="pt__qad06", blank=True, null=True
    )  # Field renamed because it contained more than one '_' in a row.
    pt_qad07 = models.DateTimeField(
        db_column="pt__qad07", blank=True, null=True
    )  # Field renamed because it contained more than one '_' in a row.
    pt_qad08 = models.DateTimeField(
        db_column="pt__qad08", blank=True, null=True
    )  # Field renamed because it contained more than one '_' in a row.
    pt_ms = models.BooleanField(blank=True, null=True)
    pt_plan_ord = models.BooleanField(blank=True, null=True)
    pt_mrp = models.BooleanField(blank=True, null=True)
    pt_ord_pol = models.CharField(max_length=30, blank=True, null=True)
    pt_ord_qty = models.DecimalField(
        max_digits=38, decimal_places=10, blank=True, null=True
    )
    pt_ord_per = models.IntegerField(blank=True, null=True)
    pt_sfty_stk = models.DecimalField(
        max_digits=38, decimal_places=0, blank=True, null=True
    )
    pt_sfty_time = models.DecimalField(
        max_digits=38, decimal_places=0, blank=True, null=True
    )
    pt_rop = models.DecimalField(max_digits=38, decimal_places=0, blank=True, null=True)
    pt_buyer = models.CharField(max_length=80, blank=True, null=True)
    pt_vend = models.CharField(max_length=80, blank=True, null=True)
    pt_qad09 = models.DecimalField(
        db_column="pt__qad09", max_digits=38, decimal_places=10, blank=True, null=True
    )  # Field renamed because it contained more than one '_' in a row.
    pt_pm_code = models.CharField(max_length=30, blank=True, null=True)
    pt_mfg_lead = models.DecimalField(
        max_digits=38, decimal_places=0, blank=True, null=True
    )
    pt_pur_lead = models.IntegerField(blank=True, null=True)
    pt_insp_rqd = models.BooleanField(blank=True, null=True)
    pt_insp_lead = models.IntegerField(blank=True, null=True)
    pt_cum_lead = models.IntegerField(blank=True, null=True)
    pt_ord_min = models.DecimalField(
        max_digits=38, decimal_places=0, blank=True, null=True
    )
    pt_ord_max = models.DecimalField(
        max_digits=38, decimal_places=0, blank=True, null=True
    )
    pt_ord_mult = models.DecimalField(
        max_digits=38, decimal_places=0, blank=True, null=True
    )
    pt_yield_pct = models.DecimalField(
        max_digits=38, decimal_places=10, blank=True, null=True
    )
    pt_qad16 = models.DecimalField(
        db_column="pt__qad16", max_digits=38, decimal_places=0, blank=True, null=True
    )  # Field renamed because it contained more than one '_' in a row.
    pt_setup = models.DecimalField(
        max_digits=38, decimal_places=10, blank=True, null=True
    )
    pt_setup_ll = models.DecimalField(
        max_digits=38, decimal_places=10, blank=True, null=True
    )
    pt_run_ll = models.DecimalField(
        max_digits=38, decimal_places=10, blank=True, null=True
    )
    pt_run = models.DecimalField(
        max_digits=38, decimal_places=10, blank=True, null=True
    )
    pt_price = models.DecimalField(
        max_digits=38, decimal_places=10, blank=True, null=True
    )
    pt_xmtl_tl = models.DecimalField(
        max_digits=38, decimal_places=10, blank=True, null=True
    )
    pt_xlbr_tl = models.DecimalField(
        max_digits=38, decimal_places=10, blank=True, null=True
    )
    pt_xbdn_tl = models.DecimalField(
        max_digits=38, decimal_places=10, blank=True, null=True
    )
    pt_xsub_tl = models.DecimalField(
        max_digits=38, decimal_places=10, blank=True, null=True
    )
    pt_xmtl_ll = models.DecimalField(
        max_digits=38, decimal_places=10, blank=True, null=True
    )
    pt_xlbr_ll = models.DecimalField(
        max_digits=38, decimal_places=10, blank=True, null=True
    )
    pt_xbdn_ll = models.DecimalField(
        max_digits=38, decimal_places=10, blank=True, null=True
    )
    pt_xsub_ll = models.DecimalField(
        max_digits=38, decimal_places=10, blank=True, null=True
    )
    pt_xtot_cur = models.DecimalField(
        max_digits=38, decimal_places=10, blank=True, null=True
    )
    pt_cur_date = models.DateTimeField(blank=True, null=True)
    pt_xmtl_stdtl = models.DecimalField(
        max_digits=38, decimal_places=10, blank=True, null=True
    )
    pt_xlbr_stdtl = models.DecimalField(
        max_digits=38, decimal_places=10, blank=True, null=True
    )
    pt_xbdn_stdtl = models.DecimalField(
        max_digits=38, decimal_places=10, blank=True, null=True
    )
    pt_xsub_stdtl = models.DecimalField(
        max_digits=38, decimal_places=10, blank=True, null=True
    )
    pt_xtot_std = models.DecimalField(
        max_digits=38, decimal_places=10, blank=True, null=True
    )
    pt_std_date = models.DateTimeField(blank=True, null=True)
    pt_ll_code = models.IntegerField(blank=True, null=True)
    pt_abc_qty = models.DecimalField(
        max_digits=38, decimal_places=10, blank=True, null=True
    )
    pt_qad10 = models.DecimalField(
        db_column="pt__qad10", max_digits=38, decimal_places=10, blank=True, null=True
    )  # Field renamed because it contained more than one '_' in a row.
    pt_qad11 = models.DecimalField(
        db_column="pt__qad11", max_digits=38, decimal_places=10, blank=True, null=True
    )  # Field renamed because it contained more than one '_' in a row.
    pt_routing = models.CharField(max_length=30, blank=True, null=True)
    pt_lot_ser = models.CharField(max_length=30, blank=True, null=True)
    pt_timefence = models.IntegerField(blank=True, null=True)
    pt_xmtl_stdll = models.DecimalField(
        max_digits=38, decimal_places=10, blank=True, null=True
    )
    pt_xlbr_stdll = models.DecimalField(
        max_digits=38, decimal_places=10, blank=True, null=True
    )
    pt_xbdn_stdll = models.DecimalField(
        max_digits=38, decimal_places=10, blank=True, null=True
    )
    pt_xsub_stdll = models.DecimalField(
        max_digits=38, decimal_places=10, blank=True, null=True
    )
    pt_rev = models.CharField(max_length=30, blank=True, null=True)
    pt_last_eco = models.DateTimeField(blank=True, null=True)
    pt_qad15 = models.BooleanField(
        db_column="pt__qad15", blank=True, null=True
    )  # Field renamed because it contained more than one '_' in a row.
    pt_qad17 = models.BooleanField(
        db_column="pt__qad17", blank=True, null=True
    )  # Field renamed because it contained more than one '_' in a row.
    pt_qc_lead = models.IntegerField(blank=True, null=True)
    pt_auto_lot = models.BooleanField(blank=True, null=True)
    pt_assay = models.DecimalField(
        max_digits=38, decimal_places=10, blank=True, null=True
    )
    pt_batch = models.DecimalField(
        max_digits=38, decimal_places=10, blank=True, null=True
    )
    pt_qad14 = models.DateTimeField(
        db_column="pt__qad14", blank=True, null=True
    )  # Field renamed because it contained more than one '_' in a row.
    pt_user3 = models.CharField(max_length=80, blank=True, null=True)
    pt_user1 = models.CharField(max_length=80, blank=True, null=True)
    pt_user2 = models.CharField(max_length=80, blank=True, null=True)
    pt_net_wt = models.DecimalField(
        max_digits=38, decimal_places=10, blank=True, null=True
    )
    pt_net_wt_um = models.CharField(max_length=30, blank=True, null=True)
    pt_size = models.DecimalField(
        max_digits=38, decimal_places=10, blank=True, null=True
    )
    pt_size_um = models.CharField(max_length=30, blank=True, null=True)
    pt_taxable = models.BooleanField(blank=True, null=True)
    pt_taxc = models.CharField(max_length=30, blank=True, null=True)
    pt_rollup = models.BooleanField(blank=True, null=True)
    pt_xovh_ll = models.DecimalField(
        max_digits=38, decimal_places=10, blank=True, null=True
    )
    pt_xovh_tl = models.DecimalField(
        max_digits=38, decimal_places=10, blank=True, null=True
    )
    pt_xovh_stdll = models.DecimalField(
        max_digits=38, decimal_places=10, blank=True, null=True
    )
    pt_xovh_stdtl = models.DecimalField(
        max_digits=38, decimal_places=10, blank=True, null=True
    )
    pt_site = models.CharField(max_length=80, blank=True, null=True)
    pt_shelflife = models.IntegerField(blank=True, null=True)
    pt_critical = models.BooleanField(blank=True, null=True)
    pt_sngl_lot = models.BooleanField(blank=True, null=True)
    pt_upc = models.CharField(max_length=30, blank=True, null=True)
    pt_hazard = models.CharField(max_length=80, blank=True, null=True)
    pt_added = models.DateTimeField(blank=True, null=True)
    pt_chr01 = models.CharField(
        db_column="pt__chr01", max_length=80, blank=True, null=True
    )  # Field renamed because it contained more than one '_' in a row.
    pt_chr02 = models.CharField(
        db_column="pt__chr02", max_length=80, blank=True, null=True
    )  # Field renamed because it contained more than one '_' in a row.
    pt_chr03 = models.CharField(
        db_column="pt__chr03", max_length=80, blank=True, null=True
    )  # Field renamed because it contained more than one '_' in a row.
    pt_chr04 = models.CharField(
        db_column="pt__chr04", max_length=80, blank=True, null=True
    )  # Field renamed because it contained more than one '_' in a row.
    pt_chr05 = models.CharField(
        db_column="pt__chr05", max_length=80, blank=True, null=True
    )  # Field renamed because it contained more than one '_' in a row.
    pt_chr06 = models.CharField(
        db_column="pt__chr06", max_length=80, blank=True, null=True
    )  # Field renamed because it contained more than one '_' in a row.
    pt_chr07 = models.CharField(
        db_column="pt__chr07", max_length=80, blank=True, null=True
    )  # Field renamed because it contained more than one '_' in a row.
    pt_chr08 = models.CharField(
        db_column="pt__chr08", max_length=80, blank=True, null=True
    )  # Field renamed because it contained more than one '_' in a row.
    pt_chr09 = models.CharField(
        db_column="pt__chr09", max_length=80, blank=True, null=True
    )  # Field renamed because it contained more than one '_' in a row.
    pt_chr10 = models.CharField(
        db_column="pt__chr10", max_length=80, blank=True, null=True
    )  # Field renamed because it contained more than one '_' in a row.
    pt_dte01 = models.DateTimeField(
        db_column="pt__dte01", blank=True, null=True
    )  # Field renamed because it contained more than one '_' in a row.
    pt_dte02 = models.DateTimeField(
        db_column="pt__dte02", blank=True, null=True
    )  # Field renamed because it contained more than one '_' in a row.
    pt_dec01 = models.DecimalField(
        db_column="pt__dec01", max_digits=38, decimal_places=10, blank=True, null=True
    )  # Field renamed because it contained more than one '_' in a row.
    pt_dec02 = models.DecimalField(
        db_column="pt__dec02", max_digits=38, decimal_places=10, blank=True, null=True
    )  # Field renamed because it contained more than one '_' in a row.
    pt_log01 = models.BooleanField(
        db_column="pt__log01", blank=True, null=True
    )  # Field renamed because it contained more than one '_' in a row.
    pt_log02 = models.BooleanField(
        db_column="pt__log02", blank=True, null=True
    )  # Field renamed because it contained more than one '_' in a row.
    pt_qad18 = models.DecimalField(
        db_column="pt__qad18", max_digits=38, decimal_places=10, blank=True, null=True
    )  # Field renamed because it contained more than one '_' in a row.
    pt_qad21 = models.DecimalField(
        db_column="pt__qad21", max_digits=38, decimal_places=10, blank=True, null=True
    )  # Field renamed because it contained more than one '_' in a row.
    pt_qad19 = models.DecimalField(
        db_column="pt__qad19", max_digits=38, decimal_places=10, blank=True, null=True
    )  # Field renamed because it contained more than one '_' in a row.
    pt_qad20 = models.DecimalField(
        db_column="pt__qad20", max_digits=38, decimal_places=10, blank=True, null=True
    )  # Field renamed because it contained more than one '_' in a row.
    pt_length = models.DecimalField(
        max_digits=38, decimal_places=10, blank=True, null=True
    )
    pt_height = models.DecimalField(
        max_digits=38, decimal_places=10, blank=True, null=True
    )
    pt_width = models.DecimalField(
        max_digits=38, decimal_places=10, blank=True, null=True
    )
    pt_dim_um = models.CharField(max_length=30, blank=True, null=True)
    pt_pkg_code = models.CharField(max_length=30, blank=True, null=True)
    pt_network = models.CharField(max_length=30, blank=True, null=True)
    pt_ll_drp = models.IntegerField(blank=True, null=True)
    pt_fr_class = models.CharField(max_length=80, blank=True, null=True)
    pt_spec_hdlg = models.CharField(max_length=80, blank=True, null=True)
    pt_bom_code = models.CharField(max_length=30, blank=True, null=True)
    pt_loc_type = models.CharField(max_length=80, blank=True, null=True)
    pt_transtype = models.CharField(max_length=80, blank=True, null=True)
    pt_cover = models.CharField(max_length=30, blank=True, null=True)
    pt_unit_isb = models.BooleanField(blank=True, null=True)
    pt_article = models.CharField(max_length=30, blank=True, null=True)
    pt_po_site = models.CharField(max_length=80, blank=True, null=True)
    pt_ship_wt = models.DecimalField(
        max_digits=38, decimal_places=10, blank=True, null=True
    )
    pt_ship_wt_um = models.CharField(max_length=30, blank=True, null=True)
    pt_formula = models.BooleanField(blank=True, null=True)
    pt_dea = models.BooleanField(blank=True, null=True)
    pt_qad26 = models.BooleanField(
        db_column="pt__qad26", blank=True, null=True
    )  # Field renamed because it contained more than one '_' in a row.
    pt_qad22 = models.BooleanField(
        db_column="pt__qad22", blank=True, null=True
    )  # Field renamed because it contained more than one '_' in a row.
    pt_qad25 = models.IntegerField(
        db_column="pt__qad25", blank=True, null=True
    )  # Field renamed because it contained more than one '_' in a row.
    pt_qad24 = models.IntegerField(
        db_column="pt__qad24", blank=True, null=True
    )  # Field renamed because it contained more than one '_' in a row.
    pt_qad23 = models.IntegerField(
        db_column="pt__qad23", blank=True, null=True
    )  # Field renamed because it contained more than one '_' in a row.
    pt_comm_code = models.CharField(max_length=80, blank=True, null=True)
    pt_inst_call = models.BooleanField(blank=True, null=True)
    pt_sys_type = models.CharField(max_length=30, blank=True, null=True)
    pt_tariff = models.CharField(max_length=80, blank=True, null=True)
    pt_origin = models.CharField(max_length=30, blank=True, null=True)
    pt_sttr = models.DecimalField(
        max_digits=38, decimal_places=10, blank=True, null=True
    )
    pt_mfg_mtbf = models.DecimalField(
        max_digits=38, decimal_places=10, blank=True, null=True
    )
    pt_mfg_mttr = models.DecimalField(
        max_digits=38, decimal_places=10, blank=True, null=True
    )
    pt_fru = models.BooleanField(blank=True, null=True)
    pt_ven_warr = models.BooleanField(blank=True, null=True)
    pt_svc_group = models.CharField(max_length=80, blank=True, null=True)
    pt_svc_type = models.CharField(max_length=30, blank=True, null=True)
    pt_mtbf = models.DecimalField(
        max_digits=38, decimal_places=10, blank=True, null=True
    )
    pt_mttr = models.DecimalField(
        max_digits=38, decimal_places=10, blank=True, null=True
    )
    pt_isb = models.BooleanField(blank=True, null=True)
    pt_pvm_days = models.IntegerField(blank=True, null=True)
    pt_warr_cd = models.CharField(max_length=80, blank=True, null=True)
    pt_mod_date = models.DateTimeField(blank=True, null=True)
    pt_userid = models.CharField(max_length=80, blank=True, null=True)
    pt_obs_date = models.DateTimeField(blank=True, null=True)
    pt_pvm_bom = models.CharField(max_length=30, blank=True, null=True)
    pt_pvm_route = models.CharField(max_length=30, blank=True, null=True)
    pt_pvm_um = models.CharField(max_length=30, blank=True, null=True)
    pt_rp_bom = models.CharField(max_length=30, blank=True, null=True)
    pt_rp_route = models.CharField(max_length=30, blank=True, null=True)
    pt_rp_vendor = models.CharField(max_length=80, blank=True, null=True)
    pt_rctpo_status = models.CharField(max_length=80, blank=True, null=True)
    pt_rollup_id = models.CharField(max_length=80, blank=True, null=True)
    pt_spec_grav = models.DecimalField(
        max_digits=38, decimal_places=10, blank=True, null=True
    )
    pt_joint_type = models.CharField(max_length=30, blank=True, null=True)
    pt_mfg_pct = models.DecimalField(
        max_digits=38, decimal_places=10, blank=True, null=True
    )
    pt_pur_pct = models.DecimalField(
        max_digits=38, decimal_places=10, blank=True, null=True
    )
    pt_drp_pct = models.DecimalField(
        max_digits=38, decimal_places=10, blank=True, null=True
    )
    pt_pou_code = models.CharField(max_length=30, blank=True, null=True)
    pt_wks_avg = models.DecimalField(
        max_digits=38, decimal_places=10, blank=True, null=True
    )
    pt_wks_max = models.DecimalField(
        max_digits=38, decimal_places=10, blank=True, null=True
    )
    pt_wks_min = models.DecimalField(
        max_digits=38, decimal_places=10, blank=True, null=True
    )
    pt_pick_logic = models.IntegerField(blank=True, null=True)
    pt_fiscal_class = models.CharField(max_length=30, blank=True, null=True)
    pt_dsgn_grp = models.CharField(max_length=80, blank=True, null=True)
    pt_drwg_loc = models.CharField(max_length=80, blank=True, null=True)
    pt_ecn_rev = models.CharField(max_length=30, blank=True, null=True)
    pt_drwg_size = models.CharField(max_length=30, blank=True, null=True)
    pt_model = models.CharField(max_length=30, blank=True, null=True)
    pt_repairable = models.BooleanField(blank=True, null=True)
    pt_rctwo_status = models.CharField(max_length=80, blank=True, null=True)
    pt_lot_grp = models.CharField(max_length=80, blank=True, null=True)
    pt_rctpo_active = models.BooleanField(blank=True, null=True)
    pt_rctwo_active = models.BooleanField(blank=True, null=True)
    pt_break_cat = models.CharField(max_length=30, blank=True, null=True)
    pt_fsc_code = models.CharField(max_length=80, blank=True, null=True)
    pt_trace_active = models.BooleanField(blank=True, null=True)
    pt_trace_detail = models.BooleanField(blank=True, null=True)
    pt_pm_mrp = models.BooleanField(blank=True, null=True)
    pt_ins_call_type = models.CharField(max_length=80, blank=True, null=True)
    pt_ins_bom = models.CharField(max_length=30, blank=True, null=True)
    pt_ins_route = models.CharField(max_length=30, blank=True, null=True)
    pt_promo = models.CharField(max_length=80, blank=True, null=True)
    pt_meter_interval = models.DecimalField(
        max_digits=38, decimal_places=10, blank=True, null=True
    )
    pt_meter_um = models.CharField(max_length=30, blank=True, null=True)
    pt_wh = models.BooleanField(blank=True, null=True)
    pt_btb_type = models.CharField(max_length=30, blank=True, null=True)
    pt_cfg_type = models.CharField(max_length=30, blank=True, null=True)
    pt_app_owner = models.CharField(max_length=30, blank=True, null=True)
    pt_op_yield = models.BooleanField(blank=True, null=True)
    pt_run_seq1 = models.CharField(max_length=80, blank=True, null=True)
    pt_run_seq2 = models.CharField(max_length=80, blank=True, null=True)
    pt_atp_enforcement = models.CharField(max_length=30, blank=True, null=True)
    pt_atp_family = models.BooleanField(blank=True, null=True)
    pt_domain = models.CharField(max_length=8, blank=True, null=True)
    oid_pt_mstr = models.DecimalField(
        max_digits=38, decimal_places=10, blank=True, null=True
    )
    pt_classification = models.CharField(max_length=12, blank=True, null=True)
    pt_memo_type = models.CharField(max_length=1, blank=True, null=True)
    pt_um_group = models.CharField(max_length=16, blank=True, null=True)
    pt_opc_threshold = models.DecimalField(
        max_digits=20, decimal_places=10, blank=True, null=True
    )
    pt_pop_code = models.CharField(max_length=16, blank=True, null=True)
    pt_whse_part_type = models.CharField(max_length=16, blank=True, null=True)
    pt_issue_method = models.CharField(max_length=16, blank=True, null=True)
    pt_rep_type = models.CharField(max_length=16, blank=True, null=True)
    pt_same_days_1 = models.IntegerField(
        db_column="pt_same_days##1", blank=True, null=True
    )  # Field renamed to remove unsuitable characters.
    pt_same_days_2 = models.IntegerField(
        db_column="pt_same_days##2", blank=True, null=True
    )  # Field renamed to remove unsuitable characters.
    pt_same_days_3 = models.IntegerField(
        db_column="pt_same_days##3", blank=True, null=True
    )  # Field renamed to remove unsuitable characters.
    pt_same_days_4 = models.IntegerField(
        db_column="pt_same_days##4", blank=True, null=True
    )  # Field renamed to remove unsuitable characters.
    pt_same_days_5 = models.IntegerField(
        db_column="pt_same_days##5", blank=True, null=True
    )  # Field renamed to remove unsuitable characters.
    pt_same_days_6 = models.IntegerField(
        db_column="pt_same_days##6", blank=True, null=True
    )  # Field renamed to remove unsuitable characters.
    pt_same_days_7 = models.IntegerField(
        db_column="pt_same_days##7", blank=True, null=True
    )  # Field renamed to remove unsuitable characters.
    pt_same_days_8 = models.IntegerField(
        db_column="pt_same_days##8", blank=True, null=True
    )  # Field renamed to remove unsuitable characters.
    pt_same_days_9 = models.IntegerField(
        db_column="pt_same_days##9", blank=True, null=True
    )  # Field renamed to remove unsuitable characters.
    pt_same_days_10 = models.IntegerField(
        db_column="pt_same_days##10", blank=True, null=True
    )  # Field renamed to remove unsuitable characters.
    pt_invent_days_1 = models.IntegerField(
        db_column="pt_invent_days##1", blank=True, null=True
    )  # Field renamed to remove unsuitable characters.
    pt_invent_days_2 = models.IntegerField(
        db_column="pt_invent_days##2", blank=True, null=True
    )  # Field renamed to remove unsuitable characters.
    pt_invent_days_3 = models.IntegerField(
        db_column="pt_invent_days##3", blank=True, null=True
    )  # Field renamed to remove unsuitable characters.
    pt_invent_days_4 = models.IntegerField(
        db_column="pt_invent_days##4", blank=True, null=True
    )  # Field renamed to remove unsuitable characters.
    pt_invent_days_5 = models.IntegerField(
        db_column="pt_invent_days##5", blank=True, null=True
    )  # Field renamed to remove unsuitable characters.
    pt_invent_days_6 = models.IntegerField(
        db_column="pt_invent_days##6", blank=True, null=True
    )  # Field renamed to remove unsuitable characters.
    pt_invent_days_7 = models.IntegerField(
        db_column="pt_invent_days##7", blank=True, null=True
    )  # Field renamed to remove unsuitable characters.
    pt_invent_days_8 = models.IntegerField(
        db_column="pt_invent_days##8", blank=True, null=True
    )  # Field renamed to remove unsuitable characters.
    pt_invent_days_9 = models.IntegerField(
        db_column="pt_invent_days##9", blank=True, null=True
    )  # Field renamed to remove unsuitable characters.
    pt_invent_days_10 = models.IntegerField(
        db_column="pt_invent_days##10", blank=True, null=True
    )  # Field renamed to remove unsuitable characters.
    pt_crit_days = models.IntegerField(blank=True, null=True)
    pt_shelf_offset = models.IntegerField(blank=True, null=True)
    pt_single_trans = models.BooleanField(blank=True, null=True)
    pt_print_id = models.BooleanField(blank=True, null=True)
    pt_id_qty = models.IntegerField(blank=True, null=True)
    pt_insp_req = models.BooleanField(blank=True, null=True)
    pt_qad27 = models.IntegerField(
        db_column="pt__qad27", blank=True, null=True
    )  # Field renamed because it contained more than one '_' in a row.
    pt_sample_pct = models.IntegerField(blank=True, null=True)
    pt_insp_freq = models.IntegerField(blank=True, null=True)
    pt_destructive = models.BooleanField(blank=True, null=True)
    pt_insp_days = models.IntegerField(blank=True, null=True)
    pt_barcode1 = models.CharField(max_length=80, blank=True, null=True)
    pt_barcode2 = models.CharField(max_length=80, blank=True, null=True)
    pt_insp_ref = models.BooleanField(blank=True, null=True)
    pt_random_insp_pct = models.DecimalField(
        max_digits=20, decimal_places=10, blank=True, null=True
    )
    pt_atp_horizon = models.IntegerField(blank=True, null=True)
    pt_gcfg_type = models.CharField(max_length=8, blank=True, null=True)
    pt_replenishment_mthd = models.CharField(max_length=8, blank=True, null=True)
    pt_gtin_barcode1 = models.CharField(max_length=80, blank=True, null=True)
    pt_gtin_barcode2 = models.CharField(max_length=80, blank=True, null=True)
    pt_fiscal_type = models.CharField(max_length=2, blank=True, null=True)
    pt_service_code = models.CharField(max_length=4, blank=True, null=True)
    pt_freight_nature = models.CharField(max_length=1, blank=True, null=True)
    pt_trade_class = models.CharField(max_length=8, blank=True, null=True)
    pt_serialized = models.IntegerField(blank=True, null=True)
    pt_sample_qty = models.DecimalField(
        max_digits=38, decimal_places=10, blank=True, null=True
    )
    pt_sourcetype = models.CharField(max_length=80, blank=True, null=True)
    pt_nve1_code = models.CharField(max_length=6, blank=True, null=True)
    pt_nve2_code = models.CharField(max_length=6, blank=True, null=True)
    pt_nve3_code = models.CharField(max_length=6, blank=True, null=True)
    pt_nve4_code = models.CharField(max_length=6, blank=True, null=True)
    pt_nve5_code = models.CharField(max_length=6, blank=True, null=True)
    pt_nve6_code = models.CharField(max_length=6, blank=True, null=True)
    pt_nve7_code = models.CharField(max_length=6, blank=True, null=True)
    pt_nve8_code = models.CharField(max_length=6, blank=True, null=True)
    pt_cest_code = models.CharField(max_length=9, blank=True, null=True)
    pt_enforce_cert = models.BooleanField(blank=True, null=True)
    pt_relev_scale = models.BooleanField(blank=True, null=True)
    pt_service_type = models.CharField(max_length=9, blank=True, null=True)
    pt_xml_group = models.CharField(max_length=8, blank=True, null=True)
    pt_anp_code = models.CharField(max_length=9, blank=True, null=True)
    pt_pk_ord = models.IntegerField(blank=True, null=True)
    pt_pk_ord_ascend = models.BooleanField(blank=True, null=True)
    pt_pick_pol = models.CharField(max_length=8, blank=True, null=True)
    pt_all_pol = models.CharField(max_length=8, blank=True, null=True)
    pt_xfer_all_pol = models.CharField(max_length=8, blank=True, null=True)
    pt_picklist_ord_mult = models.DecimalField(
        max_digits=38, decimal_places=0, blank=True, null=True
    )
    pt_picklist_ord_max = models.DecimalField(
        max_digits=38, decimal_places=0, blank=True, null=True
    )
    pt_picklist_ord_min = models.DecimalField(
        max_digits=38, decimal_places=0, blank=True, null=True
    )
    pt_comp_iss_pol = models.CharField(max_length=8, blank=True, null=True)
    pt_po_buyer = models.CharField(max_length=22, blank=True, null=True)
    pro2srcpdb = models.CharField(
        db_column="Pro2SrcPDB", max_length=12, blank=True, null=True
    )  # Field name made lowercase.
    pro2created = models.DateTimeField(blank=True, null=True)
    pro2modified = models.DateTimeField(blank=True, null=True)
    pt_plan_pos_var = models.DecimalField(
        max_digits=20, decimal_places=2, blank=True, null=True
    )
    pt_plan_neg_var = models.DecimalField(
        max_digits=20, decimal_places=2, blank=True, null=True
    )
    pt_ship_pos_var = models.DecimalField(
        max_digits=20, decimal_places=2, blank=True, null=True
    )
    pt_ship_neg_var = models.DecimalField(
        max_digits=20, decimal_places=2, blank=True, null=True
    )
    pt_schedule_type = models.CharField(max_length=8, blank=True, null=True)
    pt_smoothing_rule = models.CharField(max_length=8, blank=True, null=True)
    pt_avg_period = models.IntegerField(blank=True, null=True)
    pt_period_type = models.CharField(max_length=8, blank=True, null=True)

    class Meta:
        managed = False
        db_table = "pt_mstr"


class WevMstr(models.Model):
    prrowid = models.CharField(primary_key=True, max_length=36)
    wev_domain = models.CharField(max_length=16, blank=True, null=True)
    wev_event_id = models.BigIntegerField(blank=True, null=True)
    wev_type = models.CharField(max_length=16, blank=True, null=True)
    wev_master_id = models.IntegerField(blank=True, null=True)
    wev_whse = models.CharField(max_length=32, blank=True, null=True)
    wev_site = models.CharField(max_length=16, blank=True, null=True)
    wev_priority = models.IntegerField(blank=True, null=True)
    wev_pr_inc = models.IntegerField(blank=True, null=True)
    wev_status = models.CharField(max_length=16, blank=True, null=True)
    wev_reason = models.CharField(max_length=16, blank=True, null=True)
    wev_rmks = models.CharField(max_length=48, blank=True, null=True)
    wev_reference = models.CharField(max_length=48, blank=True, null=True)
    wev_shift = models.CharField(max_length=16, blank=True, null=True)
    wev_mes_ref = models.BigIntegerField(blank=True, null=True)
    wev_request = models.CharField(max_length=48, blank=True, null=True)
    wev_create_prog = models.CharField(max_length=16, blank=True, null=True)
    oid_wev_mstr = models.DecimalField(
        max_digits=38, decimal_places=10, blank=True, null=True
    )
    oid_abs_mstr = models.DecimalField(
        max_digits=38, decimal_places=10, blank=True, null=True
    )
    wev_create_userid = models.CharField(max_length=16, blank=True, null=True)
    wev_create_date = models.DateTimeField(blank=True, null=True)
    wev_create_time = models.CharField(max_length=16, blank=True, null=True)
    wev_mod_user = models.CharField(max_length=16, blank=True, null=True)
    wev_mod_date = models.DateTimeField(blank=True, null=True)
    wev_mod_time = models.CharField(max_length=16, blank=True, null=True)
    wev_close_user = models.CharField(max_length=16, blank=True, null=True)
    wev_close_date = models.DateTimeField(blank=True, null=True)
    wev_close_time = models.CharField(max_length=16, blank=True, null=True)
    wev_chr01 = models.CharField(
        db_column="wev__chr01", max_length=48, blank=True, null=True
    )  # Field renamed because it contained more than one '_' in a row.
    wev_chr02 = models.CharField(
        db_column="wev__chr02", max_length=48, blank=True, null=True
    )  # Field renamed because it contained more than one '_' in a row.
    wev_chr03 = models.CharField(
        db_column="wev__chr03", max_length=48, blank=True, null=True
    )  # Field renamed because it contained more than one '_' in a row.
    wev_chr04 = models.CharField(
        db_column="wev__chr04", max_length=48, blank=True, null=True
    )  # Field renamed because it contained more than one '_' in a row.
    wev_int01 = models.IntegerField(
        db_column="wev__int01", blank=True, null=True
    )  # Field renamed because it contained more than one '_' in a row.
    wev_int02 = models.IntegerField(
        db_column="wev__int02", blank=True, null=True
    )  # Field renamed because it contained more than one '_' in a row.
    wev_dec01 = models.DecimalField(
        db_column="wev__dec01", max_digits=17, decimal_places=2, blank=True, null=True
    )  # Field renamed because it contained more than one '_' in a row.
    wev_dte01 = models.DateTimeField(
        db_column="wev__dte01", blank=True, null=True
    )  # Field renamed because it contained more than one '_' in a row.
    wev_dte02 = models.DateTimeField(
        db_column="wev__dte02", blank=True, null=True
    )  # Field renamed because it contained more than one '_' in a row.
    wev_dec02 = models.DecimalField(
        db_column="wev__dec02", max_digits=15, decimal_places=2, blank=True, null=True
    )  # Field renamed because it contained more than one '_' in a row.
    wev_log02 = models.BooleanField(
        db_column="wev__log02", blank=True, null=True
    )  # Field renamed because it contained more than one '_' in a row.
    wev_log01 = models.BooleanField(
        db_column="wev__log01", blank=True, null=True
    )  # Field renamed because it contained more than one '_' in a row.
    pro2srcpdb = models.CharField(
        db_column="Pro2SrcPDB", max_length=12, blank=True, null=True
    )  # Field name made lowercase.
    pro2created = models.DateTimeField(blank=True, null=True)
    pro2modified = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = "wev_mstr"


class WevdDet(models.Model):
    prrowid = models.CharField(primary_key=True, max_length=36)
    wevd_domain = models.CharField(max_length=16, blank=True, null=True)
    wevd_event_id = models.BigIntegerField(blank=True, null=True)
    wevd_ev_sub_id = models.BigIntegerField(blank=True, null=True)
    wevd_nbr = models.CharField(max_length=36, blank=True, null=True)
    wevd_line = models.CharField(max_length=16, blank=True, null=True)
    wevd_dataset = models.CharField(max_length=16, blank=True, null=True)
    wevd_from_part = models.CharField(max_length=36, blank=True, null=True)
    wevd_storage_zone = models.CharField(max_length=32, blank=True, null=True)
    wevd_work_zone = models.CharField(max_length=32, blank=True, null=True)
    wevd_type = models.CharField(max_length=16, blank=True, null=True)
    wevd_status = models.CharField(max_length=16, blank=True, null=True)
    wevd_loc_from = models.CharField(max_length=32, blank=True, null=True)
    wevd_ser = models.CharField(max_length=80, blank=True, null=True)
    wevd_lotser = models.CharField(max_length=36, blank=True, null=True)
    wevd_ref = models.CharField(max_length=16, blank=True, null=True)
    wevd_qty_req = models.DecimalField(
        max_digits=25, decimal_places=10, blank=True, null=True
    )
    wevd_qty_comp = models.DecimalField(
        max_digits=25, decimal_places=10, blank=True, null=True
    )
    wevd_qty_cancel = models.DecimalField(
        max_digits=25, decimal_places=10, blank=True, null=True
    )
    wevd_qty_remain = models.DecimalField(
        max_digits=25, decimal_places=10, blank=True, null=True
    )
    wevd_to_whse = models.CharField(max_length=32, blank=True, null=True)
    wevd_to_site = models.CharField(max_length=16, blank=True, null=True)
    wevd_loc_to = models.CharField(max_length=32, blank=True, null=True)
    wevd_zone_to = models.CharField(max_length=32, blank=True, null=True)
    wevd_mes_ref = models.BigIntegerField(blank=True, null=True)
    wevd_pack = models.BooleanField(blank=True, null=True)
    oid_wevd_det = models.DecimalField(
        max_digits=38, decimal_places=10, blank=True, null=True
    )
    wevd_create_userid = models.CharField(max_length=16, blank=True, null=True)
    wevd_create_date = models.DateTimeField(blank=True, null=True)
    wevd_mod_user = models.CharField(max_length=16, blank=True, null=True)
    wevd_mod_date = models.DateTimeField(blank=True, null=True)
    wevd_mod_time = models.CharField(max_length=16, blank=True, null=True)
    wevd_chr01 = models.CharField(
        db_column="wevd__chr01", max_length=48, blank=True, null=True
    )  # Field renamed because it contained more than one '_' in a row.
    wevd_chr02 = models.CharField(
        db_column="wevd__chr02", max_length=48, blank=True, null=True
    )  # Field renamed because it contained more than one '_' in a row.
    wevd_chr03 = models.CharField(
        db_column="wevd__chr03", max_length=48, blank=True, null=True
    )  # Field renamed because it contained more than one '_' in a row.
    wevd_chr04 = models.CharField(
        db_column="wevd__chr04", max_length=48, blank=True, null=True
    )  # Field renamed because it contained more than one '_' in a row.
    wevd_int01 = models.IntegerField(
        db_column="wevd__int01", blank=True, null=True
    )  # Field renamed because it contained more than one '_' in a row.
    wevd_int02 = models.IntegerField(
        db_column="wevd__int02", blank=True, null=True
    )  # Field renamed because it contained more than one '_' in a row.
    wevd_dec01 = models.DecimalField(
        db_column="wevd__dec01", max_digits=17, decimal_places=2, blank=True, null=True
    )  # Field renamed because it contained more than one '_' in a row.
    wevd_dec02 = models.DecimalField(
        db_column="wevd__dec02", max_digits=17, decimal_places=2, blank=True, null=True
    )  # Field renamed because it contained more than one '_' in a row.
    wevd_dte01 = models.DateTimeField(
        db_column="wevd__dte01", blank=True, null=True
    )  # Field renamed because it contained more than one '_' in a row.
    wevd_dte02 = models.DateTimeField(
        db_column="wevd__dte02", blank=True, null=True
    )  # Field renamed because it contained more than one '_' in a row.
    wevd_log01 = models.BooleanField(
        db_column="wevd__log01", blank=True, null=True
    )  # Field renamed because it contained more than one '_' in a row.
    wevd_log02 = models.BooleanField(
        db_column="wevd__log02", blank=True, null=True
    )  # Field renamed because it contained more than one '_' in a row.
    pro2srcpdb = models.CharField(
        db_column="Pro2SrcPDB", max_length=12, blank=True, null=True
    )  # Field name made lowercase.
    pro2created = models.DateTimeField(blank=True, null=True)
    pro2modified = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = "wevd_det"


class WevhHist(models.Model):
    prrowid = models.CharField(primary_key=True, max_length=36)
    wevh_domain = models.CharField(max_length=8, blank=True, null=True)
    wevh_trnbr = models.BigIntegerField(blank=True, null=True)
    wevh_event_id = models.BigIntegerField(blank=True, null=True)
    wevh_ev_sub_id = models.BigIntegerField(blank=True, null=True)
    wevh_type = models.CharField(max_length=16, blank=True, null=True)
    wevh_master_id = models.IntegerField(blank=True, null=True)
    wevh_whse = models.CharField(max_length=4, blank=True, null=True)
    wevh_site = models.CharField(max_length=4, blank=True, null=True)
    wevh_wave_id = models.CharField(max_length=4, blank=True, null=True)
    wevh_priority = models.IntegerField(blank=True, null=True)
    wevh_pr_inc = models.IntegerField(blank=True, null=True)
    wevh_status = models.CharField(max_length=4, blank=True, null=True)
    wevh_reason = models.CharField(max_length=4, blank=True, null=True)
    wevh_shift = models.CharField(max_length=4, blank=True, null=True)
    wevh_sequence = models.IntegerField(blank=True, null=True)
    wevh_routing = models.CharField(max_length=4, blank=True, null=True)
    wevh_qty_req = models.DecimalField(
        max_digits=25, decimal_places=10, blank=True, null=True
    )
    wevh_qty_comp = models.DecimalField(
        max_digits=25, decimal_places=10, blank=True, null=True
    )
    wevh_qty_cancel = models.DecimalField(
        max_digits=25, decimal_places=10, blank=True, null=True
    )
    wevh_rmks = models.CharField(max_length=4, blank=True, null=True)
    wevh_reference = models.CharField(max_length=4, blank=True, null=True)
    wevh_mes_ref = models.BigIntegerField(blank=True, null=True)
    wevh_request = models.CharField(max_length=48, blank=True, null=True)
    wevh_create_prog = models.CharField(max_length=16, blank=True, null=True)
    wevh_qty_remain = models.DecimalField(
        max_digits=25, decimal_places=10, blank=True, null=True
    )
    oid_wevh_hist = models.DecimalField(
        max_digits=38, decimal_places=10, blank=True, null=True
    )
    wevh_create_userid = models.CharField(max_length=4, blank=True, null=True)
    wevh_create_date = models.DateTimeField(blank=True, null=True)
    wevh_create_time = models.CharField(max_length=16, blank=True, null=True)
    wevh_mod_userid = models.CharField(max_length=4, blank=True, null=True)
    wevh_mod_date = models.DateTimeField(blank=True, null=True)
    wevh_mod_time = models.CharField(max_length=16, blank=True, null=True)
    wevh_close_userid = models.CharField(max_length=4, blank=True, null=True)
    wevh_close_date = models.DateTimeField(blank=True, null=True)
    wevh_close_time = models.CharField(max_length=16, blank=True, null=True)
    wevh_chr01 = models.CharField(
        db_column="wevh__chr01", max_length=80, blank=True, null=True
    )  # Field renamed because it contained more than one '_' in a row.
    wevh_chr02 = models.CharField(
        db_column="wevh__chr02", max_length=80, blank=True, null=True
    )  # Field renamed because it contained more than one '_' in a row.
    wevh_chr03 = models.CharField(
        db_column="wevh__chr03", max_length=80, blank=True, null=True
    )  # Field renamed because it contained more than one '_' in a row.
    wevh_chr04 = models.CharField(
        db_column="wevh__chr04", max_length=80, blank=True, null=True
    )  # Field renamed because it contained more than one '_' in a row.
    wevh_int01 = models.IntegerField(
        db_column="wevh__int01", blank=True, null=True
    )  # Field renamed because it contained more than one '_' in a row.
    wevh_int02 = models.IntegerField(
        db_column="wevh__int02", blank=True, null=True
    )  # Field renamed because it contained more than one '_' in a row.
    wevh_dec01 = models.DecimalField(
        db_column="wevh__dec01", max_digits=38, decimal_places=10, blank=True, null=True
    )  # Field renamed because it contained more than one '_' in a row.
    wevh_dec02 = models.DecimalField(
        db_column="wevh__dec02", max_digits=38, decimal_places=10, blank=True, null=True
    )  # Field renamed because it contained more than one '_' in a row.
    wevh_dte01 = models.DateTimeField(
        db_column="wevh__dte01", blank=True, null=True
    )  # Field renamed because it contained more than one '_' in a row.
    wevh_dte02 = models.DateTimeField(
        db_column="wevh__dte02", blank=True, null=True
    )  # Field renamed because it contained more than one '_' in a row.
    wevh_log01 = models.BooleanField(
        db_column="wevh__log01", blank=True, null=True
    )  # Field renamed because it contained more than one '_' in a row.
    wevh_log02 = models.BooleanField(
        db_column="wevh__log02", blank=True, null=True
    )  # Field renamed because it contained more than one '_' in a row.
    pro2srcpdb = models.CharField(
        db_column="Pro2SrcPDB", max_length=12, blank=True, null=True
    )  # Field name made lowercase.
    pro2created = models.DateTimeField(blank=True, null=True)
    pro2modified = models.DateTimeField(blank=True, null=True)
    wevh_dataset = models.CharField(max_length=16, blank=True, null=True)
    wevh_from_part = models.CharField(max_length=36, blank=True, null=True)
    wevh_line = models.CharField(max_length=16, blank=True, null=True)
    wevh_loc_from = models.CharField(max_length=32, blank=True, null=True)
    wevh_loc_to = models.CharField(max_length=32, blank=True, null=True)
    wevh_lotser = models.CharField(max_length=36, blank=True, null=True)
    wevh_nbr = models.CharField(max_length=36, blank=True, null=True)
    wevh_pack = models.BooleanField(blank=True, null=True)
    wevh_ref = models.CharField(max_length=16, blank=True, null=True)
    wevh_ser = models.CharField(max_length=80, blank=True, null=True)
    wevh_storage_zone = models.CharField(max_length=32, blank=True, null=True)
    wevh_to_site = models.CharField(max_length=16, blank=True, null=True)
    wevh_to_whse = models.CharField(max_length=32, blank=True, null=True)
    wevh_work_zone = models.CharField(max_length=32, blank=True, null=True)
    wevh_zone_to = models.CharField(max_length=32, blank=True, null=True)

    class Meta:
        managed = False
        db_table = "wevh_hist"


class WtskMstr(models.Model):
    prrowid = models.CharField(primary_key=True, max_length=36)
    wtsk_domain = models.CharField(max_length=16, blank=True, null=True)
    wtsk_event_id = models.BigIntegerField(blank=True, null=True)
    wtsk_ev_sub_id = models.BigIntegerField(blank=True, null=True)
    wtsk_id = models.BigIntegerField(blank=True, null=True)
    wtsk_task_type = models.CharField(max_length=16, blank=True, null=True)
    wtsk_wave_id = models.BigIntegerField(blank=True, null=True)
    wtsk_incr = models.IntegerField(blank=True, null=True)
    wtsk_priority = models.IntegerField(blank=True, null=True)
    wtsk_from_whse = models.CharField(max_length=32, blank=True, null=True)
    wtsk_from_site = models.CharField(max_length=16, blank=True, null=True)
    wtsk_from_loc = models.CharField(max_length=16, blank=True, null=True)
    wtsk_from_part = models.CharField(max_length=36, blank=True, null=True)
    wtsk_from_lot = models.CharField(max_length=36, blank=True, null=True)
    wtsk_from_ref = models.CharField(max_length=16, blank=True, null=True)
    wtsk_from_serial_id = models.CharField(max_length=80, blank=True, null=True)
    wtsk_from_qty = models.DecimalField(
        max_digits=17, decimal_places=10, blank=True, null=True
    )
    wtsk_from_stor_zone = models.CharField(max_length=32, blank=True, null=True)
    wtsk_from_work_zone = models.CharField(max_length=32, blank=True, null=True)
    wtsk_from_pck_code = models.CharField(max_length=32, blank=True, null=True)
    wtsk_to_whse = models.CharField(max_length=32, blank=True, null=True)
    wtsk_to_site = models.CharField(max_length=16, blank=True, null=True)
    wtsk_to_loc = models.CharField(max_length=16, blank=True, null=True)
    wtsk_to_part = models.CharField(max_length=36, blank=True, null=True)
    wtsk_to_lot = models.CharField(max_length=36, blank=True, null=True)
    wtsk_to_ref = models.CharField(max_length=16, blank=True, null=True)
    wtsk_to_serial_id = models.CharField(max_length=80, blank=True, null=True)
    wtsk_to_qty = models.DecimalField(
        max_digits=17, decimal_places=10, blank=True, null=True
    )
    wtsk_to_stor_zone = models.CharField(max_length=32, blank=True, null=True)
    wtsk_to_work_zone = models.CharField(max_length=32, blank=True, null=True)
    wtsk_to_pck_code = models.CharField(max_length=32, blank=True, null=True)
    wtsk_task_status = models.CharField(max_length=16, blank=True, null=True)
    wtsk_reason = models.CharField(max_length=16, blank=True, null=True)
    wtsk_rmks = models.CharField(max_length=48, blank=True, null=True)
    wtsk_fail = models.BooleanField(blank=True, null=True)
    wtsk_hard_assign = models.BooleanField(blank=True, null=True)
    wtsk_routing = models.CharField(max_length=36, blank=True, null=True)
    wtsk_seq = models.IntegerField(blank=True, null=True)
    wtsk_orig_from_loc = models.CharField(max_length=16, blank=True, null=True)
    wtsk_orig_from_part = models.CharField(max_length=36, blank=True, null=True)
    wtsk_orig_from_lot = models.CharField(max_length=36, blank=True, null=True)
    wtsk_orig_from_ref = models.CharField(max_length=16, blank=True, null=True)
    wtsk_orig_from_serial_id = models.CharField(max_length=80, blank=True, null=True)
    wtsk_orig_to_loc = models.CharField(max_length=16, blank=True, null=True)
    wtsk_orig_to_part = models.CharField(max_length=36, blank=True, null=True)
    wtsk_orig_to_lot = models.CharField(max_length=36, blank=True, null=True)
    wtsk_orig_to_ref = models.CharField(max_length=16, blank=True, null=True)
    wtsk_orig_to_serial_id = models.CharField(max_length=80, blank=True, null=True)
    wtsk_ult_whse = models.CharField(max_length=32, blank=True, null=True)
    wtsk_ult_site = models.CharField(max_length=16, blank=True, null=True)
    wtsk_ult_area = models.CharField(max_length=16, blank=True, null=True)
    wtsk_ult_loc = models.CharField(max_length=16, blank=True, null=True)
    wtsk_qty_act = models.DecimalField(
        max_digits=17, decimal_places=10, blank=True, null=True
    )
    wtsk_qty_exp = models.DecimalField(
        max_digits=17, decimal_places=10, blank=True, null=True
    )
    wtsk_cmt_indx = models.IntegerField(blank=True, null=True)
    wtsk_mes_ref = models.BigIntegerField(blank=True, null=True)
    wtsk_create_prog = models.CharField(max_length=16, blank=True, null=True)
    wtsk_user_id = models.CharField(max_length=16, blank=True, null=True)
    wtsk_create_userid = models.CharField(max_length=16, blank=True, null=True)
    wtsk_create_date = models.DateTimeField(blank=True, null=True)
    wtsk_create_time = models.CharField(max_length=16, blank=True, null=True)
    wtsk_curr_userid = models.CharField(max_length=16, blank=True, null=True)
    wtsk_start_date = models.DateTimeField(blank=True, null=True)
    wtsk_start_time = models.CharField(max_length=16, blank=True, null=True)
    wtsk_end_date = models.DateTimeField(blank=True, null=True)
    wtsk_end_time = models.CharField(max_length=16, blank=True, null=True)
    wtsk_mod_userid = models.CharField(max_length=16, blank=True, null=True)
    wtsk_mod_date = models.DateTimeField(blank=True, null=True)
    wtsk_mod_time = models.CharField(max_length=16, blank=True, null=True)
    oid_wtsk_mstr = models.DecimalField(
        max_digits=38, decimal_places=10, blank=True, null=True
    )
    oid_wevd_det = models.DecimalField(
        max_digits=38, decimal_places=10, blank=True, null=True
    )
    wtsk_int01 = models.IntegerField(
        db_column="wtsk__int01", blank=True, null=True
    )  # Field renamed because it contained more than one '_' in a row.
    wtsk_chr01 = models.CharField(
        db_column="wtsk__chr01", max_length=48, blank=True, null=True
    )  # Field renamed because it contained more than one '_' in a row.
    wtsk_chr02 = models.CharField(
        db_column="wtsk__chr02", max_length=48, blank=True, null=True
    )  # Field renamed because it contained more than one '_' in a row.
    wtsk_chr03 = models.CharField(
        db_column="wtsk__chr03", max_length=48, blank=True, null=True
    )  # Field renamed because it contained more than one '_' in a row.
    wtsk_chr04 = models.CharField(
        db_column="wtsk__chr04", max_length=48, blank=True, null=True
    )  # Field renamed because it contained more than one '_' in a row.
    wtsk_dte02 = models.DateTimeField(
        db_column="wtsk__dte02", blank=True, null=True
    )  # Field renamed because it contained more than one '_' in a row.
    wtsk_log01 = models.BooleanField(
        db_column="wtsk__log01", blank=True, null=True
    )  # Field renamed because it contained more than one '_' in a row.
    wtsk_log02 = models.BooleanField(
        db_column="wtsk__log02", blank=True, null=True
    )  # Field renamed because it contained more than one '_' in a row.
    wtsk_int02 = models.IntegerField(
        db_column="wtsk__int02", blank=True, null=True
    )  # Field renamed because it contained more than one '_' in a row.
    wtsk_dec01 = models.DecimalField(
        db_column="wtsk__dec01", max_digits=17, decimal_places=2, blank=True, null=True
    )  # Field renamed because it contained more than one '_' in a row.
    wtsk_dec02 = models.DecimalField(
        db_column="wtsk__dec02", max_digits=17, decimal_places=2, blank=True, null=True
    )  # Field renamed because it contained more than one '_' in a row.
    wtsk_dte01 = models.DateTimeField(
        db_column="wtsk__dte01", blank=True, null=True
    )  # Field renamed because it contained more than one '_' in a row.
    pro2srcpdb = models.CharField(
        db_column="Pro2SrcPDB", max_length=12, blank=True, null=True
    )  # Field name made lowercase.
    pro2created = models.DateTimeField(blank=True, null=True)
    pro2modified = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = "wtsk_mstr"


class WtskhHist(models.Model):
    prrowid = models.CharField(primary_key=True, max_length=36)
    wtskh_domain = models.CharField(max_length=8, blank=True, null=True)
    wtskh_trnbr = models.BigIntegerField(blank=True, null=True)
    wtskh_task_id = models.BigIntegerField(blank=True, null=True)
    wtskh_event_id = models.BigIntegerField(blank=True, null=True)
    wtskh_ev_sub_id = models.BigIntegerField(blank=True, null=True)
    wtskh_nbr = models.CharField(max_length=8, blank=True, null=True)
    wtskh_line = models.CharField(max_length=8, blank=True, null=True)
    wtskh_from_whse = models.CharField(max_length=8, blank=True, null=True)
    wtskh_wave_id = models.BigIntegerField(blank=True, null=True)
    wtskh_type = models.CharField(max_length=8, blank=True, null=True)
    wtskh_from_site = models.CharField(max_length=8, blank=True, null=True)
    wtskh_from_loc = models.CharField(max_length=8, blank=True, null=True)
    wtskh_from_part = models.CharField(max_length=8, blank=True, null=True)
    wtskh_from_lot = models.CharField(max_length=8, blank=True, null=True)
    wtskh_from_ref = models.CharField(max_length=8, blank=True, null=True)
    wtskh_from_serial_id = models.CharField(max_length=8, blank=True, null=True)
    wtskh_qty_exp = models.DecimalField(
        max_digits=38, decimal_places=10, blank=True, null=True
    )
    wtskh_actual_qty = models.DecimalField(
        max_digits=38, decimal_places=10, blank=True, null=True
    )
    wtskh_to_whse = models.CharField(max_length=8, blank=True, null=True)
    wtskh_to_part = models.CharField(max_length=8, blank=True, null=True)
    wtskh_to_lot = models.CharField(max_length=8, blank=True, null=True)
    wtskh_to_ref = models.CharField(max_length=8, blank=True, null=True)
    wtskh_to_serial_id = models.CharField(max_length=8, blank=True, null=True)
    wtskh_storage_zone = models.CharField(max_length=8, blank=True, null=True)
    wtskh_work_zone = models.CharField(max_length=8, blank=True, null=True)
    wtskh_to_storage_zone = models.CharField(max_length=8, blank=True, null=True)
    wtskh_to_work_zone = models.CharField(max_length=8, blank=True, null=True)
    wtskh_status = models.CharField(max_length=8, blank=True, null=True)
    wtskh_userid = models.CharField(max_length=4, blank=True, null=True)
    wtskh_create_date = models.DateTimeField(blank=True, null=True)
    wtskh_create_time = models.CharField(max_length=16, blank=True, null=True)
    wtskh_reason = models.CharField(max_length=8, blank=True, null=True)
    wtskh_rmks = models.CharField(max_length=8, blank=True, null=True)
    wtskh_dc_trans_name = models.CharField(max_length=8, blank=True, null=True)
    wtskh_dc_trans_version = models.CharField(max_length=8, blank=True, null=True)
    oid_wtskh_hist = models.DecimalField(
        max_digits=38, decimal_places=10, blank=True, null=True
    )
    wtskh_mes_ref = models.BigIntegerField(blank=True, null=True)
    wtskh_to_site = models.CharField(max_length=8, blank=True, null=True)
    wtskh_to_loc = models.CharField(max_length=8, blank=True, null=True)
    wtskh_routing = models.CharField(max_length=36, blank=True, null=True)
    wtskh_start_date = models.DateTimeField(blank=True, null=True)
    wtskh_start_time = models.CharField(max_length=16, blank=True, null=True)
    wtskh_end_date = models.DateTimeField(blank=True, null=True)
    wtskh_end_time = models.CharField(max_length=16, blank=True, null=True)
    wtskh_mod_userid = models.CharField(max_length=4, blank=True, null=True)
    wtskh_mod_date = models.DateTimeField(blank=True, null=True)
    wtskh_mod_time = models.CharField(max_length=16, blank=True, null=True)
    wtskh_chr01 = models.CharField(
        db_column="wtskh__chr01", max_length=80, blank=True, null=True
    )  # Field renamed because it contained more than one '_' in a row.
    wtskh_chr02 = models.CharField(
        db_column="wtskh__chr02", max_length=80, blank=True, null=True
    )  # Field renamed because it contained more than one '_' in a row.
    wtskh_chr03 = models.CharField(
        db_column="wtskh__chr03", max_length=80, blank=True, null=True
    )  # Field renamed because it contained more than one '_' in a row.
    wtskh_chr04 = models.CharField(
        db_column="wtskh__chr04", max_length=80, blank=True, null=True
    )  # Field renamed because it contained more than one '_' in a row.
    wtskh_int01 = models.IntegerField(
        db_column="wtskh__int01", blank=True, null=True
    )  # Field renamed because it contained more than one '_' in a row.
    wtskh_int02 = models.IntegerField(
        db_column="wtskh__int02", blank=True, null=True
    )  # Field renamed because it contained more than one '_' in a row.
    wtskh_dec01 = models.DecimalField(
        db_column="wtskh__dec01",
        max_digits=38,
        decimal_places=10,
        blank=True,
        null=True,
    )  # Field renamed because it contained more than one '_' in a row.
    wtskh_dec02 = models.DecimalField(
        db_column="wtskh__dec02",
        max_digits=38,
        decimal_places=10,
        blank=True,
        null=True,
    )  # Field renamed because it contained more than one '_' in a row.
    wtskh_dte01 = models.DateTimeField(
        db_column="wtskh__dte01", blank=True, null=True
    )  # Field renamed because it contained more than one '_' in a row.
    wtskh_dte02 = models.DateTimeField(
        db_column="wtskh__dte02", blank=True, null=True
    )  # Field renamed because it contained more than one '_' in a row.
    wtskh_log01 = models.BooleanField(
        db_column="wtskh__log01", blank=True, null=True
    )  # Field renamed because it contained more than one '_' in a row.
    wtskh_log02 = models.BooleanField(
        db_column="wtskh__log02", blank=True, null=True
    )  # Field renamed because it contained more than one '_' in a row.
    pro2srcpdb = models.CharField(
        db_column="Pro2SrcPDB", max_length=12, blank=True, null=True
    )  # Field name made lowercase.
    pro2created = models.DateTimeField(blank=True, null=True)
    pro2modified = models.DateTimeField(blank=True, null=True)
    wtskh_cmt_indx = models.IntegerField(blank=True, null=True)
    wtskh_create_prog = models.CharField(max_length=16, blank=True, null=True)
    wtskh_curr_userid = models.CharField(max_length=16, blank=True, null=True)
    wtskh_fail = models.BooleanField(blank=True, null=True)
    wtskh_from_pck_code = models.CharField(max_length=32, blank=True, null=True)
    wtskh_from_qty = models.DecimalField(
        max_digits=25, decimal_places=10, blank=True, null=True
    )
    wtskh_orig_from_loc = models.CharField(max_length=16, blank=True, null=True)
    wtskh_orig_from_lot = models.CharField(max_length=36, blank=True, null=True)
    wtskh_orig_from_part = models.CharField(max_length=36, blank=True, null=True)
    wtskh_orig_from_ref = models.CharField(max_length=16, blank=True, null=True)
    wtskh_orig_from_serial_id = models.CharField(max_length=80, blank=True, null=True)
    wtskh_orig_to_loc = models.CharField(max_length=16, blank=True, null=True)
    wtskh_orig_to_lot = models.CharField(max_length=36, blank=True, null=True)
    wtskh_orig_to_part = models.CharField(max_length=36, blank=True, null=True)
    wtskh_orig_to_ref = models.CharField(max_length=16, blank=True, null=True)
    wtskh_orig_to_serial_id = models.CharField(max_length=80, blank=True, null=True)
    wtskh_priority = models.IntegerField(blank=True, null=True)
    wtskh_seq = models.IntegerField(blank=True, null=True)
    wtskh_to_pck_code = models.CharField(max_length=32, blank=True, null=True)
    wtskh_to_qty = models.DecimalField(
        max_digits=25, decimal_places=10, blank=True, null=True
    )
    wtskh_ult_area = models.CharField(max_length=16, blank=True, null=True)
    wtskh_ult_loc = models.CharField(max_length=16, blank=True, null=True)
    wtskh_ult_site = models.CharField(max_length=16, blank=True, null=True)
    wtskh_ult_whse = models.CharField(max_length=32, blank=True, null=True)
    wtskh_user_id = models.CharField(max_length=16, blank=True, null=True)

    class Meta:
        managed = False
        db_table = "wtskh_hist"


class XxusrwWkfl(models.Model):
    prrowid = models.CharField(primary_key=True, max_length=36)
    xxusrw_domain = models.CharField(max_length=9, blank=True, null=True)
    xxusrw_session = models.CharField(max_length=83, blank=True, null=True)
    xxusrw_key1 = models.CharField(max_length=80, blank=True, null=True)
    xxusrw_key2 = models.CharField(max_length=80, blank=True, null=True)
    xxusrw_key3 = models.CharField(max_length=80, blank=True, null=True)
    xxusrw_key4 = models.CharField(max_length=80, blank=True, null=True)
    xxusrw_key5 = models.CharField(max_length=80, blank=True, null=True)
    xxusrw_key6 = models.CharField(max_length=80, blank=True, null=True)
    xxusrw_charfld_1 = models.TextField(
        db_column="xxusrw_charfld##1", blank=True, null=True
    )  # Field renamed to remove unsuitable characters.
    xxusrw_charfld_2 = models.TextField(
        db_column="xxusrw_charfld##2", blank=True, null=True
    )  # Field renamed to remove unsuitable characters.
    xxusrw_charfld_3 = models.TextField(
        db_column="xxusrw_charfld##3", blank=True, null=True
    )  # Field renamed to remove unsuitable characters.
    xxusrw_charfld_4 = models.TextField(
        db_column="xxusrw_charfld##4", blank=True, null=True
    )  # Field renamed to remove unsuitable characters.
    xxusrw_charfld_5 = models.TextField(
        db_column="xxusrw_charfld##5", blank=True, null=True
    )  # Field renamed to remove unsuitable characters.
    xxusrw_charfld_6 = models.TextField(
        db_column="xxusrw_charfld##6", blank=True, null=True
    )  # Field renamed to remove unsuitable characters.
    xxusrw_charfld_7 = models.TextField(
        db_column="xxusrw_charfld##7", blank=True, null=True
    )  # Field renamed to remove unsuitable characters.
    xxusrw_charfld_8 = models.TextField(
        db_column="xxusrw_charfld##8", blank=True, null=True
    )  # Field renamed to remove unsuitable characters.
    xxusrw_charfld_9 = models.TextField(
        db_column="xxusrw_charfld##9", blank=True, null=True
    )  # Field renamed to remove unsuitable characters.
    xxusrw_charfld_10 = models.TextField(
        db_column="xxusrw_charfld##10", blank=True, null=True
    )  # Field renamed to remove unsuitable characters.
    xxusrw_charfld_11 = models.TextField(
        db_column="xxusrw_charfld##11", blank=True, null=True
    )  # Field renamed to remove unsuitable characters.
    xxusrw_charfld_12 = models.TextField(
        db_column="xxusrw_charfld##12", blank=True, null=True
    )  # Field renamed to remove unsuitable characters.
    xxusrw_charfld_13 = models.TextField(
        db_column="xxusrw_charfld##13", blank=True, null=True
    )  # Field renamed to remove unsuitable characters.
    xxusrw_charfld_14 = models.TextField(
        db_column="xxusrw_charfld##14", blank=True, null=True
    )  # Field renamed to remove unsuitable characters.
    xxusrw_charfld_15 = models.TextField(
        db_column="xxusrw_charfld##15", blank=True, null=True
    )  # Field renamed to remove unsuitable characters.
    xxusrw_decfld_1 = models.DecimalField(
        db_column="xxusrw_decfld##1",
        max_digits=38,
        decimal_places=10,
        blank=True,
        null=True,
    )  # Field renamed to remove unsuitable characters.
    xxusrw_decfld_2 = models.DecimalField(
        db_column="xxusrw_decfld##2",
        max_digits=38,
        decimal_places=10,
        blank=True,
        null=True,
    )  # Field renamed to remove unsuitable characters.
    xxusrw_decfld_3 = models.DecimalField(
        db_column="xxusrw_decfld##3",
        max_digits=38,
        decimal_places=10,
        blank=True,
        null=True,
    )  # Field renamed to remove unsuitable characters.
    xxusrw_decfld_4 = models.DecimalField(
        db_column="xxusrw_decfld##4",
        max_digits=38,
        decimal_places=10,
        blank=True,
        null=True,
    )  # Field renamed to remove unsuitable characters.
    xxusrw_decfld_5 = models.DecimalField(
        db_column="xxusrw_decfld##5",
        max_digits=38,
        decimal_places=10,
        blank=True,
        null=True,
    )  # Field renamed to remove unsuitable characters.
    xxusrw_decfld_6 = models.DecimalField(
        db_column="xxusrw_decfld##6",
        max_digits=38,
        decimal_places=10,
        blank=True,
        null=True,
    )  # Field renamed to remove unsuitable characters.
    xxusrw_decfld_7 = models.DecimalField(
        db_column="xxusrw_decfld##7",
        max_digits=38,
        decimal_places=10,
        blank=True,
        null=True,
    )  # Field renamed to remove unsuitable characters.
    xxusrw_decfld_8 = models.DecimalField(
        db_column="xxusrw_decfld##8",
        max_digits=38,
        decimal_places=10,
        blank=True,
        null=True,
    )  # Field renamed to remove unsuitable characters.
    xxusrw_decfld_9 = models.DecimalField(
        db_column="xxusrw_decfld##9",
        max_digits=38,
        decimal_places=10,
        blank=True,
        null=True,
    )  # Field renamed to remove unsuitable characters.
    xxusrw_decfld_10 = models.DecimalField(
        db_column="xxusrw_decfld##10",
        max_digits=38,
        decimal_places=10,
        blank=True,
        null=True,
    )  # Field renamed to remove unsuitable characters.
    xxusrw_decfld_11 = models.DecimalField(
        db_column="xxusrw_decfld##11",
        max_digits=38,
        decimal_places=10,
        blank=True,
        null=True,
    )  # Field renamed to remove unsuitable characters.
    xxusrw_decfld_12 = models.DecimalField(
        db_column="xxusrw_decfld##12",
        max_digits=38,
        decimal_places=10,
        blank=True,
        null=True,
    )  # Field renamed to remove unsuitable characters.
    xxusrw_decfld_13 = models.DecimalField(
        db_column="xxusrw_decfld##13",
        max_digits=38,
        decimal_places=10,
        blank=True,
        null=True,
    )  # Field renamed to remove unsuitable characters.
    xxusrw_decfld_14 = models.DecimalField(
        db_column="xxusrw_decfld##14",
        max_digits=38,
        decimal_places=10,
        blank=True,
        null=True,
    )  # Field renamed to remove unsuitable characters.
    xxusrw_decfld_15 = models.DecimalField(
        db_column="xxusrw_decfld##15",
        max_digits=38,
        decimal_places=10,
        blank=True,
        null=True,
    )  # Field renamed to remove unsuitable characters.
    xxusrw_intfld_1 = models.IntegerField(
        db_column="xxusrw_intfld##1", blank=True, null=True
    )  # Field renamed to remove unsuitable characters.
    xxusrw_intfld_2 = models.IntegerField(
        db_column="xxusrw_intfld##2", blank=True, null=True
    )  # Field renamed to remove unsuitable characters.
    xxusrw_intfld_3 = models.IntegerField(
        db_column="xxusrw_intfld##3", blank=True, null=True
    )  # Field renamed to remove unsuitable characters.
    xxusrw_intfld_4 = models.IntegerField(
        db_column="xxusrw_intfld##4", blank=True, null=True
    )  # Field renamed to remove unsuitable characters.
    xxusrw_intfld_5 = models.IntegerField(
        db_column="xxusrw_intfld##5", blank=True, null=True
    )  # Field renamed to remove unsuitable characters.
    xxusrw_intfld_6 = models.IntegerField(
        db_column="xxusrw_intfld##6", blank=True, null=True
    )  # Field renamed to remove unsuitable characters.
    xxusrw_intfld_7 = models.IntegerField(
        db_column="xxusrw_intfld##7", blank=True, null=True
    )  # Field renamed to remove unsuitable characters.
    xxusrw_intfld_8 = models.IntegerField(
        db_column="xxusrw_intfld##8", blank=True, null=True
    )  # Field renamed to remove unsuitable characters.
    xxusrw_intfld_9 = models.IntegerField(
        db_column="xxusrw_intfld##9", blank=True, null=True
    )  # Field renamed to remove unsuitable characters.
    xxusrw_intfld_10 = models.IntegerField(
        db_column="xxusrw_intfld##10", blank=True, null=True
    )  # Field renamed to remove unsuitable characters.
    xxusrw_intfld_11 = models.IntegerField(
        db_column="xxusrw_intfld##11", blank=True, null=True
    )  # Field renamed to remove unsuitable characters.
    xxusrw_intfld_12 = models.IntegerField(
        db_column="xxusrw_intfld##12", blank=True, null=True
    )  # Field renamed to remove unsuitable characters.
    xxusrw_intfld_13 = models.IntegerField(
        db_column="xxusrw_intfld##13", blank=True, null=True
    )  # Field renamed to remove unsuitable characters.
    xxusrw_intfld_14 = models.IntegerField(
        db_column="xxusrw_intfld##14", blank=True, null=True
    )  # Field renamed to remove unsuitable characters.
    xxusrw_intfld_15 = models.IntegerField(
        db_column="xxusrw_intfld##15", blank=True, null=True
    )  # Field renamed to remove unsuitable characters.
    xxusrw_datefld_1 = models.DateTimeField(
        db_column="xxusrw_datefld##1", blank=True, null=True
    )  # Field renamed to remove unsuitable characters.
    xxusrw_datefld_2 = models.DateTimeField(
        db_column="xxusrw_datefld##2", blank=True, null=True
    )  # Field renamed to remove unsuitable characters.
    xxusrw_datefld_3 = models.DateTimeField(
        db_column="xxusrw_datefld##3", blank=True, null=True
    )  # Field renamed to remove unsuitable characters.
    xxusrw_datefld_4 = models.DateTimeField(
        db_column="xxusrw_datefld##4", blank=True, null=True
    )  # Field renamed to remove unsuitable characters.
    xxusrw_datefld_5 = models.DateTimeField(
        db_column="xxusrw_datefld##5", blank=True, null=True
    )  # Field renamed to remove unsuitable characters.
    xxusrw_datefld_6 = models.DateTimeField(
        db_column="xxusrw_datefld##6", blank=True, null=True
    )  # Field renamed to remove unsuitable characters.
    xxusrw_datefld_7 = models.DateTimeField(
        db_column="xxusrw_datefld##7", blank=True, null=True
    )  # Field renamed to remove unsuitable characters.
    xxusrw_datefld_8 = models.DateTimeField(
        db_column="xxusrw_datefld##8", blank=True, null=True
    )  # Field renamed to remove unsuitable characters.
    xxusrw_datefld_9 = models.DateTimeField(
        db_column="xxusrw_datefld##9", blank=True, null=True
    )  # Field renamed to remove unsuitable characters.
    xxusrw_datefld_10 = models.DateTimeField(
        db_column="xxusrw_datefld##10", blank=True, null=True
    )  # Field renamed to remove unsuitable characters.
    xxusrw_datefld_11 = models.DateTimeField(
        db_column="xxusrw_datefld##11", blank=True, null=True
    )  # Field renamed to remove unsuitable characters.
    xxusrw_datefld_12 = models.DateTimeField(
        db_column="xxusrw_datefld##12", blank=True, null=True
    )  # Field renamed to remove unsuitable characters.
    xxusrw_datefld_13 = models.DateTimeField(
        db_column="xxusrw_datefld##13", blank=True, null=True
    )  # Field renamed to remove unsuitable characters.
    xxusrw_datefld_14 = models.DateTimeField(
        db_column="xxusrw_datefld##14", blank=True, null=True
    )  # Field renamed to remove unsuitable characters.
    xxusrw_datefld_15 = models.DateTimeField(
        db_column="xxusrw_datefld##15", blank=True, null=True
    )  # Field renamed to remove unsuitable characters.
    xxusrw_logfld_1 = models.BooleanField(
        db_column="xxusrw_logfld##1", blank=True, null=True
    )  # Field renamed to remove unsuitable characters.
    xxusrw_logfld_2 = models.BooleanField(
        db_column="xxusrw_logfld##2", blank=True, null=True
    )  # Field renamed to remove unsuitable characters.
    xxusrw_logfld_3 = models.BooleanField(
        db_column="xxusrw_logfld##3", blank=True, null=True
    )  # Field renamed to remove unsuitable characters.
    xxusrw_logfld_4 = models.BooleanField(
        db_column="xxusrw_logfld##4", blank=True, null=True
    )  # Field renamed to remove unsuitable characters.
    xxusrw_logfld_5 = models.BooleanField(
        db_column="xxusrw_logfld##5", blank=True, null=True
    )  # Field renamed to remove unsuitable characters.
    xxusrw_logfld_6 = models.BooleanField(
        db_column="xxusrw_logfld##6", blank=True, null=True
    )  # Field renamed to remove unsuitable characters.
    xxusrw_logfld_7 = models.BooleanField(
        db_column="xxusrw_logfld##7", blank=True, null=True
    )  # Field renamed to remove unsuitable characters.
    xxusrw_logfld_8 = models.BooleanField(
        db_column="xxusrw_logfld##8", blank=True, null=True
    )  # Field renamed to remove unsuitable characters.
    xxusrw_logfld_9 = models.BooleanField(
        db_column="xxusrw_logfld##9", blank=True, null=True
    )  # Field renamed to remove unsuitable characters.
    xxusrw_logfld_10 = models.BooleanField(
        db_column="xxusrw_logfld##10", blank=True, null=True
    )  # Field renamed to remove unsuitable characters.
    xxusrw_logfld_11 = models.BooleanField(
        db_column="xxusrw_logfld##11", blank=True, null=True
    )  # Field renamed to remove unsuitable characters.
    xxusrw_logfld_12 = models.BooleanField(
        db_column="xxusrw_logfld##12", blank=True, null=True
    )  # Field renamed to remove unsuitable characters.
    xxusrw_logfld_13 = models.BooleanField(
        db_column="xxusrw_logfld##13", blank=True, null=True
    )  # Field renamed to remove unsuitable characters.
    xxusrw_logfld_14 = models.BooleanField(
        db_column="xxusrw_logfld##14", blank=True, null=True
    )  # Field renamed to remove unsuitable characters.
    xxusrw_logfld_15 = models.BooleanField(
        db_column="xxusrw_logfld##15", blank=True, null=True
    )  # Field renamed to remove unsuitable characters.
    xxusrw_user1 = models.CharField(max_length=80, blank=True, null=True)
    xxusrw_user2 = models.CharField(max_length=80, blank=True, null=True)
    oid_xxusrw_wkfl = models.DecimalField(
        max_digits=38, decimal_places=10, blank=True, null=True
    )
    xxusrw_chr01_1 = models.CharField(
        db_column="xxusrw__chr01##1", max_length=90, blank=True, null=True
    )  # Field renamed to remove unsuitable characters. Field renamed because it contained more than one '_' in a row.
    xxusrw_chr01_2 = models.CharField(
        db_column="xxusrw__chr01##2", max_length=90, blank=True, null=True
    )  # Field renamed to remove unsuitable characters. Field renamed because it contained more than one '_' in a row.
    xxusrw_chr01_3 = models.CharField(
        db_column="xxusrw__chr01##3", max_length=90, blank=True, null=True
    )  # Field renamed to remove unsuitable characters. Field renamed because it contained more than one '_' in a row.
    xxusrw_chr01_4 = models.CharField(
        db_column="xxusrw__chr01##4", max_length=90, blank=True, null=True
    )  # Field renamed to remove unsuitable characters. Field renamed because it contained more than one '_' in a row.
    xxusrw_chr01_5 = models.CharField(
        db_column="xxusrw__chr01##5", max_length=90, blank=True, null=True
    )  # Field renamed to remove unsuitable characters. Field renamed because it contained more than one '_' in a row.
    xxusrw_dec01_1 = models.DecimalField(
        db_column="xxusrw__dec01##1",
        max_digits=38,
        decimal_places=10,
        blank=True,
        null=True,
    )  # Field renamed to remove unsuitable characters. Field renamed because it contained more than one '_' in a row.
    xxusrw_dec01_2 = models.DecimalField(
        db_column="xxusrw__dec01##2",
        max_digits=38,
        decimal_places=10,
        blank=True,
        null=True,
    )  # Field renamed to remove unsuitable characters. Field renamed because it contained more than one '_' in a row.
    xxusrw_dec01_3 = models.DecimalField(
        db_column="xxusrw__dec01##3",
        max_digits=38,
        decimal_places=10,
        blank=True,
        null=True,
    )  # Field renamed to remove unsuitable characters. Field renamed because it contained more than one '_' in a row.
    xxusrw_dec01_4 = models.DecimalField(
        db_column="xxusrw__dec01##4",
        max_digits=38,
        decimal_places=10,
        blank=True,
        null=True,
    )  # Field renamed to remove unsuitable characters. Field renamed because it contained more than one '_' in a row.
    xxusrw_dec01_5 = models.DecimalField(
        db_column="xxusrw__dec01##5",
        max_digits=38,
        decimal_places=10,
        blank=True,
        null=True,
    )  # Field renamed to remove unsuitable characters. Field renamed because it contained more than one '_' in a row.
    xxusrw_log01_1 = models.BooleanField(
        db_column="xxusrw__log01##1", blank=True, null=True
    )  # Field renamed to remove unsuitable characters. Field renamed because it contained more than one '_' in a row.
    xxusrw_log01_2 = models.BooleanField(
        db_column="xxusrw__log01##2", blank=True, null=True
    )  # Field renamed to remove unsuitable characters. Field renamed because it contained more than one '_' in a row.
    xxusrw_log01_3 = models.BooleanField(
        db_column="xxusrw__log01##3", blank=True, null=True
    )  # Field renamed to remove unsuitable characters. Field renamed because it contained more than one '_' in a row.
    xxusrw_log01_4 = models.BooleanField(
        db_column="xxusrw__log01##4", blank=True, null=True
    )  # Field renamed to remove unsuitable characters. Field renamed because it contained more than one '_' in a row.
    xxusrw_log01_5 = models.BooleanField(
        db_column="xxusrw__log01##5", blank=True, null=True
    )  # Field renamed to remove unsuitable characters. Field renamed because it contained more than one '_' in a row.
    xxusrw_dte01_1 = models.DateTimeField(
        db_column="xxusrw__dte01##1", blank=True, null=True
    )  # Field renamed to remove unsuitable characters. Field renamed because it contained more than one '_' in a row.
    xxusrw_dte01_2 = models.DateTimeField(
        db_column="xxusrw__dte01##2", blank=True, null=True
    )  # Field renamed to remove unsuitable characters. Field renamed because it contained more than one '_' in a row.
    xxusrw_dte01_3 = models.DateTimeField(
        db_column="xxusrw__dte01##3", blank=True, null=True
    )  # Field renamed to remove unsuitable characters. Field renamed because it contained more than one '_' in a row.
    xxusrw_dte01_4 = models.DateTimeField(
        db_column="xxusrw__dte01##4", blank=True, null=True
    )  # Field renamed to remove unsuitable characters. Field renamed because it contained more than one '_' in a row.
    xxusrw_dte01_5 = models.DateTimeField(
        db_column="xxusrw__dte01##5", blank=True, null=True
    )  # Field renamed to remove unsuitable characters. Field renamed because it contained more than one '_' in a row.
    xxusrw_int01_1 = models.IntegerField(
        db_column="xxusrw__int01##1", blank=True, null=True
    )  # Field renamed to remove unsuitable characters. Field renamed because it contained more than one '_' in a row.
    xxusrw_int01_2 = models.IntegerField(
        db_column="xxusrw__int01##2", blank=True, null=True
    )  # Field renamed to remove unsuitable characters. Field renamed because it contained more than one '_' in a row.
    xxusrw_int01_3 = models.IntegerField(
        db_column="xxusrw__int01##3", blank=True, null=True
    )  # Field renamed to remove unsuitable characters. Field renamed because it contained more than one '_' in a row.
    xxusrw_int01_4 = models.IntegerField(
        db_column="xxusrw__int01##4", blank=True, null=True
    )  # Field renamed to remove unsuitable characters. Field renamed because it contained more than one '_' in a row.
    xxusrw_int01_5 = models.IntegerField(
        db_column="xxusrw__int01##5", blank=True, null=True
    )  # Field renamed to remove unsuitable characters. Field renamed because it contained more than one '_' in a row.
    pro2srcpdb = models.CharField(
        db_column="Pro2SrcPDB", max_length=12, blank=True, null=True
    )  # Field name made lowercase.
    pro2created = models.DateTimeField(blank=True, null=True)
    pro2modified = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = "xxusrw_wkfl"


class WoMstr(models.Model):
    prrowid = models.CharField(max_length=36)
    wo_nbr = models.CharField(max_length=30, blank=True, null=True)
    wo_lot = models.CharField(max_length=80, blank=True, null=True)
    wo_so_job = models.CharField(max_length=80, blank=True, null=True)
    wo_ord_date = models.DateTimeField(blank=True, null=True)
    wo_rel_date = models.DateTimeField(blank=True, null=True)
    wo_due_date = models.DateTimeField(blank=True, null=True)
    wo_per_date = models.DateTimeField(blank=True, null=True)
    wo_part = models.CharField(max_length=30, blank=True, null=True)
    wo_type = models.CharField(max_length=30, blank=True, null=True)
    wo_qty_ord = models.DecimalField(
        max_digits=38, decimal_places=10, blank=True, null=True
    )
    wo_qty_comp = models.DecimalField(
        max_digits=38, decimal_places=10, blank=True, null=True
    )
    wo_qty_rjct = models.DecimalField(
        max_digits=38, decimal_places=10, blank=True, null=True
    )
    wo_status = models.CharField(max_length=30, blank=True, null=True)
    wo_vend = models.CharField(max_length=80, blank=True, null=True)
    wo_rmks = models.CharField(max_length=80, blank=True, null=True)
    wo_qty_chg = models.DecimalField(
        max_digits=38, decimal_places=10, blank=True, null=True
    )
    wo_rjct_chg = models.DecimalField(
        max_digits=38, decimal_places=10, blank=True, null=True
    )
    wo_bo_chg = models.DecimalField(
        max_digits=38, decimal_places=10, blank=True, null=True
    )
    wo_yield_pct = models.DecimalField(
        max_digits=38, decimal_places=10, blank=True, null=True
    )
    wo_rev = models.CharField(max_length=30, blank=True, null=True)
    wo_acct = models.CharField(max_length=20, blank=True, null=True)
    wo_cc = models.CharField(max_length=20, blank=True, null=True)
    wo_qad01 = models.CharField(
        db_column="wo__qad01", max_length=80, blank=True, null=True
    )  # Field renamed because it contained more than one '_' in a row.
    wo_lot_prev = models.CharField(max_length=80, blank=True, null=True)
    wo_schd_type = models.CharField(max_length=30, blank=True, null=True)
    wo_cmtindx = models.IntegerField(blank=True, null=True)
    wo_project = models.CharField(max_length=20, blank=True, null=True)
    wo_lead_time = models.IntegerField(blank=True, null=True)
    wo_wip_tot = models.DecimalField(
        max_digits=38, decimal_places=10, blank=True, null=True
    )
    wo_lbr_tot = models.DecimalField(
        max_digits=38, decimal_places=10, blank=True, null=True
    )
    wo_mtl_tot = models.DecimalField(
        max_digits=38, decimal_places=10, blank=True, null=True
    )
    wo_bdn_tot = models.DecimalField(
        max_digits=38, decimal_places=10, blank=True, null=True
    )
    wo_sub_tot = models.DecimalField(
        max_digits=38, decimal_places=10, blank=True, null=True
    )
    wo_user1 = models.CharField(max_length=80, blank=True, null=True)
    wo_user2 = models.CharField(max_length=80, blank=True, null=True)
    wo_ovh_tot = models.DecimalField(
        max_digits=38, decimal_places=10, blank=True, null=True
    )
    wo_loc = models.CharField(max_length=80, blank=True, null=True)
    wo_serial = models.CharField(max_length=50, blank=True, null=True)
    wo_routing = models.CharField(max_length=30, blank=True, null=True)
    wo_bom_code = models.CharField(max_length=30, blank=True, null=True)
    wo_site = models.CharField(max_length=80, blank=True, null=True)
    wo_queue_eff = models.DecimalField(
        max_digits=38, decimal_places=10, blank=True, null=True
    )
    wo_draw = models.CharField(max_length=30, blank=True, null=True)
    wo_lbr_up = models.BooleanField(blank=True, null=True)
    wo_bdn_up = models.BooleanField(blank=True, null=True)
    wo_gl_lbr = models.BooleanField(blank=True, null=True)
    wo_gl_bdn = models.BooleanField(blank=True, null=True)
    wo_chr01 = models.CharField(
        db_column="wo__chr01", max_length=80, blank=True, null=True
    )  # Field renamed because it contained more than one '_' in a row.
    wo_chr02 = models.CharField(
        db_column="wo__chr02", max_length=80, blank=True, null=True
    )  # Field renamed because it contained more than one '_' in a row.
    wo_chr03 = models.CharField(
        db_column="wo__chr03", max_length=80, blank=True, null=True
    )  # Field renamed because it contained more than one '_' in a row.
    wo_chr04 = models.CharField(
        db_column="wo__chr04", max_length=80, blank=True, null=True
    )  # Field renamed because it contained more than one '_' in a row.
    wo_chr05 = models.CharField(
        db_column="wo__chr05", max_length=80, blank=True, null=True
    )  # Field renamed because it contained more than one '_' in a row.
    wo_dte01 = models.DateTimeField(
        db_column="wo__dte01", blank=True, null=True
    )  # Field renamed because it contained more than one '_' in a row.
    wo_dte02 = models.DateTimeField(
        db_column="wo__dte02", blank=True, null=True
    )  # Field renamed because it contained more than one '_' in a row.
    wo_dec01 = models.DecimalField(
        db_column="wo__dec01", max_digits=38, decimal_places=10, blank=True, null=True
    )  # Field renamed because it contained more than one '_' in a row.
    wo_dec02 = models.DecimalField(
        db_column="wo__dec02", max_digits=38, decimal_places=10, blank=True, null=True
    )  # Field renamed because it contained more than one '_' in a row.
    wo_log01 = models.BooleanField(
        db_column="wo__log01", blank=True, null=True
    )  # Field renamed because it contained more than one '_' in a row.
    wo_line = models.CharField(max_length=80, blank=True, null=True)
    wo_var = models.BooleanField(blank=True, null=True)
    wo_mtl_var = models.DecimalField(
        max_digits=38, decimal_places=10, blank=True, null=True
    )
    wo_lbr_var = models.DecimalField(
        max_digits=38, decimal_places=10, blank=True, null=True
    )
    wo_bdn_var = models.DecimalField(
        max_digits=38, decimal_places=10, blank=True, null=True
    )
    wo_sub_var = models.DecimalField(
        max_digits=38, decimal_places=10, blank=True, null=True
    )
    wo_mvar_acct = models.CharField(max_length=20, blank=True, null=True)
    wo_mvar_cc = models.CharField(max_length=20, blank=True, null=True)
    wo_mvrr_acct = models.CharField(max_length=20, blank=True, null=True)
    wo_mvrr_cc = models.CharField(max_length=20, blank=True, null=True)
    wo_svar_acct = models.CharField(max_length=20, blank=True, null=True)
    wo_svar_cc = models.CharField(max_length=20, blank=True, null=True)
    wo_svrr_acct = models.CharField(max_length=20, blank=True, null=True)
    wo_svrr_cc = models.CharField(max_length=20, blank=True, null=True)
    wo_flr_acct = models.CharField(max_length=20, blank=True, null=True)
    wo_flr_cc = models.CharField(max_length=20, blank=True, null=True)
    wo_dec03 = models.DecimalField(
        db_column="wo__dec03", max_digits=38, decimal_places=10, blank=True, null=True
    )  # Field renamed because it contained more than one '_' in a row.
    wo_rjct_tot = models.DecimalField(
        max_digits=38, decimal_places=10, blank=True, null=True
    )
    wo_mthd_var = models.DecimalField(
        max_digits=38, decimal_places=10, blank=True, null=True
    )
    wo_rval_tot = models.DecimalField(
        max_digits=38, decimal_places=10, blank=True, null=True
    )
    wo_acct_close = models.BooleanField(blank=True, null=True)
    wo_close_date = models.DateTimeField(blank=True, null=True)
    wo_close_eff = models.DateTimeField(blank=True, null=True)
    wo_fsm_type = models.CharField(max_length=80, blank=True, null=True)
    wo_xvar_acct = models.CharField(max_length=20, blank=True, null=True)
    wo_xvar_cc = models.CharField(max_length=20, blank=True, null=True)
    wo_myld_var = models.DecimalField(
        max_digits=38, decimal_places=10, blank=True, null=True
    )
    wo_joint_type = models.CharField(max_length=30, blank=True, null=True)
    wo_prod_pct = models.DecimalField(
        max_digits=38, decimal_places=10, blank=True, null=True
    )
    wo_qty_type = models.CharField(max_length=30, blank=True, null=True)
    wo_dec04 = models.DecimalField(
        db_column="wo__dec04", max_digits=38, decimal_places=10, blank=True, null=True
    )  # Field renamed because it contained more than one '_' in a row.
    wo_base_id = models.CharField(max_length=80, blank=True, null=True)
    wo_unit_cost = models.DecimalField(
        max_digits=38, decimal_places=10, blank=True, null=True
    )
    wo_mix_var = models.DecimalField(
        max_digits=38, decimal_places=10, blank=True, null=True
    )
    wo_bdn_totx = models.DecimalField(
        max_digits=38, decimal_places=10, blank=True, null=True
    )
    wo_lbr_totx = models.DecimalField(
        max_digits=38, decimal_places=10, blank=True, null=True
    )
    wo_mtl_totx = models.DecimalField(
        max_digits=38, decimal_places=10, blank=True, null=True
    )
    wo_sub_totx = models.DecimalField(
        max_digits=38, decimal_places=10, blank=True, null=True
    )
    wo_ovh_totx = models.DecimalField(
        max_digits=38, decimal_places=10, blank=True, null=True
    )
    wo_rctstat_active = models.BooleanField(blank=True, null=True)
    wo_batch = models.CharField(max_length=30, blank=True, null=True)
    wo_assay = models.DecimalField(
        max_digits=38, decimal_places=10, blank=True, null=True
    )
    wo_grade = models.CharField(max_length=30, blank=True, null=True)
    wo_expire = models.DateTimeField(blank=True, null=True)
    wo_rctstat = models.CharField(max_length=80, blank=True, null=True)
    wo_lot_next = models.CharField(max_length=30, blank=True, null=True)
    wo_lot_rcpt = models.BooleanField(blank=True, null=True)
    wo_ca_int_type = models.CharField(max_length=80, blank=True, null=True)
    wo_iss_site = models.CharField(max_length=80, blank=True, null=True)
    wo_itm_line = models.IntegerField(blank=True, null=True)
    wo_date_posted = models.DateTimeField(blank=True, null=True)
    wo_qadc01 = models.CharField(
        db_column="wo__qadc01", max_length=80, blank=True, null=True
    )  # Field renamed because it contained more than one '_' in a row.
    wo_qadc02 = models.CharField(
        db_column="wo__qadc02", max_length=80, blank=True, null=True
    )  # Field renamed because it contained more than one '_' in a row.
    wo_qadc03 = models.CharField(
        db_column="wo__qadc03", max_length=80, blank=True, null=True
    )  # Field renamed because it contained more than one '_' in a row.
    wo_qadt01 = models.DateTimeField(
        db_column="wo__qadt01", blank=True, null=True
    )  # Field renamed because it contained more than one '_' in a row.
    wo_qadt02 = models.DateTimeField(
        db_column="wo__qadt02", blank=True, null=True
    )  # Field renamed because it contained more than one '_' in a row.
    wo_qade01 = models.DecimalField(
        db_column="wo__qade01", max_digits=38, decimal_places=10, blank=True, null=True
    )  # Field renamed because it contained more than one '_' in a row.
    wo_qade02 = models.DecimalField(
        db_column="wo__qade02", max_digits=38, decimal_places=10, blank=True, null=True
    )  # Field renamed because it contained more than one '_' in a row.
    wo_qade03 = models.DecimalField(
        db_column="wo__qade03", max_digits=38, decimal_places=10, blank=True, null=True
    )  # Field renamed because it contained more than one '_' in a row.
    wo_qadi01 = models.IntegerField(
        db_column="wo__qadi01", blank=True, null=True
    )  # Field renamed because it contained more than one '_' in a row.
    wo_qadi02 = models.IntegerField(
        db_column="wo__qadi02", blank=True, null=True
    )  # Field renamed because it contained more than one '_' in a row.
    wo_qadl01 = models.BooleanField(
        db_column="wo__qadl01", blank=True, null=True
    )  # Field renamed because it contained more than one '_' in a row.
    wo_qadl02 = models.BooleanField(
        db_column="wo__qadl02", blank=True, null=True
    )  # Field renamed because it contained more than one '_' in a row.
    wo_eng_code = models.CharField(max_length=80, blank=True, null=True)
    wo_sub = models.CharField(max_length=20, blank=True, null=True)
    wo_flr_sub = models.CharField(max_length=20, blank=True, null=True)
    wo_mvar_sub = models.CharField(max_length=20, blank=True, null=True)
    wo_mvrr_sub = models.CharField(max_length=20, blank=True, null=True)
    wo_svar_sub = models.CharField(max_length=20, blank=True, null=True)
    wo_svrr_sub = models.CharField(max_length=20, blank=True, null=True)
    wo_xvar_sub = models.CharField(max_length=20, blank=True, null=True)
    wo_ref = models.CharField(max_length=80, blank=True, null=True)
    wo_record_date = models.DateTimeField(blank=True, null=True)
    wo_stat_close_date = models.DateTimeField(blank=True, null=True)
    wo_stat_close_userid = models.CharField(max_length=80, blank=True, null=True)
    wo_app_owner = models.CharField(max_length=30, blank=True, null=True)
    wo_domain = models.CharField(max_length=8, blank=True, null=True)
    oid_wo_mstr = models.DecimalField(
        max_digits=38, decimal_places=10, blank=True, null=True
    )
    wo_doc_id = models.CharField(max_length=24, blank=True, null=True)
    wo_rate = models.DecimalField(
        max_digits=38, decimal_places=10, blank=True, null=True
    )
    wo_selected_for_print = models.BooleanField(blank=True, null=True)
    wo_seq = models.DecimalField(max_digits=20, decimal_places=2, blank=True, null=True)
    wo_shift = models.CharField(max_length=2, blank=True, null=True)
    wo_order_sheet_printed = models.BooleanField(blank=True, null=True)
    wo_setup_time = models.IntegerField(blank=True, null=True)
    wo_due_date_anchor = models.BooleanField(blank=True, null=True)
    wo_tool = models.CharField(max_length=8, blank=True, null=True)
    wo_run_size = models.IntegerField(blank=True, null=True)
    wo_nbr_lines = models.DecimalField(
        max_digits=20, decimal_places=2, blank=True, null=True
    )
    wo_duration_buffer = models.IntegerField(blank=True, null=True)
    wo_qty_booked = models.IntegerField(blank=True, null=True)
    wo_need_date = models.DateTimeField(blank=True, null=True)
    wo_priority = models.IntegerField(blank=True, null=True)
    wo_restriction = models.CharField(max_length=8, blank=True, null=True)
    wo_allow_splits = models.BooleanField(blank=True, null=True)
    wo_qty_exp_complete = models.DecimalField(
        max_digits=38, decimal_places=10, blank=True, null=True
    )
    wo_qty_exp_scrap = models.DecimalField(
        max_digits=38, decimal_places=10, blank=True, null=True
    )
    wo_mfg_type = models.CharField(max_length=1, blank=True, null=True)
    wo_cum_lot_id = models.CharField(max_length=80, blank=True, null=True)
    wo_need_time = models.IntegerField(blank=True, null=True)
    wo_mps_auto_reschedule = models.BooleanField(blank=True, null=True)
    oid_wo_demand = models.DecimalField(
        max_digits=38, decimal_places=10, blank=True, null=True
    )
    wo_demand_dataset = models.CharField(max_length=30, blank=True, null=True)
    pro2srcpdb = models.CharField(
        db_column="Pro2SrcPDB", max_length=12, blank=True, null=True
    )  # Field name made lowercase.
    pro2created = models.DateTimeField(blank=True, null=True)
    pro2modified = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False  # Created from a view. Don't remove.
        db_table = "wo_mstr"


class InMstr(models.Model):
    prrowid = models.CharField(max_length=36)
    in_part = models.CharField(max_length=30, blank=True, null=True)
    in_site = models.CharField(max_length=80, blank=True, null=True)
    in_qty_oh = models.DecimalField(
        max_digits=38, decimal_places=10, blank=True, null=True
    )
    in_qty_req = models.DecimalField(
        max_digits=38, decimal_places=10, blank=True, null=True
    )
    in_qty_all = models.DecimalField(
        max_digits=38, decimal_places=10, blank=True, null=True
    )
    in_qty_ord = models.DecimalField(
        max_digits=38, decimal_places=10, blank=True, null=True
    )
    in_qty_chg = models.DecimalField(
        max_digits=38, decimal_places=10, blank=True, null=True
    )
    in_qty_avail = models.DecimalField(
        max_digits=38, decimal_places=10, blank=True, null=True
    )
    in_sls_chg = models.DecimalField(
        max_digits=38, decimal_places=10, blank=True, null=True
    )
    in_iss_chg = models.DecimalField(
        max_digits=38, decimal_places=10, blank=True, null=True
    )
    in_iss_date = models.DateTimeField(blank=True, null=True)
    in_rec_date = models.DateTimeField(blank=True, null=True)
    in_cnt_date = models.DateTimeField(blank=True, null=True)
    in_avg_iss = models.DecimalField(
        max_digits=38, decimal_places=10, blank=True, null=True
    )
    in_avg_sls = models.DecimalField(
        max_digits=38, decimal_places=10, blank=True, null=True
    )
    in_avg_date = models.DateTimeField(blank=True, null=True)
    in_user1 = models.CharField(max_length=80, blank=True, null=True)
    in_user2 = models.CharField(max_length=80, blank=True, null=True)
    in_rop = models.DecimalField(max_digits=20, decimal_places=0, blank=True, null=True)
    in_sfty_stk = models.DecimalField(
        max_digits=20, decimal_places=0, blank=True, null=True
    )
    in_qty_nonet = models.DecimalField(
        max_digits=38, decimal_places=10, blank=True, null=True
    )
    in_mrp = models.BooleanField(blank=True, null=True)
    in_gl_set = models.CharField(max_length=80, blank=True, null=True)
    in_cur_set = models.CharField(max_length=80, blank=True, null=True)
    in_qadc02 = models.CharField(
        db_column="in__qadc02", max_length=80, blank=True, null=True
    )  # Field renamed because it contained more than one '_' in a row.
    in_qadi01 = models.IntegerField(
        db_column="in__qadi01", blank=True, null=True
    )  # Field renamed because it contained more than one '_' in a row.
    in_qadi02 = models.IntegerField(
        db_column="in__qadi02", blank=True, null=True
    )  # Field renamed because it contained more than one '_' in a row.
    in_level = models.IntegerField(blank=True, null=True)
    in_loc = models.CharField(max_length=80, blank=True, null=True)
    in_loc_type = models.CharField(max_length=80, blank=True, null=True)
    in_proj_use = models.IntegerField(blank=True, null=True)
    in_grade = models.CharField(max_length=30, blank=True, null=True)
    in_assay = models.DecimalField(
        max_digits=38, decimal_places=10, blank=True, null=True
    )
    in_rollup = models.BooleanField(blank=True, null=True)
    in_rollup_id = models.CharField(max_length=80, blank=True, null=True)
    in_qadc03 = models.CharField(
        db_column="in__qadc03", max_length=80, blank=True, null=True
    )  # Field renamed because it contained more than one '_' in a row.
    in_qadc04 = models.CharField(
        db_column="in__qadc04", max_length=80, blank=True, null=True
    )  # Field renamed because it contained more than one '_' in a row.
    in_qadl01 = models.BooleanField(
        db_column="in__qadl01", blank=True, null=True
    )  # Field renamed because it contained more than one '_' in a row.
    in_qadl02 = models.BooleanField(
        db_column="in__qadl02", blank=True, null=True
    )  # Field renamed because it contained more than one '_' in a row.
    in_qadc01 = models.CharField(
        db_column="in__qadc01", max_length=80, blank=True, null=True
    )  # Field renamed because it contained more than one '_' in a row.
    in_wh = models.BooleanField(blank=True, null=True)
    in_gl_cost_site = models.CharField(max_length=80, blank=True, null=True)
    in_cust_consign_qty = models.DecimalField(
        max_digits=38, decimal_places=10, blank=True, null=True
    )
    in_supp_consign_qty = models.DecimalField(
        max_digits=38, decimal_places=10, blank=True, null=True
    )
    in_domain = models.CharField(max_length=8, blank=True, null=True)
    oid_in_mstr = models.DecimalField(
        max_digits=38, decimal_places=10, blank=True, null=True
    )
    pro2srcpdb = models.CharField(
        db_column="Pro2SrcPDB", max_length=12, blank=True, null=True
    )  # Field name made lowercase.
    pro2created = models.DateTimeField(blank=True, null=True)
    pro2modified = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False  # Created from a view. Don't remove.
        db_table = "in_mstr"


class LdDet(models.Model):
    prrowid = models.CharField(max_length=36)
    ld_loc = models.CharField(max_length=80, blank=True, null=True)
    ld_part = models.CharField(max_length=30, blank=True, null=True)
    ld_date = models.DateTimeField(blank=True, null=True)
    ld_qty_oh = models.DecimalField(
        max_digits=38, decimal_places=10, blank=True, null=True
    )
    ld_lot = models.CharField(max_length=30, blank=True, null=True)
    ld_ref = models.CharField(max_length=80, blank=True, null=True)
    ld_cnt_date = models.DateTimeField(blank=True, null=True)
    ld_assay = models.DecimalField(
        max_digits=38, decimal_places=10, blank=True, null=True
    )
    ld_expire = models.DateTimeField(blank=True, null=True)
    ld_user1 = models.CharField(max_length=80, blank=True, null=True)
    ld_user2 = models.CharField(max_length=80, blank=True, null=True)
    ld_site = models.CharField(max_length=80, blank=True, null=True)
    ld_status = models.CharField(max_length=80, blank=True, null=True)
    ld_qty_all = models.DecimalField(
        max_digits=38, decimal_places=10, blank=True, null=True
    )
    ld_grade = models.CharField(max_length=30, blank=True, null=True)
    ld_qty_frz = models.DecimalField(
        max_digits=38, decimal_places=10, blank=True, null=True
    )
    ld_date_frz = models.DateTimeField(blank=True, null=True)
    ld_vd_lot = models.CharField(max_length=30, blank=True, null=True)
    ld_cmtindx = models.IntegerField(blank=True, null=True)
    ld_work = models.DecimalField(
        max_digits=38, decimal_places=10, blank=True, null=True
    )
    ld_chr01 = models.CharField(
        db_column="ld__chr01", max_length=80, blank=True, null=True
    )  # Field renamed because it contained more than one '_' in a row.
    ld_chr02 = models.CharField(
        db_column="ld__chr02", max_length=80, blank=True, null=True
    )  # Field renamed because it contained more than one '_' in a row.
    ld_chr03 = models.CharField(
        db_column="ld__chr03", max_length=80, blank=True, null=True
    )  # Field renamed because it contained more than one '_' in a row.
    ld_chr04 = models.CharField(
        db_column="ld__chr04", max_length=80, blank=True, null=True
    )  # Field renamed because it contained more than one '_' in a row.
    ld_chr05 = models.CharField(
        db_column="ld__chr05", max_length=80, blank=True, null=True
    )  # Field renamed because it contained more than one '_' in a row.
    ld_dte01 = models.DateTimeField(
        db_column="ld__dte01", blank=True, null=True
    )  # Field renamed because it contained more than one '_' in a row.
    ld_dte02 = models.DateTimeField(
        db_column="ld__dte02", blank=True, null=True
    )  # Field renamed because it contained more than one '_' in a row.
    ld_dec01 = models.DecimalField(
        db_column="ld__dec01", max_digits=38, decimal_places=10, blank=True, null=True
    )  # Field renamed because it contained more than one '_' in a row.
    ld_dec02 = models.DecimalField(
        db_column="ld__dec02", max_digits=38, decimal_places=10, blank=True, null=True
    )  # Field renamed because it contained more than one '_' in a row.
    ld_log01 = models.BooleanField(
        db_column="ld__log01", blank=True, null=True
    )  # Field renamed because it contained more than one '_' in a row.
    ld_cost = models.DecimalField(
        max_digits=38, decimal_places=10, blank=True, null=True
    )
    ld_rev = models.CharField(max_length=30, blank=True, null=True)
    ld_cust_consign_qty = models.DecimalField(
        max_digits=38, decimal_places=10, blank=True, null=True
    )
    ld_supp_consign_qty = models.DecimalField(
        max_digits=38, decimal_places=10, blank=True, null=True
    )
    ld_domain = models.CharField(max_length=8, blank=True, null=True)
    oid_ld_det = models.DecimalField(
        max_digits=38, decimal_places=10, blank=True, null=True
    )
    ld_alt_um = models.CharField(max_length=30, blank=True, null=True)
    ld_crt_time = models.IntegerField(blank=True, null=True)
    ld_crt_date = models.DateTimeField(blank=True, null=True)
    ld_exp_qtyin = models.DecimalField(
        max_digits=38, decimal_places=10, blank=True, null=True
    )
    ld_exp_qtyout = models.DecimalField(
        max_digits=38, decimal_places=10, blank=True, null=True
    )
    ld_time_frz = models.IntegerField(blank=True, null=True)
    pro2srcpdb = models.CharField(
        db_column="L", max_length=12, blank=True, null=True
    )  # Field name made lowercase.
    pro2created = models.DateTimeField(blank=True, null=True)
    pro2modified = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False  # Created from a view. Don't remove.
        db_table = "ld_det"


class SerMstr(models.Model):
    prrowid = models.CharField(max_length=36)
    ser_domain = models.CharField(max_length=8, blank=True, null=True)
    ser_serial_id = models.CharField(max_length=40, blank=True, null=True)
    oid_ser_mstr_parent = models.DecimalField(
        max_digits=38, decimal_places=10, blank=True, null=True
    )
    ser_stage = models.CharField(max_length=10, blank=True, null=True)
    ser_pack_code = models.CharField(max_length=18, blank=True, null=True)
    ser_prt_lbl = models.BooleanField(blank=True, null=True)
    oid_loc_mstr = models.DecimalField(
        max_digits=38, decimal_places=10, blank=True, null=True
    )
    ser_site = models.CharField(max_length=80, blank=True, null=True)
    ser_loc = models.CharField(max_length=30, blank=True, null=True)
    ser_part = models.CharField(max_length=30, blank=True, null=True)
    ser_lotser = models.CharField(max_length=30, blank=True, null=True)
    ser_ref = models.CharField(max_length=80, blank=True, null=True)
    ser_qty_pck = models.DecimalField(
        max_digits=38, decimal_places=10, blank=True, null=True
    )
    ser_qty_avail = models.DecimalField(
        max_digits=38, decimal_places=10, blank=True, null=True
    )
    ser_um = models.CharField(max_length=30, blank=True, null=True)
    ser_mod_userid = models.CharField(max_length=80, blank=True, null=True)
    ser_mod_date = models.DateTimeField(blank=True, null=True)
    ser_user1 = models.CharField(max_length=80, blank=True, null=True)
    ser_user2 = models.CharField(max_length=80, blank=True, null=True)
    ser_qadc01 = models.CharField(
        db_column="ser__qadc01", max_length=80, blank=True, null=True
    )  # Field renamed because it contained more than one '_' in a row.
    ser_qadc02 = models.CharField(
        db_column="ser__qadc02", max_length=80, blank=True, null=True
    )  # Field renamed because it contained more than one '_' in a row.
    oid_ser_mstr = models.DecimalField(
        max_digits=38, decimal_places=10, blank=True, null=True
    )
    ser_ship_wt = models.DecimalField(
        max_digits=38, decimal_places=10, blank=True, null=True
    )
    ser_ship_wt_um = models.CharField(max_length=30, blank=True, null=True)
    ser_size = models.DecimalField(
        max_digits=20, decimal_places=10, blank=True, null=True
    )
    ser_size_um = models.CharField(max_length=30, blank=True, null=True)
    oid_ld_det = models.DecimalField(
        max_digits=38, decimal_places=10, blank=True, null=True
    )
    ser_truck_loaded = models.BooleanField(blank=True, null=True)
    ser_gross_weight = models.DecimalField(
        max_digits=38, decimal_places=10, blank=True, null=True
    )
    ser_gross_weight_um = models.CharField(max_length=30, blank=True, null=True)
    ser_unloaded = models.BooleanField(blank=True, null=True)
    ser_phantom = models.BooleanField(blank=True, null=True)
    ser_vend_lot = models.CharField(max_length=30, blank=True, null=True)
    ser_ext_sn_id = models.CharField(max_length=40, blank=True, null=True)
    ser_commission_date = models.DateTimeField(blank=True, null=True)
    ser_origin_code = models.CharField(max_length=16, blank=True, null=True)
    pro2srcpdb = models.CharField(
        db_column="Pro2SrcPDB", max_length=12, blank=True, null=True
    )  # Field name made lowercase.
    pro2created = models.DateTimeField(blank=True, null=True)
    pro2modified = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False  # Created from a view. Don't remove.
        db_table = "ser_mstr"


class SctDet(models.Model):
    prrowid = models.CharField(max_length=36)
    sct_sim = models.CharField(max_length=80, blank=True, null=True)
    sct_part = models.CharField(max_length=30, blank=True, null=True)
    sct_cst_tot = models.DecimalField(
        max_digits=38, decimal_places=10, blank=True, null=True
    )
    sct_mtl_tl = models.DecimalField(
        max_digits=38, decimal_places=10, blank=True, null=True
    )
    sct_lbr_tl = models.DecimalField(
        max_digits=38, decimal_places=10, blank=True, null=True
    )
    sct_bdn_tl = models.DecimalField(
        max_digits=38, decimal_places=10, blank=True, null=True
    )
    sct_ovh_tl = models.DecimalField(
        max_digits=38, decimal_places=10, blank=True, null=True
    )
    sct_sub_tl = models.DecimalField(
        max_digits=38, decimal_places=10, blank=True, null=True
    )
    sct_mtl_ll = models.DecimalField(
        max_digits=38, decimal_places=10, blank=True, null=True
    )
    sct_lbr_ll = models.DecimalField(
        max_digits=38, decimal_places=10, blank=True, null=True
    )
    sct_bdn_ll = models.DecimalField(
        max_digits=38, decimal_places=10, blank=True, null=True
    )
    sct_ovh_ll = models.DecimalField(
        max_digits=38, decimal_places=10, blank=True, null=True
    )
    sct_sub_ll = models.DecimalField(
        max_digits=38, decimal_places=10, blank=True, null=True
    )
    sct_cst_date = models.DateTimeField(blank=True, null=True)
    sct_user1 = models.CharField(max_length=80, blank=True, null=True)
    sct_user2 = models.CharField(max_length=80, blank=True, null=True)
    sct_serial = models.CharField(max_length=50, blank=True, null=True)
    sct_site = models.CharField(max_length=80, blank=True, null=True)
    sct_rollup = models.BooleanField(blank=True, null=True)
    sct_rollup_id = models.CharField(max_length=30, blank=True, null=True)
    sct_nrv = models.DecimalField(
        max_digits=38, decimal_places=10, blank=True, null=True
    )
    sct_qadc01 = models.CharField(
        db_column="sct__qadc01", max_length=80, blank=True, null=True
    )  # Field renamed because it contained more than one '_' in a row.
    sct_cost_changed = models.BooleanField(blank=True, null=True)
    sct_domain = models.CharField(max_length=8, blank=True, null=True)
    oid_sct_det = models.DecimalField(
        max_digits=38, decimal_places=10, blank=True, null=True
    )
    pro2srcpdb = models.CharField(
        db_column="Pro2SrcPDB", max_length=12, blank=True, null=True
    )  # Field name made lowercase.
    pro2created = models.DateTimeField(blank=True, null=True)
    pro2modified = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False  # Created from a view. Don't remove.
        db_table = "sct_det"
