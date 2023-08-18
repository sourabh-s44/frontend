from django.db import models

# role table to store all the roles that users will have in the system
class Role(models.Model):
    role = models.CharField(max_length=100,unique=True)
    description = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.role

    # PaymentMode table to store all the mode of payments supported by the system
class PaymentMode(models.Model):
    name = models.CharField(max_length=100,unique=True)
    description = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


# StatusType table to store the different status types for different workflows
class StatusType(models.Model):
    type = models.CharField(max_length=100,unique=True)
    description = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.type


# Status table to store all the statuses defined for various workflows
class Status(models.Model):
    statusType = models.ForeignKey(StatusType, on_delete=models.CASCADE, unique=True)
    type = models.CharField(max_length=100)
    status_string = models.CharField(max_length=100)
    description = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.type


# user table to store the information about all the users that will use the system
class User(models.Model):
    role = models.ForeignKey(Role, on_delete=models.CASCADE)
    username = models.CharField(max_length=50, unique=True)
    password = models.CharField(max_length=128)
    full_name = models.CharField(max_length=100)
    first_name = models.CharField(max_length=50)
    middle_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(max_length=100, unique=True)
    date_of_birth = models.DateField()
    aadhar = models.BigIntegerField(unique=True)
    pan = models.CharField(max_length=10,unique=True)
    license_number = models.CharField(max_length=20,unique=True)
    license_validity = models.CharField(max_length=10)
    background_verified = models.BooleanField(default=False)
    phone_number = models.BigIntegerField()
    role = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    updated_by = models.IntegerField()

    def __str__(self):
        return self.username


# MaterailType table to store all the information about the materials that customer can order
class MaterialType(models.Model):
    material_type = models.CharField(max_length=100,unique=True)
    description = models.CharField(max_length=255)
    desired_temp_min = models.FloatField()
    desired_temp_max = models.FloatField()
    desired_humidity_min = models.IntegerField()
    desired_humidity_max = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.material_type

