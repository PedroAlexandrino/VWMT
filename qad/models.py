from django.db import models

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
    wtsk_from_qty = models.DecimalField(max_digits=17, decimal_places=10, blank=True, null=True)
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
    wtsk_to_qty = models.DecimalField(max_digits=17, decimal_places=10, blank=True, null=True)
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
    wtsk_qty_act = models.DecimalField(max_digits=17, decimal_places=10, blank=True, null=True)
    wtsk_qty_exp = models.DecimalField(max_digits=17, decimal_places=10, blank=True, null=True)
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
    oid_wtsk_mstr = models.DecimalField(max_digits=38, decimal_places=10, blank=True, null=True)
    oid_wevd_det = models.DecimalField(max_digits=38, decimal_places=10, blank=True, null=True)
    wtsk_int01 = models.IntegerField(db_column='wtsk__int01', blank=True, null=True)  # Field renamed because it contained more than one '_' in a row.
    wtsk_chr01 = models.CharField(db_column='wtsk__chr01', max_length=48, blank=True, null=True)  # Field renamed because it contained more than one '_' in a row.
    wtsk_chr02 = models.CharField(db_column='wtsk__chr02', max_length=48, blank=True, null=True)  # Field renamed because it contained more than one '_' in a row.
    wtsk_chr03 = models.CharField(db_column='wtsk__chr03', max_length=48, blank=True, null=True)  # Field renamed because it contained more than one '_' in a row.
    wtsk_chr04 = models.CharField(db_column='wtsk__chr04', max_length=48, blank=True, null=True)  # Field renamed because it contained more than one '_' in a row.
    wtsk_dte02 = models.DateTimeField(db_column='wtsk__dte02', blank=True, null=True)  # Field renamed because it contained more than one '_' in a row.
    wtsk_log01 = models.BooleanField(db_column='wtsk__log01', blank=True, null=True)  # Field renamed because it contained more than one '_' in a row.
    wtsk_log02 = models.BooleanField(db_column='wtsk__log02', blank=True, null=True)  # Field renamed because it contained more than one '_' in a row.
    wtsk_int02 = models.IntegerField(db_column='wtsk__int02', blank=True, null=True)  # Field renamed because it contained more than one '_' in a row.
    wtsk_dec01 = models.DecimalField(db_column='wtsk__dec01', max_digits=17, decimal_places=2, blank=True, null=True)  # Field renamed because it contained more than one '_' in a row.
    wtsk_dec02 = models.DecimalField(db_column='wtsk__dec02', max_digits=17, decimal_places=2, blank=True, null=True)  # Field renamed because it contained more than one '_' in a row.
    wtsk_dte01 = models.DateTimeField(db_column='wtsk__dte01', blank=True, null=True)  # Field renamed because it contained more than one '_' in a row.
    pro2srcpdb = models.CharField(db_column='Pro2SrcPDB', max_length=12, blank=True, null=True)  # Field name made lowercase.
    pro2created = models.DateTimeField(blank=True, null=True)
    pro2modified = models.DateTimeField(blank=True, null=True)

    class Meta:
        db_table = 'wtsk_mstr'

    # TO STRING METHOD
    def __str__(self):
        return f"{self.wtsk_id}"


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
    wtskh_qty_exp = models.DecimalField(max_digits=38, decimal_places=10, blank=True, null=True)
    wtskh_actual_qty = models.DecimalField(max_digits=38, decimal_places=10, blank=True, null=True)
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
    oid_wtskh_hist = models.DecimalField(max_digits=38, decimal_places=10, blank=True, null=True)
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
    wtskh_chr01 = models.CharField(db_column='wtskh__chr01', max_length=80, blank=True, null=True)  # Field renamed because it contained more than one '_' in a row.
    wtskh_chr02 = models.CharField(db_column='wtskh__chr02', max_length=80, blank=True, null=True)  # Field renamed because it contained more than one '_' in a row.
    wtskh_chr03 = models.CharField(db_column='wtskh__chr03', max_length=80, blank=True, null=True)  # Field renamed because it contained more than one '_' in a row.
    wtskh_chr04 = models.CharField(db_column='wtskh__chr04', max_length=80, blank=True, null=True)  # Field renamed because it contained more than one '_' in a row.
    wtskh_int01 = models.IntegerField(db_column='wtskh__int01', blank=True, null=True)  # Field renamed because it contained more than one '_' in a row.
    wtskh_int02 = models.IntegerField(db_column='wtskh__int02', blank=True, null=True)  # Field renamed because it contained more than one '_' in a row.
    wtskh_dec01 = models.DecimalField(db_column='wtskh__dec01', max_digits=38, decimal_places=10, blank=True, null=True)  # Field renamed because it contained more than one '_' in a row.
    wtskh_dec02 = models.DecimalField(db_column='wtskh__dec02', max_digits=38, decimal_places=10, blank=True, null=True)  # Field renamed because it contained more than one '_' in a row.
    wtskh_dte01 = models.DateTimeField(db_column='wtskh__dte01', blank=True, null=True)  # Field renamed because it contained more than one '_' in a row.
    wtskh_dte02 = models.DateTimeField(db_column='wtskh__dte02', blank=True, null=True)  # Field renamed because it contained more than one '_' in a row.
    wtskh_log01 = models.BooleanField(db_column='wtskh__log01', blank=True, null=True)  # Field renamed because it contained more than one '_' in a row.
    wtskh_log02 = models.BooleanField(db_column='wtskh__log02', blank=True, null=True)  # Field renamed because it contained more than one '_' in a row.
    pro2srcpdb = models.CharField(db_column='Pro2SrcPDB', max_length=12, blank=True, null=True)  # Field name made lowercase.
    pro2created = models.DateTimeField(blank=True, null=True)
    pro2modified = models.DateTimeField(blank=True, null=True)
    wtskh_cmt_indx = models.IntegerField(blank=True, null=True)
    wtskh_create_prog = models.CharField(max_length=16, blank=True, null=True)
    wtskh_curr_userid = models.CharField(max_length=16, blank=True, null=True)
    wtskh_fail = models.BooleanField(blank=True, null=True)
    wtskh_from_pck_code = models.CharField(max_length=32, blank=True, null=True)
    wtskh_from_qty = models.DecimalField(max_digits=25, decimal_places=10, blank=True, null=True)
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
    wtskh_to_qty = models.DecimalField(max_digits=25, decimal_places=10, blank=True, null=True)
    wtskh_ult_area = models.CharField(max_length=16, blank=True, null=True)
    wtskh_ult_loc = models.CharField(max_length=16, blank=True, null=True)
    wtskh_ult_site = models.CharField(max_length=16, blank=True, null=True)
    wtskh_ult_whse = models.CharField(max_length=32, blank=True, null=True)
    wtskh_user_id = models.CharField(max_length=16, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'wtskh_hist'

    # TO STRING METHOD
    def __str__(self):
        return f"{self.wtskh_user_id}"


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
    xxusrw_charfld_1 = models.TextField(db_column='xxusrw_charfld##1', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    xxusrw_charfld_2 = models.TextField(db_column='xxusrw_charfld##2', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    xxusrw_charfld_3 = models.TextField(db_column='xxusrw_charfld##3', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    xxusrw_charfld_4 = models.TextField(db_column='xxusrw_charfld##4', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    xxusrw_charfld_5 = models.TextField(db_column='xxusrw_charfld##5', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    xxusrw_charfld_6 = models.TextField(db_column='xxusrw_charfld##6', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    xxusrw_charfld_7 = models.TextField(db_column='xxusrw_charfld##7', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    xxusrw_charfld_8 = models.TextField(db_column='xxusrw_charfld##8', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    xxusrw_charfld_9 = models.TextField(db_column='xxusrw_charfld##9', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    xxusrw_charfld_10 = models.TextField(db_column='xxusrw_charfld##10', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    xxusrw_charfld_11 = models.TextField(db_column='xxusrw_charfld##11', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    xxusrw_charfld_12 = models.TextField(db_column='xxusrw_charfld##12', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    xxusrw_charfld_13 = models.TextField(db_column='xxusrw_charfld##13', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    xxusrw_charfld_14 = models.TextField(db_column='xxusrw_charfld##14', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    xxusrw_charfld_15 = models.TextField(db_column='xxusrw_charfld##15', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    xxusrw_decfld_1 = models.DecimalField(db_column='xxusrw_decfld##1', max_digits=38, decimal_places=10, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    xxusrw_decfld_2 = models.DecimalField(db_column='xxusrw_decfld##2', max_digits=38, decimal_places=10, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    xxusrw_decfld_3 = models.DecimalField(db_column='xxusrw_decfld##3', max_digits=38, decimal_places=10, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    xxusrw_decfld_4 = models.DecimalField(db_column='xxusrw_decfld##4', max_digits=38, decimal_places=10, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    xxusrw_decfld_5 = models.DecimalField(db_column='xxusrw_decfld##5', max_digits=38, decimal_places=10, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    xxusrw_decfld_6 = models.DecimalField(db_column='xxusrw_decfld##6', max_digits=38, decimal_places=10, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    xxusrw_decfld_7 = models.DecimalField(db_column='xxusrw_decfld##7', max_digits=38, decimal_places=10, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    xxusrw_decfld_8 = models.DecimalField(db_column='xxusrw_decfld##8', max_digits=38, decimal_places=10, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    xxusrw_decfld_9 = models.DecimalField(db_column='xxusrw_decfld##9', max_digits=38, decimal_places=10, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    xxusrw_decfld_10 = models.DecimalField(db_column='xxusrw_decfld##10', max_digits=38, decimal_places=10, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    xxusrw_decfld_11 = models.DecimalField(db_column='xxusrw_decfld##11', max_digits=38, decimal_places=10, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    xxusrw_decfld_12 = models.DecimalField(db_column='xxusrw_decfld##12', max_digits=38, decimal_places=10, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    xxusrw_decfld_13 = models.DecimalField(db_column='xxusrw_decfld##13', max_digits=38, decimal_places=10, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    xxusrw_decfld_14 = models.DecimalField(db_column='xxusrw_decfld##14', max_digits=38, decimal_places=10, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    xxusrw_decfld_15 = models.DecimalField(db_column='xxusrw_decfld##15', max_digits=38, decimal_places=10, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    xxusrw_intfld_1 = models.IntegerField(db_column='xxusrw_intfld##1', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    xxusrw_intfld_2 = models.IntegerField(db_column='xxusrw_intfld##2', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    xxusrw_intfld_3 = models.IntegerField(db_column='xxusrw_intfld##3', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    xxusrw_intfld_4 = models.IntegerField(db_column='xxusrw_intfld##4', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    xxusrw_intfld_5 = models.IntegerField(db_column='xxusrw_intfld##5', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    xxusrw_intfld_6 = models.IntegerField(db_column='xxusrw_intfld##6', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    xxusrw_intfld_7 = models.IntegerField(db_column='xxusrw_intfld##7', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    xxusrw_intfld_8 = models.IntegerField(db_column='xxusrw_intfld##8', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    xxusrw_intfld_9 = models.IntegerField(db_column='xxusrw_intfld##9', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    xxusrw_intfld_10 = models.IntegerField(db_column='xxusrw_intfld##10', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    xxusrw_intfld_11 = models.IntegerField(db_column='xxusrw_intfld##11', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    xxusrw_intfld_12 = models.IntegerField(db_column='xxusrw_intfld##12', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    xxusrw_intfld_13 = models.IntegerField(db_column='xxusrw_intfld##13', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    xxusrw_intfld_14 = models.IntegerField(db_column='xxusrw_intfld##14', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    xxusrw_intfld_15 = models.IntegerField(db_column='xxusrw_intfld##15', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    xxusrw_datefld_1 = models.DateTimeField(db_column='xxusrw_datefld##1', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    xxusrw_datefld_2 = models.DateTimeField(db_column='xxusrw_datefld##2', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    xxusrw_datefld_3 = models.DateTimeField(db_column='xxusrw_datefld##3', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    xxusrw_datefld_4 = models.DateTimeField(db_column='xxusrw_datefld##4', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    xxusrw_datefld_5 = models.DateTimeField(db_column='xxusrw_datefld##5', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    xxusrw_datefld_6 = models.DateTimeField(db_column='xxusrw_datefld##6', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    xxusrw_datefld_7 = models.DateTimeField(db_column='xxusrw_datefld##7', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    xxusrw_datefld_8 = models.DateTimeField(db_column='xxusrw_datefld##8', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    xxusrw_datefld_9 = models.DateTimeField(db_column='xxusrw_datefld##9', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    xxusrw_datefld_10 = models.DateTimeField(db_column='xxusrw_datefld##10', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    xxusrw_datefld_11 = models.DateTimeField(db_column='xxusrw_datefld##11', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    xxusrw_datefld_12 = models.DateTimeField(db_column='xxusrw_datefld##12', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    xxusrw_datefld_13 = models.DateTimeField(db_column='xxusrw_datefld##13', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    xxusrw_datefld_14 = models.DateTimeField(db_column='xxusrw_datefld##14', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    xxusrw_datefld_15 = models.DateTimeField(db_column='xxusrw_datefld##15', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    xxusrw_logfld_1 = models.BooleanField(db_column='xxusrw_logfld##1', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    xxusrw_logfld_2 = models.BooleanField(db_column='xxusrw_logfld##2', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    xxusrw_logfld_3 = models.BooleanField(db_column='xxusrw_logfld##3', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    xxusrw_logfld_4 = models.BooleanField(db_column='xxusrw_logfld##4', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    xxusrw_logfld_5 = models.BooleanField(db_column='xxusrw_logfld##5', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    xxusrw_logfld_6 = models.BooleanField(db_column='xxusrw_logfld##6', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    xxusrw_logfld_7 = models.BooleanField(db_column='xxusrw_logfld##7', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    xxusrw_logfld_8 = models.BooleanField(db_column='xxusrw_logfld##8', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    xxusrw_logfld_9 = models.BooleanField(db_column='xxusrw_logfld##9', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    xxusrw_logfld_10 = models.BooleanField(db_column='xxusrw_logfld##10', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    xxusrw_logfld_11 = models.BooleanField(db_column='xxusrw_logfld##11', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    xxusrw_logfld_12 = models.BooleanField(db_column='xxusrw_logfld##12', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    xxusrw_logfld_13 = models.BooleanField(db_column='xxusrw_logfld##13', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    xxusrw_logfld_14 = models.BooleanField(db_column='xxusrw_logfld##14', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    xxusrw_logfld_15 = models.BooleanField(db_column='xxusrw_logfld##15', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    xxusrw_user1 = models.CharField(max_length=80, blank=True, null=True)
    xxusrw_user2 = models.CharField(max_length=80, blank=True, null=True)
    oid_xxusrw_wkfl = models.DecimalField(max_digits=38, decimal_places=10, blank=True, null=True)
    xxusrw_chr01_1 = models.CharField(db_column='xxusrw__chr01##1', max_length=90, blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it contained more than one '_' in a row.
    xxusrw_chr01_2 = models.CharField(db_column='xxusrw__chr01##2', max_length=90, blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it contained more than one '_' in a row.
    xxusrw_chr01_3 = models.CharField(db_column='xxusrw__chr01##3', max_length=90, blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it contained more than one '_' in a row.
    xxusrw_chr01_4 = models.CharField(db_column='xxusrw__chr01##4', max_length=90, blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it contained more than one '_' in a row.
    xxusrw_chr01_5 = models.CharField(db_column='xxusrw__chr01##5', max_length=90, blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it contained more than one '_' in a row.
    xxusrw_dec01_1 = models.DecimalField(db_column='xxusrw__dec01##1', max_digits=38, decimal_places=10, blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it contained more than one '_' in a row.
    xxusrw_dec01_2 = models.DecimalField(db_column='xxusrw__dec01##2', max_digits=38, decimal_places=10, blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it contained more than one '_' in a row.
    xxusrw_dec01_3 = models.DecimalField(db_column='xxusrw__dec01##3', max_digits=38, decimal_places=10, blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it contained more than one '_' in a row.
    xxusrw_dec01_4 = models.DecimalField(db_column='xxusrw__dec01##4', max_digits=38, decimal_places=10, blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it contained more than one '_' in a row.
    xxusrw_dec01_5 = models.DecimalField(db_column='xxusrw__dec01##5', max_digits=38, decimal_places=10, blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it contained more than one '_' in a row.
    xxusrw_log01_1 = models.BooleanField(db_column='xxusrw__log01##1', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it contained more than one '_' in a row.
    xxusrw_log01_2 = models.BooleanField(db_column='xxusrw__log01##2', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it contained more than one '_' in a row.
    xxusrw_log01_3 = models.BooleanField(db_column='xxusrw__log01##3', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it contained more than one '_' in a row.
    xxusrw_log01_4 = models.BooleanField(db_column='xxusrw__log01##4', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it contained more than one '_' in a row.
    xxusrw_log01_5 = models.BooleanField(db_column='xxusrw__log01##5', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it contained more than one '_' in a row.
    xxusrw_dte01_1 = models.DateTimeField(db_column='xxusrw__dte01##1', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it contained more than one '_' in a row.
    xxusrw_dte01_2 = models.DateTimeField(db_column='xxusrw__dte01##2', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it contained more than one '_' in a row.
    xxusrw_dte01_3 = models.DateTimeField(db_column='xxusrw__dte01##3', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it contained more than one '_' in a row.
    xxusrw_dte01_4 = models.DateTimeField(db_column='xxusrw__dte01##4', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it contained more than one '_' in a row.
    xxusrw_dte01_5 = models.DateTimeField(db_column='xxusrw__dte01##5', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it contained more than one '_' in a row.
    xxusrw_int01_1 = models.IntegerField(db_column='xxusrw__int01##1', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it contained more than one '_' in a row.
    xxusrw_int01_2 = models.IntegerField(db_column='xxusrw__int01##2', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it contained more than one '_' in a row.
    xxusrw_int01_3 = models.IntegerField(db_column='xxusrw__int01##3', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it contained more than one '_' in a row.
    xxusrw_int01_4 = models.IntegerField(db_column='xxusrw__int01##4', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it contained more than one '_' in a row.
    xxusrw_int01_5 = models.IntegerField(db_column='xxusrw__int01##5', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it contained more than one '_' in a row.
    pro2srcpdb = models.CharField(db_column='Pro2SrcPDB', max_length=12, blank=True, null=True)  # Field name made lowercase.
    pro2created = models.DateTimeField(blank=True, null=True)
    pro2modified = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'xxusrw_wkfl'

    # TO STRING METHOD
    def __str__(self):
        return f"{self.prrowid}"
