# Generated by Django 4.0.4 on 2022-05-14 17:03

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ActiveStorageAttachments',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
                ('record_type', models.CharField(max_length=255)),
                ('record_id', models.BigIntegerField()),
                ('created_at', models.DateTimeField()),
            ],
            options={
                'db_table': 'active_storage_attachments',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='ActiveStorageBlobs',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('key', models.CharField(max_length=255, unique=True)),
                ('filename', models.CharField(max_length=255)),
                ('content_type', models.CharField(blank=True, max_length=255, null=True)),
                ('metadata', models.TextField(blank=True, null=True)),
                ('byte_size', models.BigIntegerField()),
                ('checksum', models.CharField(max_length=255)),
                ('created_at', models.DateTimeField()),
            ],
            options={
                'db_table': 'active_storage_blobs',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Addresses',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('type_of_address', models.CharField(blank=True, max_length=255, null=True)),
                ('status', models.CharField(blank=True, max_length=255, null=True)),
                ('entity', models.CharField(blank=True, max_length=255, null=True)),
                ('number_and_street', models.CharField(blank=True, max_length=255, null=True)),
                ('suite_or_apartment', models.CharField(blank=True, max_length=255, null=True)),
                ('city', models.CharField(blank=True, max_length=255, null=True)),
                ('postal_code', models.CharField(blank=True, max_length=255, null=True)),
                ('country', models.CharField(blank=True, max_length=255, null=True)),
                ('notes', models.CharField(blank=True, max_length=255, null=True)),
                ('created_at', models.DateTimeField()),
                ('updated_at', models.DateTimeField()),
                ('state', models.CharField(blank=True, max_length=255, null=True)),
            ],
            options={
                'db_table': 'addresses',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='ArInternalMetadata',
            fields=[
                ('key', models.CharField(max_length=255, primary_key=True, serialize=False)),
                ('value', models.CharField(blank=True, max_length=255, null=True)),
                ('created_at', models.DateTimeField()),
                ('updated_at', models.DateTimeField()),
            ],
            options={
                'db_table': 'ar_internal_metadata',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthGroup',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, unique=True)),
            ],
            options={
                'db_table': 'auth_group',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthGroupPermissions',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
            ],
            options={
                'db_table': 'auth_group_permissions',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthPermission',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('codename', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'auth_permission',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128)),
                ('last_login', models.DateTimeField(blank=True, null=True)),
                ('is_superuser', models.IntegerField()),
                ('username', models.CharField(max_length=150, unique=True)),
                ('first_name', models.CharField(max_length=150)),
                ('last_name', models.CharField(max_length=150)),
                ('email', models.CharField(max_length=254)),
                ('is_staff', models.IntegerField()),
                ('is_active', models.IntegerField()),
                ('date_joined', models.DateTimeField()),
            ],
            options={
                'db_table': 'auth_user',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthUserGroups',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
            ],
            options={
                'db_table': 'auth_user_groups',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthUserUserPermissions',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
            ],
            options={
                'db_table': 'auth_user_user_permissions',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Batteries',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('status', models.CharField(blank=True, max_length=255, null=True)),
                ('date_of_commissioning', models.DateField(blank=True, null=True)),
                ('date_of_last_inspection', models.DateField(blank=True, null=True)),
                ('certificate_of_operations', models.TextField(blank=True, null=True)),
                ('information', models.CharField(blank=True, max_length=255, null=True)),
                ('notes', models.CharField(blank=True, max_length=255, null=True)),
                ('created_at', models.DateTimeField()),
                ('updated_at', models.DateTimeField()),
                ('typing', models.CharField(blank=True, max_length=255, null=True)),
            ],
            options={
                'db_table': 'batteries',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='BuildingDetails',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('information_key', models.CharField(blank=True, max_length=255, null=True)),
                ('value', models.CharField(blank=True, max_length=255, null=True)),
                ('created_at', models.DateTimeField()),
                ('updated_at', models.DateTimeField()),
            ],
            options={
                'db_table': 'building_details',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Buildings',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('full_name_of_the_building_administrator', models.CharField(blank=True, max_length=255, null=True)),
                ('email_of_the_administrator_of_the_building', models.CharField(blank=True, max_length=255, null=True)),
                ('phone_number_of_the_building_administrator', models.CharField(blank=True, max_length=255, null=True)),
                ('full_name_of_the_technical_contact_for_the_building', models.CharField(blank=True, max_length=255, null=True)),
                ('technical_contact_email_for_the_building', models.CharField(blank=True, max_length=255, null=True)),
                ('technical_contact_phone_for_the_building', models.CharField(blank=True, max_length=255, null=True)),
                ('created_at', models.DateTimeField()),
                ('updated_at', models.DateTimeField()),
            ],
            options={
                'db_table': 'buildings',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Columns',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('number_of_floors_served', models.CharField(blank=True, max_length=255, null=True)),
                ('status', models.CharField(blank=True, max_length=255, null=True)),
                ('information', models.CharField(blank=True, max_length=255, null=True)),
                ('notes', models.CharField(blank=True, max_length=255, null=True)),
                ('created_at', models.DateTimeField()),
                ('updated_at', models.DateTimeField()),
                ('typing', models.CharField(blank=True, max_length=255, null=True)),
            ],
            options={
                'db_table': 'columns',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('first_name', models.CharField(blank=True, max_length=255, null=True)),
                ('last_name', models.CharField(blank=True, max_length=255, null=True)),
            ],
            options={
                'db_table': 'customer',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Customers',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('company_name', models.CharField(blank=True, max_length=255, null=True)),
                ('company_headquarters_address', models.CharField(blank=True, max_length=255, null=True)),
                ('full_name_of_the_company_contact', models.CharField(blank=True, max_length=255, null=True)),
                ('company_contact_phone', models.CharField(blank=True, max_length=255, null=True)),
                ('email_of_the_company_contact', models.CharField(blank=True, max_length=255, null=True)),
                ('company_description', models.CharField(blank=True, max_length=255, null=True)),
                ('full_name_of_service_technical_authority', models.CharField(blank=True, max_length=255, null=True)),
                ('technical_authority_phone_for_service', models.CharField(blank=True, max_length=255, null=True)),
                ('technical_manager_email_for_service', models.CharField(blank=True, max_length=255, null=True)),
                ('created_at', models.DateTimeField()),
                ('updated_at', models.DateTimeField()),
                ('customer_creation_date', models.DateField(blank=True, null=True)),
            ],
            options={
                'db_table': 'customers',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DjangoAdminLog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('action_time', models.DateTimeField()),
                ('object_id', models.TextField(blank=True, null=True)),
                ('object_repr', models.CharField(max_length=200)),
                ('action_flag', models.PositiveSmallIntegerField()),
                ('change_message', models.TextField()),
            ],
            options={
                'db_table': 'django_admin_log',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DjangoContentType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('app_label', models.CharField(max_length=100)),
                ('model', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'django_content_type',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DjangoMigrations',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('app', models.CharField(max_length=255)),
                ('name', models.CharField(max_length=255)),
                ('applied', models.DateTimeField()),
            ],
            options={
                'db_table': 'django_migrations',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DjangoSession',
            fields=[
                ('session_key', models.CharField(max_length=40, primary_key=True, serialize=False)),
                ('session_data', models.TextField()),
                ('expire_date', models.DateTimeField()),
            ],
            options={
                'db_table': 'django_session',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Elevators',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('serial_number', models.CharField(blank=True, max_length=255, null=True)),
                ('model', models.CharField(blank=True, max_length=255, null=True)),
                ('status', models.CharField(blank=True, max_length=255, null=True)),
                ('date_of_commissioning', models.DateField(blank=True, null=True)),
                ('date_of_last_inspection', models.DateField(blank=True, null=True)),
                ('certificate_of_inspection', models.TextField(blank=True, null=True)),
                ('information', models.CharField(blank=True, max_length=255, null=True)),
                ('notes', models.CharField(blank=True, max_length=255, null=True)),
                ('created_at', models.DateTimeField()),
                ('updated_at', models.DateTimeField()),
                ('typing', models.CharField(blank=True, max_length=255, null=True)),
            ],
            options={
                'db_table': 'elevators',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Employees',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(blank=True, max_length=255, null=True)),
                ('created_at', models.DateTimeField()),
                ('updated_at', models.DateTimeField()),
                ('image_encoding', models.CharField(blank=True, max_length=2000, null=True)),
            ],
            options={
                'db_table': 'employees',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='HibernateSequence',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('next_val', models.BigIntegerField(blank=True, null=True)),
            ],
            options={
                'db_table': 'hibernate_sequence',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Interventions',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('customer_id', models.CharField(blank=True, max_length=255, null=True)),
                ('building_id', models.CharField(blank=True, max_length=255, null=True)),
                ('battery_id', models.CharField(blank=True, max_length=255, null=True)),
                ('column_id', models.CharField(blank=True, max_length=255, null=True)),
                ('elevator_id', models.CharField(blank=True, max_length=255, null=True)),
                ('employee_id', models.CharField(blank=True, max_length=255, null=True)),
                ('start_date', models.DateTimeField(blank=True, null=True)),
                ('end_date', models.DateTimeField(blank=True, null=True)),
                ('result', models.CharField(blank=True, max_length=255, null=True)),
                ('report', models.TextField(blank=True, null=True)),
                ('status', models.CharField(blank=True, max_length=255, null=True)),
                ('author', models.CharField(blank=True, max_length=255, null=True)),
            ],
            options={
                'db_table': 'interventions',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Leads',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('full_name', models.CharField(blank=True, max_length=255, null=True)),
                ('company_name', models.CharField(blank=True, max_length=255, null=True)),
                ('email', models.CharField(blank=True, max_length=255, null=True)),
                ('phone', models.CharField(blank=True, max_length=255, null=True)),
                ('project_name', models.CharField(blank=True, max_length=255, null=True)),
                ('project_description', models.CharField(blank=True, max_length=255, null=True)),
                ('department_in_charge_of_elevators', models.CharField(blank=True, max_length=255, null=True)),
                ('message', models.CharField(blank=True, max_length=255, null=True)),
                ('attached_file_stored_as_binary', models.TextField(blank=True, null=True)),
                ('created_at', models.DateTimeField()),
                ('updated_at', models.DateTimeField()),
                ('date_of_contact_request', models.DateField(blank=True, null=True)),
            ],
            options={
                'db_table': 'leads',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='MyapiHero',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=60)),
                ('alias', models.CharField(max_length=60)),
            ],
            options={
                'db_table': 'myapi_hero',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='MyapiVillain',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=60)),
                ('alias', models.CharField(max_length=60)),
            ],
            options={
                'db_table': 'myapi_villain',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Quotes',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('building_type', models.CharField(blank=True, max_length=255, null=True)),
                ('num_apts', models.IntegerField(blank=True, null=True)),
                ('num_floors', models.IntegerField(blank=True, null=True)),
                ('num_base', models.IntegerField(blank=True, null=True)),
                ('num_comp', models.IntegerField(blank=True, null=True)),
                ('num_park', models.IntegerField(blank=True, null=True)),
                ('num_elev', models.IntegerField(blank=True, null=True)),
                ('num_corps', models.IntegerField(blank=True, null=True)),
                ('max_occ', models.IntegerField(blank=True, null=True)),
                ('b_hours', models.IntegerField(blank=True, null=True)),
                ('product_line', models.CharField(blank=True, max_length=255, null=True)),
                ('unit_price', models.CharField(blank=True, max_length=255, null=True)),
                ('elev_cost', models.CharField(blank=True, max_length=255, null=True)),
                ('install_fee', models.CharField(blank=True, max_length=255, null=True)),
                ('total_cost', models.CharField(blank=True, max_length=255, null=True)),
                ('created_at', models.DateTimeField()),
                ('updated_at', models.DateTimeField()),
                ('company_name', models.CharField(blank=True, max_length=255, null=True)),
                ('email', models.CharField(blank=True, max_length=255, null=True)),
                ('estimated_elev', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'db_table': 'quotes',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='SchemaMigrations',
            fields=[
                ('version', models.CharField(max_length=255, primary_key=True, serialize=False)),
            ],
            options={
                'db_table': 'schema_migrations',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Users',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('email', models.CharField(max_length=255, unique=True)),
                ('encrypted_password', models.CharField(max_length=255)),
                ('reset_password_token', models.CharField(blank=True, max_length=255, null=True, unique=True)),
                ('reset_password_sent_at', models.DateTimeField(blank=True, null=True)),
                ('remember_created_at', models.DateTimeField(blank=True, null=True)),
                ('created_at', models.DateTimeField()),
                ('updated_at', models.DateTimeField()),
                ('first_name', models.CharField(blank=True, max_length=255, null=True)),
                ('last_name', models.CharField(blank=True, max_length=255, null=True)),
            ],
            options={
                'db_table': 'users',
                'managed': False,
            },
        ),
    ]
