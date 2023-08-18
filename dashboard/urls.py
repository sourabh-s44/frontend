"""
URL configuration for dashboard project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from dashboard import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path('',views.home),
    path('admin/', admin.site.urls),
    path('roles/', views.role_list),
    path('roles/<int:id>', views.role_details),
    path('paymentModes/',views.paymentMode_list),
    path('paymentModes/<int:id>',views.paymentMode_details),
    path('statusTypes/',views.statusType_list),
    path('statusTypes/<int:id>',views.statusType_details),
    path('statuses/',views.status_list),
    path('statuses/<int:id>',views.status_details),
    path('users/',views.user_list),
    path('users/<int:id>',views.user_details),
    path('materialTypes/',views.materialType_list),
    path('materialTypes/<int:id>',views.materialType_details),
    path('products/',views.product_list),
    path('products/<int:id>',views.product_details),
    path('customerOrders/',views.customerOrder_list),
    path('customerOrders/<int:id>',views.customerOrder_details),
    path('sensors/',views.sensor_list),
    path('sensors/<int:id>',views.sensor_details),
    path('vehicles/',views.vehicle_list),
    path('vehicles/<int:id>',views.vehicle_details),
    path('orderDetails/',views.orderDetail_list),
    path('orderDetails/<int:id>',views.orderDetail_details),
    path('orderPayments/',views.orderPayment_list),
    path('orderPayments/<int:id>',views.orderPayment_details),
    path('warehouses/',views.warehouse_list),
    path('warehouses/<int:id>',views.warehouse_details),
    path('customerInfos/',views.customerInfo_list),
    path('customerInfos/<int:id>',views.customerInfo_details),
    path('sensorDatas/',views.sensorData_list),
    path('sensorDatas/<int:id>',views.sensorData_details)
]

urlpatterns = format_suffix_patterns(urlpatterns)