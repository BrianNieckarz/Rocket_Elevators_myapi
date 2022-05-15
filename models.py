# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class ActiveStorageAttachments(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=255)
    record_type = models.CharField(max_length=255)
    record_id = models.BigIntegerField()
    blob = models.ForeignKey('ActiveStorageBlobs', models.DO_NOTHING)
    created_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'active_storage_attachments'
        unique_together = (('record_type', 'record_id', 'name', 'blob'),)


class ActiveStorageBlobs(models.Model):
    id = models.BigAutoField(primary_key=True)
    key = models.CharField(unique=True, max_length=255)
    filename = models.CharField(max_length=255)
    content_type = models.CharField(max_length=255, blank=True, null=True)
    metadata = models.TextField(blank=True, null=True)
    byte_size = models.BigIntegerField()
    checksum = models.CharField(max_length=255)
    created_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'active_storage_blobs'


class Addresses(models.Model):
    id = models.BigAutoField(primary_key=True)
    type_of_address = models.CharField(max_length=255, blank=True, null=True)
    status = models.CharField(max_length=255, blank=True, null=True)
    entity = models.CharField(max_length=255, blank=True, null=True)
    number_and_street = models.CharField(max_length=255, blank=True, null=True)
    suite_or_apartment = models.CharField(max_length=255, blank=True, null=True)
    city = models.CharField(max_length=255, blank=True, null=True)
    postal_code = models.CharField(max_length=255, blank=True, null=True)
    country = models.CharField(max_length=255, blank=True, null=True)
    notes = models.CharField(max_length=255, blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    state = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'addresses'


class ArInternalMetadata(models.Model):
    key = models.CharField(primary_key=True, max_length=255)
    value = models.CharField(max_length=255, blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'ar_internal_metadata'


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class Batteries(models.Model):
    id = models.BigAutoField(primary_key=True)
    building = models.ForeignKey('Buildings', models.DO_NOTHING, blank=True, null=True)
    status = models.CharField(max_length=255, blank=True, null=True)
    employee = models.ForeignKey('Employees', models.DO_NOTHING, blank=True, null=True)
    date_of_commissioning = models.DateField(blank=True, null=True)
    date_of_last_inspection = models.DateField(blank=True, null=True)
    certificate_of_operations = models.TextField(blank=True, null=True)
    information = models.CharField(max_length=255, blank=True, null=True)
    notes = models.CharField(max_length=255, blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    typing = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'batteries'


class BuildingDetails(models.Model):
    id = models.BigAutoField(primary_key=True)
    building = models.ForeignKey('Buildings', models.DO_NOTHING, blank=True, null=True)
    information_key = models.CharField(max_length=255, blank=True, null=True)
    value = models.CharField(max_length=255, blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'building_details'


class Buildings(models.Model):
    id = models.BigAutoField(primary_key=True)
    customer = models.ForeignKey('Customers', models.DO_NOTHING, blank=True, null=True)
    full_name_of_the_building_administrator = models.CharField(max_length=255, blank=True, null=True)
    email_of_the_administrator_of_the_building = models.CharField(max_length=255, blank=True, null=True)
    phone_number_of_the_building_administrator = models.CharField(max_length=255, blank=True, null=True)
    full_name_of_the_technical_contact_for_the_building = models.CharField(max_length=255, blank=True, null=True)
    technical_contact_email_for_the_building = models.CharField(max_length=255, blank=True, null=True)
    technical_contact_phone_for_the_building = models.CharField(max_length=255, blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    address = models.ForeignKey(Addresses, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'buildings'


class Columns(models.Model):
    id = models.BigAutoField(primary_key=True)
    battery = models.ForeignKey(Batteries, models.DO_NOTHING, blank=True, null=True)
    number_of_floors_served = models.CharField(max_length=255, blank=True, null=True)
    status = models.CharField(max_length=255, blank=True, null=True)
    information = models.CharField(max_length=255, blank=True, null=True)
    notes = models.CharField(max_length=255, blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    typing = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'columns'


class Customer(models.Model):
    id = models.IntegerField(primary_key=True)
    first_name = models.CharField(max_length=255, blank=True, null=True)
    last_name = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'customer'


class Customers(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey('Users', models.DO_NOTHING, blank=True, null=True)
    company_name = models.CharField(max_length=255, blank=True, null=True)
    company_headquarters_address = models.CharField(max_length=255, blank=True, null=True)
    full_name_of_the_company_contact = models.CharField(max_length=255, blank=True, null=True)
    company_contact_phone = models.CharField(max_length=255, blank=True, null=True)
    email_of_the_company_contact = models.CharField(max_length=255, blank=True, null=True)
    company_description = models.CharField(max_length=255, blank=True, null=True)
    full_name_of_service_technical_authority = models.CharField(max_length=255, blank=True, null=True)
    technical_authority_phone_for_service = models.CharField(max_length=255, blank=True, null=True)
    technical_manager_email_for_service = models.CharField(max_length=255, blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    customer_creation_date = models.DateField(blank=True, null=True)
    address = models.ForeignKey(Addresses, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'customers'


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

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


class Elevators(models.Model):
    id = models.BigAutoField(primary_key=True)
    column = models.ForeignKey(Columns, models.DO_NOTHING, blank=True, null=True)
    serial_number = models.CharField(max_length=255, blank=True, null=True)
    model = models.CharField(max_length=255, blank=True, null=True)
    status = models.CharField(max_length=255, blank=True, null=True)
    date_of_commissioning = models.DateField(blank=True, null=True)
    date_of_last_inspection = models.DateField(blank=True, null=True)
    certificate_of_inspection = models.TextField(blank=True, null=True)
    information = models.CharField(max_length=255, blank=True, null=True)
    notes = models.CharField(max_length=255, blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    typing = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'elevators'


class Employees(models.Model):
    id = models.BigAutoField(primary_key=True)
    title = models.CharField(max_length=255, blank=True, null=True)
    user = models.ForeignKey('Users', models.DO_NOTHING, blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    image_encoding = models.CharField(max_length=2000, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'employees'


class HibernateSequence(models.Model):
    next_val = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'hibernate_sequence'


class Interventions(models.Model):
    id = models.BigAutoField(primary_key=True)
    customer_id = models.CharField(max_length=255, blank=True, null=True)
    building_id = models.CharField(max_length=255, blank=True, null=True)
    battery_id = models.CharField(max_length=255, blank=True, null=True)
    column_id = models.CharField(max_length=255, blank=True, null=True)
    elevator_id = models.CharField(max_length=255, blank=True, null=True)
    employee_id = models.CharField(max_length=255, blank=True, null=True)
    start_date = models.DateTimeField(blank=True, null=True)
    end_date = models.DateTimeField(blank=True, null=True)
    result = models.CharField(max_length=255, blank=True, null=True)
    report = models.TextField(blank=True, null=True)
    status = models.CharField(max_length=255, blank=True, null=True)
    author = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'interventions'


class Leads(models.Model):
    id = models.BigAutoField(primary_key=True)
    full_name = models.CharField(max_length=255, blank=True, null=True)
    company_name = models.CharField(max_length=255, blank=True, null=True)
    email = models.CharField(max_length=255, blank=True, null=True)
    phone = models.CharField(max_length=255, blank=True, null=True)
    project_name = models.CharField(max_length=255, blank=True, null=True)
    project_description = models.CharField(max_length=255, blank=True, null=True)
    department_in_charge_of_elevators = models.CharField(max_length=255, blank=True, null=True)
    message = models.CharField(max_length=255, blank=True, null=True)
    attached_file_stored_as_binary = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    date_of_contact_request = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'leads'


class MyapiHero(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=60)
    alias = models.CharField(max_length=60)

    class Meta:
        managed = False
        db_table = 'myapi_hero'


class MyapiVillain(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=60)
    alias = models.CharField(max_length=60)

    class Meta:
        managed = False
        db_table = 'myapi_villain'


class Quotes(models.Model):
    id = models.BigAutoField(primary_key=True)
    building_type = models.CharField(max_length=255, blank=True, null=True)
    num_apts = models.IntegerField(blank=True, null=True)
    num_floors = models.IntegerField(blank=True, null=True)
    num_base = models.IntegerField(blank=True, null=True)
    num_comp = models.IntegerField(blank=True, null=True)
    num_park = models.IntegerField(blank=True, null=True)
    num_elev = models.IntegerField(blank=True, null=True)
    num_corps = models.IntegerField(blank=True, null=True)
    max_occ = models.IntegerField(blank=True, null=True)
    b_hours = models.IntegerField(blank=True, null=True)
    product_line = models.CharField(max_length=255, blank=True, null=True)
    unit_price = models.CharField(max_length=255, blank=True, null=True)
    elev_cost = models.CharField(max_length=255, blank=True, null=True)
    install_fee = models.CharField(max_length=255, blank=True, null=True)
    total_cost = models.CharField(max_length=255, blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    company_name = models.CharField(max_length=255, blank=True, null=True)
    email = models.CharField(max_length=255, blank=True, null=True)
    estimated_elev = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'quotes'


class SchemaMigrations(models.Model):
    version = models.CharField(primary_key=True, max_length=255)

    class Meta:
        managed = False
        db_table = 'schema_migrations'


class Users(models.Model):
    id = models.BigAutoField(primary_key=True)
    email = models.CharField(unique=True, max_length=255)
    encrypted_password = models.CharField(max_length=255)
    reset_password_token = models.CharField(unique=True, max_length=255, blank=True, null=True)
    reset_password_sent_at = models.DateTimeField(blank=True, null=True)
    remember_created_at = models.DateTimeField(blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    first_name = models.CharField(max_length=255, blank=True, null=True)
    last_name = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'users'


class Image(models.Model):
    image = models.ImageField(upload_to='myapi/unknown_faces')
