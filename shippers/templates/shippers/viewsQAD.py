# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class WevMstrVw(models.Model):
    prrowid = models.CharField(max_length=36)
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
        managed = False  # Created from a view. Don't remove.
        db_table = "wev_mstr_vw"


class WevdDetVw(models.Model):
    prrowid = models.CharField(max_length=36)
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
        managed = False  # Created from a view. Don't remove.
        db_table = "wevd_det_vw"
