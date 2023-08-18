from django.contrib import admin
from .models import Role, PaymentMode, StatusType, Status, User, MaterialType, Product, CustomerOrder, Sensor, Vehicle, OrderDetail, OrderPayment, Warehouse, CustomerInfo, SensorData

admin.site.register(Role)
admin.site.register(PaymentMode)
admin.site.register(StatusType)
admin.site.register(Status)
admin.site.register(User)
admin.site.register(MaterialType)
admin.site.register(Product)
admin.site.register(CustomerOrder)
admin.site.register(Sensor)
admin.site.register(Vehicle)
admin.site.register(OrderDetail)
admin.site.register(OrderPayment)
admin.site.register(Warehouse)
admin.site.register(CustomerInfo)
admin.site.register(SensorData)