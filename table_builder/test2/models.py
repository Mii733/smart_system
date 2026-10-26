# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    group = models.ForeignKey(AuthGroup, models.CASCADE)
    permission = models.ForeignKey('AuthPermission', models.CASCADE)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.CASCADE)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.BooleanField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.BooleanField()
    is_active = models.BooleanField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.CASCADE)
    group = models.ForeignKey(AuthGroup, models.CASCADE)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.CASCADE)
    permission = models.ForeignKey(AuthPermission, models.CASCADE)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.SmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.CASCADE, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.CASCADE)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    id = models.BigAutoField(primary_key=True)
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class DynamicModelsAaaa(models.Model):
    id = models.BigAutoField(primary_key=True)

    class Meta:
        managed = False
        db_table = 'dynamic_models_aaaa'


class DynamicModelsDddd(models.Model):
    id = models.BigAutoField(primary_key=True)

    class Meta:
        managed = False
        db_table = 'dynamic_models_dddd'


class DynamicModelsFieldschema(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=63)
    class_name = models.TextField()
    kwargs = models.JSONField()
    model_schema = models.ForeignKey('DynamicModelsModelschema', models.CASCADE)

    class Meta:
        managed = False
        db_table = 'dynamic_models_fieldschema'
        unique_together = (('name', 'model_schema'),)


class DynamicModelsHhhh(models.Model):
    id = models.BigAutoField(primary_key=True)

    class Meta:
        managed = False
        db_table = 'dynamic_models_hhhh'


class DynamicModelsKhkhkhkh(models.Model):
    id = models.BigAutoField(primary_key=True)

    class Meta:
        managed = False
        db_table = 'dynamic_models_khkhkhkh'


class DynamicModelsKkk(models.Model):
    id = models.BigAutoField(primary_key=True)

    class Meta:
        managed = False
        db_table = 'dynamic_models_kkk'


class DynamicModelsMmmm(models.Model):
    id = models.BigAutoField(primary_key=True)

    class Meta:
        managed = False
        db_table = 'dynamic_models_mmmm'


class DynamicModelsModelschema(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(unique=True, max_length=250)
    db_name = models.CharField(max_length=32)
    managed = models.BooleanField()
    db_table_name = models.CharField(max_length=250, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'dynamic_models_modelschema'


class DynamicModelsNnnn(models.Model):
    id = models.BigAutoField(primary_key=True)

    class Meta:
        managed = False
        db_table = 'dynamic_models_nnnn'


class DynamicModelsTtttt(models.Model):
    id = models.BigAutoField(primary_key=True)

    class Meta:
        managed = False
        db_table = 'dynamic_models_ttttt'


class DynamicModelsWwww(models.Model):
    id = models.BigAutoField(primary_key=True)

    class Meta:
        managed = False
        db_table = 'dynamic_models_wwww'


class DynamicModelsZzzz(models.Model):
    id = models.BigAutoField(primary_key=True)

    class Meta:
        managed = False
        db_table = 'dynamic_models_zzzz'


class DynmicTableCustmreportheader(models.Model):
    id = models.BigAutoField(primary_key=True)
    imge = models.CharField(max_length=100, blank=True, null=True)
    field1_right = models.CharField(max_length=200, blank=True, null=True)
    field2_right = models.CharField(max_length=200, blank=True, null=True)
    field3_right = models.CharField(max_length=200, blank=True, null=True)
    field1_left = models.CharField(max_length=200, blank=True, null=True)
    field2_left = models.CharField(max_length=200, blank=True, null=True)
    field3_left = models.CharField(max_length=200, blank=True, null=True)
    current_user = models.ForeignKey(AuthUser, models.CASCADE, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'dynmic_table_custmreportheader'


class DynmicTableCustomfield(models.Model):
    id = models.BigAutoField(primary_key=True)
    table = models.CharField(max_length=100)
    field_name = models.CharField(max_length=100)
    field_type = models.CharField(max_length=100, blank=True, null=True)
    verbose_name = models.CharField(max_length=100, blank=True, null=True)
    max_length = models.IntegerField(blank=True, null=True)
    null_or_not = models.BooleanField(blank=True, null=True)
    blank_or_not = models.BooleanField(blank=True, null=True)
    unique_or_not = models.BooleanField(blank=True, null=True)
    on_delete = models.CharField(max_length=100, blank=True, null=True)
    related_name = models.CharField(max_length=100, blank=True, null=True)
    related_table = models.CharField(max_length=100, blank=True, null=True)
    is_related = models.BooleanField()

    class Meta:
        managed = False
        db_table = 'dynmic_table_customfield'


class DynmicTableCustomuser(models.Model):
    id = models.BigAutoField(primary_key=True)
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.BooleanField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    is_staff = models.BooleanField()
    is_active = models.BooleanField()
    date_joined = models.DateTimeField()
    email = models.CharField(unique=True, max_length=254)
    date_of_birth = models.DateField(blank=True, null=True)
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    country = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'dynmic_table_customuser'


class DynmicTableCustomuserGroups(models.Model):
    id = models.BigAutoField(primary_key=True)
    customuser = models.ForeignKey(DynmicTableCustomuser, models.CASCADE)
    group = models.ForeignKey(AuthGroup, models.CASCADE)

    class Meta:
        managed = False
        db_table = 'dynmic_table_customuser_groups'
        unique_together = (('customuser', 'group'),)


class DynmicTableCustomuserUserPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    customuser = models.ForeignKey(DynmicTableCustomuser, models.CASCADE)
    permission = models.ForeignKey(AuthPermission, models.CASCADE)

    class Meta:
        managed = False
        db_table = 'dynmic_table_customuser_user_permissions'
        unique_together = (('customuser', 'permission'),)


class DynmicTableFieldcondition(models.Model):
    id = models.BigAutoField(primary_key=True)
    model_name = models.CharField(max_length=255, blank=True, null=True)
    field_name = models.CharField(max_length=255, blank=True, null=True)
    dependent_field = models.CharField(max_length=255, blank=True, null=True)
    condition = models.CharField(max_length=50, blank=True, null=True)
    condition_value = models.CharField(max_length=255, blank=True, null=True)
    action = models.CharField(max_length=50, blank=True, null=True)
    restricted_values = models.JSONField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'dynmic_table_fieldcondition'


class DynmicTableModelnames(models.Model):
    id = models.BigAutoField(primary_key=True)
    modelname = models.CharField(unique=True, max_length=100)
    modelnamear = models.CharField(db_column='modelnameAr', unique=True, max_length=100)  # Field name made lowercase.
    model_type = models.CharField(max_length=100, blank=True, null=True)
    sys_name = models.ForeignKey('DynmicTableTblsystem', models.CASCADE, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'dynmic_table_modelnames'


class DynmicTableTblsystem(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(unique=True, max_length=100)

    class Meta:
        managed = False
        db_table = 'dynmic_table_tblsystem'


class DynmicTableUseraction(models.Model):
    id = models.BigAutoField(primary_key=True)
    action = models.CharField(max_length=255, blank=True, null=True)
    model_name = models.CharField(max_length=255, blank=True, null=True)
    details = models.TextField(blank=True, null=True)
    timestamp = models.DateTimeField(blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.CASCADE, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'dynmic_table_useraction'