# Products table to store all the information related to products that custoimer can order
class Product(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    materialType = models.ForeignKey(MaterialType, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=255)
    material_type = models.CharField(max_length=100)
    logistics = models.CharField(max_length=100)
    warehouse_logistics = models.CharField(max_length=100)
    warehouse_logistics_warehouse = models.CharField(max_length=100)
    logistics_warehouse = models.CharField(max_length=100)
    warehouse_requirement_source = models.CharField(max_length=100)
    warehouse_requirment_destination = models.CharField(max_length=100)
    logistics_source_destination = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    updated_by = models.IntegerField()

    def __str__(self):
        return self.name

    # customerOrder table to store all the orders placed by the customer 
class CustomerOrder(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    status = models.ForeignKey(Status, on_delete=models.CASCADE)
    materialType = models.ForeignKey(MaterialType, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    ordered_by = models.IntegerField()
    product_name = models.CharField(max_length=100)
    material_type = models.CharField(max_length=100)
    quantity = models.FloatField()
    starting_location = models.CharField(max_length=100)
    destination_location = models.CharField(max_length=100)
    warehouse_requirement = models.BooleanField()
    status = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    updated_by = models.IntegerField()

    def __str__(self):
        return self.ordered_by

# Sensor table to store all the sensor information
class Sensor(models.Model):
    status = models.ForeignKey(Status, on_delete=models.CASCADE)
    customerOrder = models.ForeignKey(CustomerOrder, on_delete=models.CASCADE)
    name = models.CharField(max_length=100, default='TestSensor')
    type = models.CharField(max_length=100)
    status = models.CharField(max_length=100)
    token = models.CharField(max_length=100)
    current_order_tag = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

# Vehicle table to store all the information related to Vehicles
class Vehicle(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    sensor = models.ForeignKey(Sensor, on_delete=models.CASCADE)
    manufacturing_company = models.CharField(max_length=100)
    owner_id = models.IntegerField()
    owner_backgroundcheck = models.BooleanField()
    vehicle_model = models.CharField(max_length=100)
    vehicle_make_year = models.CharField(max_length=100)
    vehicle_registration_year = models.CharField(max_length=100)
    vehicle_insurence_number = models.CharField(max_length=100,unique=True)
    vehicle_insurence_validity = models.CharField(max_length=100)
    vehicle_rc = models.CharField(max_length=100,unique=True)
    driver_id = models.IntegerField()
    temperature_sensor_id = models.IntegerField()
    humidity_sensor_id = models.IntegerField()
    dashboard_sensor_id = models.IntegerField()
    gps_locator_id = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    updated_by = models.IntegerField()

    def __str__(self):
        return self.vehicle_model

# orderDetail table to store all the details about the order placed by the customer
class OrderDetail(models.Model):
    customerOrder = models.ForeignKey(CustomerOrder, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    status = models.ForeignKey(Status, on_delete=models.CASCADE)
    materialType = models.ForeignKey(MaterialType, on_delete=models.CASCADE)
    vehicle = models.ForeignKey(Vehicle, on_delete=models.CASCADE)
    order_number = models.IntegerField()
    ordered_by = models.IntegerField()
    material_type = models.CharField(max_length=100)
    quantity = models.FloatField()
    status = models.CharField(max_length=100)
    starting_location = models.CharField(max_length=100)
    destination_location = models.CharField(max_length=100)
    warehouse_requirement = models.BooleanField()
    material_pickup_quanitity_customer_location = models.FloatField()
    material_pickup_vehicle_customer_location_datetime = models.DateTimeField()
    material_quantity_received_warehouse = models.FloatField()
    material_unload_warehouse_datetime = models.DateTimeField()
    material_loading_vehicle_warehouse_quantity = models.FloatField()
    material_loading_vehicle_warehouse_datetime = models.DateTimeField()
    material_unloading_destination_quantity = models.FloatField()
    material_unloading_destination_datetime = models.DateTimeField()
    invoice_status = models.CharField(max_length=100)
    payment_status = models.CharField(max_length=100)
    current_temp = models.FloatField()
    current_humidity = models.IntegerField()
    current_location = models.CharField(max_length=100)
    sensor_mapping_id = models.IntegerField()
    assigned_to = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    updated_by = models.IntegerField()

    def __str__(self):
        return self.order_number

# OrderPayment table to store all the information related to the payment of the orders    
class OrderPayment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    status = models.ForeignKey(Status, on_delete=models.CASCADE)
    orderDetail = models.ForeignKey(OrderDetail, on_delete=models.CASCADE)
    paymentMethod = models.ForeignKey(PaymentMode, on_delete=models.CASCADE)
    order_number = models.IntegerField()
    amount = models.FloatField()
    payment_method = models.CharField(max_length=100)
    payment_received_datetime = models.DateTimeField()
    payment_status = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    updated_by = models.IntegerField()

    def __str__(self):
        return self.order_number


# Warehouse table to store all the information about the warehouse
class Warehouse(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    owner = models.IntegerField()
    capacity = models.IntegerField()
    precooling_capacity = models.IntegerField()
    temp_min = models.FloatField()
    temp_max = models.FloatField()
    associated_sensors = models.IntegerField()
    contract_validity = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


# CustomerInfo table to store the customer information
class CustomerInfo(models.Model):
    company_name = models.CharField(max_length=100)
    owner_fullname = models.CharField(max_length=100)
    owner_first_name = models.CharField(max_length=100)
    owner_middle_name = models.CharField(max_length=100)
    owner_last_name = models.CharField(max_length=100)
    tan_details = models.CharField(max_length=100)
    gst_details = models.CharField(max_length=100)
    business_type = models.CharField(max_length=100)
    head_office = models.CharField(max_length=100)
    ceo_name = models.CharField(max_length=100)
    poc_name = models.CharField(max_length=100)
    phone_number = models.IntegerField()
    email = models.EmailField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.company_name

# Temperature table to store the temperature & humidityreading data for various sensors
class SensorData(models.Model):
    sensor = models.ForeignKey(Sensor, on_delete=models.CASCADE)
    value = models.FloatField(max_length=5)
    datetime = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.sensor



