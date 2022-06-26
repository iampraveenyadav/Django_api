from django.db import models

 #Create your models here.
class UserServicesChtghFinal(models.Model):
    #id = models.BigIntegerField(db_column='ID', blank=True, null=True)  # Field name made lowercase.
    user_id = models.BigIntegerField(db_column='USER_ID', blank=True, null=True)  # Field name made lowercase.
    arn = models.TextField(db_column='ARN', blank=True, null=True)  # Field name made lowercase.
    application_id = models.FloatField(db_column='APPLICATION_ID', blank=True, null=True)  # Field name made lowercase.
    created_on = models.DateTimeField(db_column='CREATED_ON', blank=True, null=True)  # Field name made lowercase.
    modified_on = models.DateTimeField(db_column='MODIFIED_ON', blank=True, null=True)  # Field name made lowercase.
    product_id = models.BigIntegerField(db_column='PRODUCT_ID', blank=True, null=True)  # Field name made lowercase.
    user_geography_id = models.FloatField(db_column='USER_GEOGRAPHY_ID', blank=True, null=True)  # Field name made lowercase.
    form_id = models.BigIntegerField(db_column='FORM_ID', blank=True, null=True)  # Field name made lowercase.
    state = models.TextField(db_column='STATE', blank=True, null=True)  # Field name made lowercase.
    district = models.TextField(db_column='DISTRICT', blank=True, null=True)  # Field name made lowercase.
    tehsil_id = models.FloatField(db_column='TEHSIL_ID', blank=True, null=True)  # Field name made lowercase.
    scheme_name = models.TextField(db_column='SCHEME_NAME', blank=True, null=True)  # Field name made lowercase.
    corporation = models.TextField(db_column='CORPORATION', blank=True, null=True)  # Field name made lowercase.
    department = models.TextField(db_column='DEPARTMENT', blank=True, null=True)  # Field name made lowercase.
    application_status = models.TextField(db_column='APPLICATION_STATUS', blank=True, null=True)  # Field name made lowercase.
    role_sla = models.FloatField(db_column='ROLE_SLA', blank=True, null=True)  # Field name made lowercase.
    limit_status = models.TextField(db_column='LIMIT_STATUS', blank=True, null=True)  # Field name made lowercase.
    dsc_role_id = models.FloatField(db_column='DSC_ROLE_ID', blank=True, null=True)  # Field name made lowercase.
    dsc_role = models.TextField(db_column='DSC_ROLE', blank=True, null=True)  # Field name made lowercase.
    dsc_name = models.TextField(db_column='DSC_NAME', blank=True, null=True)  # Field name made lowercase.
    dsc_user_id = models.FloatField(db_column='DSC_USER_ID', blank=True, null=True)  # Field name made lowercase.
    verifier_code = models.TextField(db_column='VERIFIER_CODE', blank=True, null=True)  # Field name made lowercase.
    verifier_lgd = models.TextField(db_column='VERIFIER_LGD', blank=True, null=True)  # Field name made lowercase.
    verifier_name = models.TextField(db_column='VERIFIER_NAME', blank=True, null=True)  # Field name made lowercase.
    total_marks = models.FloatField(blank=True, null=True)
    ranking = models.FloatField(blank=True, null=True)
    accounts = models.TextField(db_column='ACCOUNTS', blank=True, null=True)  # Field name made lowercase.
    division = models.TextField(db_column='DIVISION', blank=True, null=True)  # Field name made lowercase.
    tehsil_name = models.TextField(db_column='TEHSIL_NAME', blank=True, null=True)  # Field name made lowercase.
    office_name = models.TextField(db_column='OFFICE_NAME', blank=True, null=True)  # Field name made lowercase.
    role_type = models.TextField(db_column='ROLE_TYPE', blank=True, null=True)  # Field name made lowercase.
    applicant_name = models.TextField(blank=True, null=True)
    due_date = models.DateTimeField(db_column='DUE_DATE', blank=True, null=True)  # Field name made lowercase.
    within_limit = models.TextField(db_column='WITHIN_LIMIT', blank=True, null=True)  # Field name made lowercase.
    beyond_limit = models.TextField(db_column='BEYOND_LIMIT', blank=True, null=True)  # Field name made lowercase.
    due_date_in_2_days = models.TextField(blank=True, null=True)
    admin_designation = models.CharField(max_length=200, blank=True, null=True)
    application_district = models.CharField(db_column='APPLICATION_DISTRICT', max_length=255, blank=True, null=True)  # Field name made lowercase.
    lgd_code = models.BigIntegerField(db_column='LGD_CODE', blank=True, null=True)  # Field name made lowercase.
    census = models.CharField(db_column='CENSUS', max_length=30, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'user_services_chtgh_final'
  