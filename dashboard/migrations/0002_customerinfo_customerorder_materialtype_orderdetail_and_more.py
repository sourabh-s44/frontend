# Generated by Django 4.2.3 on 2023-07-31 10:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CustomerInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company_name', models.CharField(max_length=100)),
                ('owner_fullname', models.CharField(max_length=100)),
                ('owner_first_name', models.CharField(max_length=100)),
                ('owner_middle_name', models.CharField(max_length=100)),
                ('owner_last_name', models.CharField(max_length=100)),
                ('tan_details', models.CharField(max_length=100)),
                ('gst_details', models.CharField(max_length=100)),
                ('business_type', models.CharField(max_length=100)),
                ('head_office', models.CharField(max_length=100)),
                ('ceo_name', models.CharField(max_length=100)),
                ('poc_name', models.CharField(max_length=100)),
                ('phone_number', models.IntegerField()),
                ('email', models.EmailField(max_length=254)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='CustomerOrder',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ordered_by', models.IntegerField()),
                ('product_name', models.CharField(max_length=100)),
                ('material_type', models.CharField(max_length=100)),
                ('quantity', models.FloatField()),
                ('starting_location', models.CharField(max_length=100)),
                ('destination_location', models.CharField(max_length=100)),
                ('warehouse_requirement', models.BooleanField()),
                ('status', models.CharField(max_length=100)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('updated_by', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='MaterialType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('material_type', models.CharField(max_length=100, unique=True)),
                ('description', models.CharField(max_length=255)),
                ('desired_temp_min', models.FloatField()),
                ('desired_temp_max', models.FloatField()),
                ('desired_humidity_min', models.IntegerField()),
                ('desired_humidity_max', models.IntegerField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='OrderDetail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_number', models.IntegerField()),
                ('ordered_by', models.IntegerField()),
                ('material_type', models.CharField(max_length=100)),
                ('quantity', models.FloatField()),
                ('status', models.CharField(max_length=100)),
                ('starting_location', models.CharField(max_length=100)),
                ('destination_location', models.CharField(max_length=100)),
                ('warehouse_requirement', models.BooleanField()),
                ('material_pickup_quanitity_customer_location', models.FloatField()),
                ('material_pickup_vehicle_customer_location_datetime', models.DateTimeField()),
                ('material_quantity_received_warehouse', models.FloatField()),
                ('material_unload_warehouse_datetime', models.DateTimeField()),
                ('material_loading_vehicle_warehouse_quantity', models.FloatField()),
                ('material_loading_vehicle_warehouse_datetime', models.DateTimeField()),
                ('material_unloading_destination_quantity', models.FloatField()),
                ('material_unloading_destination_datetime', models.DateTimeField()),
                ('invoice_status', models.CharField(max_length=100)),
                ('payment_status', models.CharField(max_length=100)),
                ('current_temp', models.FloatField()),
                ('current_humidity', models.IntegerField()),
                ('current_location', models.CharField(max_length=100)),
                ('sensor_mapping_id', models.IntegerField()),
                ('assigned_to', models.IntegerField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('updated_by', models.IntegerField()),
                ('customerOrder', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dashboard.customerorder')),
                ('materialType', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dashboard.materialtype')),
            ],
        ),
        migrations.CreateModel(
            name='PaymentMode',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True)),
                ('description', models.CharField(max_length=255)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Sensor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(max_length=100)),
                ('status', models.CharField(max_length=100)),
                ('token', models.CharField(max_length=100)),
                ('current_order_tag', models.IntegerField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('customerOrder', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dashboard.customerorder')),
            ],
        ),
        migrations.CreateModel(
            name='StatusType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(max_length=100, unique=True)),
                ('description', models.CharField(max_length=255)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=50, unique=True)),
                ('password', models.CharField(max_length=128)),
                ('full_name', models.CharField(max_length=100)),
                ('first_name', models.CharField(max_length=50)),
                ('middle_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=100, unique=True)),
                ('date_of_birth', models.DateField()),
                ('aadhar', models.BigIntegerField(unique=True)),
                ('pan', models.CharField(max_length=10, unique=True)),
                ('license_number', models.CharField(max_length=20, unique=True)),
                ('license_validity', models.CharField(max_length=10)),
                ('background_verified', models.BooleanField(default=False)),
                ('phone_number', models.BigIntegerField()),
                ('role', models.CharField(max_length=50)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('updated_by', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Warehouse',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('location', models.CharField(max_length=100)),
                ('owner', models.IntegerField()),
                ('capacity', models.IntegerField()),
                ('precooling_capacity', models.IntegerField()),
                ('temp_min', models.FloatField()),
                ('temp_max', models.FloatField()),
                ('associated_sensors', models.IntegerField()),
                ('contract_validity', models.DateTimeField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Vehicle',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('manufacturing_company', models.CharField(max_length=100)),
                ('owner_id', models.IntegerField()),
                ('owner_backgroundcheck', models.BooleanField()),
                ('vehicle_model', models.CharField(max_length=100)),
                ('vehicle_make_year', models.CharField(max_length=100)),
                ('vehicle_registration_year', models.CharField(max_length=100)),
                ('vehicle_insurence_number', models.CharField(max_length=100, unique=True)),
                ('vehicle_insurence_validity', models.CharField(max_length=100)),
                ('vehicle_rc', models.CharField(max_length=100, unique=True)),
                ('driver_id', models.IntegerField()),
                ('temperature_sensor_id', models.IntegerField()),
                ('humidity_sensor_id', models.IntegerField()),
                ('dashboard_sensor_id', models.IntegerField()),
                ('gps_locator_id', models.IntegerField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('updated_by', models.IntegerField()),
                ('sensor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dashboard.sensor')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dashboard.user')),
            ],
        ),
        migrations.CreateModel(
            name='Status',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(max_length=100)),
                ('status_string', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=255)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('statusType', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dashboard.statustype', unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='SensorData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.FloatField(max_length=5)),
                ('datetime', models.DateTimeField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('sensor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dashboard.sensor')),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=255)),
                ('material_type', models.CharField(max_length=100)),
                ('logistics', models.CharField(max_length=100)),
                ('warehouse_logistics', models.CharField(max_length=100)),
                ('warehouse_logistics_warehouse', models.CharField(max_length=100)),
                ('logistics_warehouse', models.CharField(max_length=100)),
                ('warehouse_requirement_source', models.CharField(max_length=100)),
                ('warehouse_requirment_destination', models.CharField(max_length=100)),
                ('logistics_source_destination', models.CharField(max_length=100)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('updated_by', models.IntegerField()),
                ('materialType', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dashboard.materialtype')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dashboard.user')),
            ],
        ),
        migrations.CreateModel(
            name='OrderPayment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_number', models.IntegerField()),
                ('amount', models.FloatField()),
                ('payment_method', models.CharField(max_length=100)),
                ('payment_received_datetime', models.DateTimeField()),
                ('payment_status', models.CharField(max_length=100)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('updated_by', models.IntegerField()),
                ('orderDetail', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dashboard.orderdetail')),
                ('paymentMethod', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dashboard.paymentmode')),
                ('status', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dashboard.status')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dashboard.user')),
            ],
        ),
        migrations.AddField(
            model_name='orderdetail',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dashboard.product'),
        ),
        migrations.AddField(
            model_name='orderdetail',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dashboard.user'),
        ),
        migrations.AddField(
            model_name='orderdetail',
            name='vehicle',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dashboard.vehicle'),
        ),
        migrations.AddField(
            model_name='customerorder',
            name='materialType',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dashboard.materialtype'),
        ),
        migrations.AddField(
            model_name='customerorder',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dashboard.product'),
        ),
        migrations.AddField(
            model_name='customerorder',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dashboard.user'),
        ),
    ]
