from rest_framework import generics
from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.decorators import api_view
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .models import Role, PaymentMode, StatusType, Status, User, MaterialType, Product, CustomerOrder, Sensor, Vehicle, OrderDetail, OrderPayment, Warehouse, CustomerInfo, SensorData
from .serializers import RoleSerializer, PaymentModeSerializer, StatusTypeSerializer, StatusSerializer, UserSerializer, MaterialTypeSerializer, ProductSerializer, CustomerOrderSerializer, SensorSerializer, VehicleSerializer, OrderDetailSerializer, OrderPaymentSerializer, WarehouseSerializer, CustomerInfoSerializer, SensorDataSerializer

#WEBSITE CODE STARTS HERE
def home(request):
    return HttpResponse('<h1> This is MeCold Logistics Home page!!!')

#API CODE STARTS HERE
#role
@api_view(['GET', 'POST'])
def role_list(request, format=None):
    if request.method == 'GET':
        roles = Role.objects.all()
        serializer = RoleSerializer(roles, many=True)
        return Response({'roles': serializer.data})
    elif request.method == 'POST':
        serializer = RoleSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET','PUT', 'DELETE'])
def role_details(request, id, format=None):
    role = Role.objects.get(pk=id)
    if request.method == 'GET':
        serializer = RoleSerializer(role)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = RoleSerializer(role, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data) 
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)   
    elif request.method == 'DELETE':
        role.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

#paymentMode

@api_view(['GET', 'POST'])
def paymentMode_list(request, format=None):
    if request.method == 'GET':
        paymentModes = PaymentMode.objects.all()
        serializer = PaymentModeSerializer(paymentModes, many=True)
        return Response({'paymentModes': serializer.data})
    elif request.method == 'POST':
        serializer = PaymentModeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET','PUT', 'DELETE'])
def paymentMode_details(request, id, format=None):
    paymentMode = PaymentMode.objects.get(pk=id)
    if request.method == 'GET':
        serializer = PaymentModeSerializer(paymentMode)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = PaymentModeSerializer(paymentMode, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data) 
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)   
    elif request.method == 'DELETE':
        paymentMode.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

#statusType
@api_view(['GET', 'POST'])
def statusType_list(request, format=None):
    if request.method == 'GET':
        statusTypes = StatusType.objects.all()
        serializer = StatusTypeSerializer(statusTypes, many=True)
        return Response({'statusTypes': serializer.data})
    elif request.method == 'POST':
        serializer = StatusTypeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET','PUT', 'DELETE'])
def statusType_details(request, id, format=None):
    statusType = StatusType.objects.get(pk=id)
    if request.method == 'GET':
        serializer = StatusTypeSerializer(statusType)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = StatusTypeSerializer(statusType, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data) 
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)   
    elif request.method == 'DELETE':
        statusType.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

#status
@api_view(['GET', 'POST'])
def status_list(request, format=None):
    if request.method == 'GET':
        statuses = Status.objects.all()
        serializer = StatusSerializer(statuses, many=True)
        return Response({'statuses': serializer.data})
    elif request.method == 'POST':
        serializer = StatusSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET','PUT', 'DELETE'])
def status_details(request, id, format=None):
    status = Status.objects.get(pk=id)
    if request.method == 'GET':
        serializer = StatusSerializer(status)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = StatusSerializer(status, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data) 
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)   
    elif request.method == 'DELETE':
        status.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

#user
@api_view(['GET', 'POST'])
def user_list(request, format=None):
    if request.method == 'GET':
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        return Response({'users': serializer.data})
    elif request.method == 'POST':
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET','PUT', 'DELETE'])
def user_details(request, id, format=None):
    user = User.objects.get(pk=id)
    if request.method == 'GET':
        serializer = UserSerializer(user)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = UserSerializer(user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data) 
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)   
    elif request.method == 'DELETE':
        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

#MaterialType
@api_view(['GET', 'POST'])
def materialType_list(request, format=None):
    if request.method == 'GET':
        materialTypes = MaterialType.objects.all()
        serializer = MaterialTypeSerializer(materialTypes, many=True)
        return Response({'materialTypes': serializer.data})
    elif request.method == 'POST':
        serializer = MaterialTypeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET','PUT', 'DELETE'])
def materialType_details(request, id, format=None):
    materailType = MaterialType.objects.get(pk=id)
    if request.method == 'GET':
        serializer = MaterialTypeSerializer(materailType)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = MaterialTypeSerializer(materailType, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data) 
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)   
    elif request.method == 'DELETE':
        materailType.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

#Product
@api_view(['GET', 'POST'])
def product_list(request, format=None):
    if request.method == 'GET':
        products = Product.objects.all()
        serializer = ProductSerializer(products, many=True)
        return Response({'products': serializer.data})
    elif request.method == 'POST':
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET','PUT', 'DELETE'])
def product_details(request, id, format=None):
    product = Product.objects.get(pk=id)
    if request.method == 'GET':
        serializer = ProductSerializer(product)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = ProductSerializer(product, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data) 
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)   
    elif request.method == 'DELETE':
        product.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

#CustomerOrder
@api_view(['GET', 'POST'])
def customerOrder_list(request, format=None):
    if request.method == 'GET':
        customerOrders = CustomerOrder.objects.all()
        serializer = CustomerOrderSerializer(customerOrders, many=True)
        return Response({'customerOrders': serializer.data})
    elif request.method == 'POST':
        serializer = CustomerOrderSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET','PUT', 'DELETE'])
def customerOrder_details(request, id, format=None):
    customerOrder = CustomerOrder.objects.get(pk=id)
    if request.method == 'GET':
        serializer = CustomerOrderSerializer(customerOrder)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = CustomerOrderSerializer(customerOrder, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data) 
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)   
    elif request.method == 'DELETE':
        customerOrder.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

#Sensor
@api_view(['GET', 'POST'])
def sensor_list(request, format=None):
    if request.method == 'GET':
        sensors = Sensor.objects.all()
        serializer = SensorSerializer(sensors, many=True)
        return Response({'sensors': serializer.data})
    elif request.method == 'POST':
        serializer = SensorSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET','PUT', 'DELETE'])
def sensor_details(request, id, format=None):
    sensor = Sensor.objects.get(pk=id)
    if request.method == 'GET':
        serializer = SensorSerializer(sensor)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = SensorSerializer(sensor, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data) 
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)   
    elif request.method == 'DELETE':
        sensor.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

#Vehicle
@api_view(['GET', 'POST'])
def vehicle_list(request, format=None):
    if request.method == 'GET':
        vehicles = Vehicle.objects.all()
        serializer = VehicleSerializer(vehicles, many=True)
        return Response({'vehicles': serializer.data})
    elif request.method == 'POST':
        serializer = VehicleSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET','PUT', 'DELETE'])
def vehicle_details(request, id, format=None):
    vehicle = Vehicle.objects.get(pk=id)
    if request.method == 'GET':
        serializer = VehicleSerializer(vehicle)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = VehicleSerializer(vehicle, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data) 
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)   
    elif request.method == 'DELETE':
        vehicle.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

#OrderDetail


@api_view(['GET', 'POST'])  # Added POST method
def orderDetail_list(request, format=None):
    if request.method == 'GET':
        orderDetails = OrderDetail.objects.all()
        serializer = OrderDetailSerializer(orderDetails, many=True)
        return Response({'orderDetails': serializer.data})
    elif request.method == 'POST':  # Changed if to elif
        serializer = OrderDetailSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET','PUT', 'DELETE'])
def orderDetail_details(request, id, format=None):
    orderDetail = OrderDetail.objects.get(pk=id)
    if request.method == 'GET':
        serializer = OrderDetailSerializer(orderDetail)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = OrderDetailSerializer(orderDetail, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data) 
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)   
    elif request.method == 'DELETE':
        orderDetail.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

#OrderPayment
@api_view(['GET', 'POST'])
def orderPayment_list(request, format=None):
    if request.method == 'GET':
        orderPayments = OrderPayment.objects.all()
        serializer = OrderPaymentSerializer(orderPayments, many=True)
        return Response({'orderPayments': serializer.data})
    elif request.method == 'POST':
        serializer = OrderPaymentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET','PUT', 'DELETE'])
def orderPayment_details(request, id, format=None):
    orderPayment = OrderPayment.objects.get(pk=id)
    if request.method == 'GET':
        serializer = OrderPaymentSerializer(orderPayment)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = OrderPaymentSerializer(orderPayment, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data) 
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)   
    elif request.method == 'DELETE':
        orderPayment.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

#warehouse
@api_view(['GET', 'POST'])
def warehouse_list(request, format=None):
    if request.method == 'GET':
        warehouses = Warehouse.objects.all()
        serializer = WarehouseSerializer(warehouses, many=True)
        return Response({'warehouses': serializer.data})
    elif request.method == 'POST':
        serializer = WarehouseSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET','PUT', 'DELETE'])
def warehouse_details(request, id, format=None):
    warehouse = Warehouse.objects.get(pk=id)
    if request.method == 'GET':
        serializer = WarehouseSerializer(warehouse)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = WarehouseSerializer(warehouse, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data) 
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)   
    elif request.method == 'DELETE':
        warehouse.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

#customerInfo
@api_view(['GET', 'POST'])
def customerInfo_list(request, format=None):
    if request.method == 'GET':
        customerInfos = CustomerInfo.objects.all()
        serializer = CustomerInfoSerializer(customerInfos, many=True)
        return Response({'customerInfos': serializer.data})
    elif request.method == 'POST':
        serializer = CustomerInfoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET','PUT', 'DELETE'])
def customerInfo_details(request, id, format=None):
    customerInfo = CustomerInfo.objects.get(pk=id)
    if request.method == 'GET':
        serializer = CustomerInfoSerializer(customerInfo)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = CustomerInfoSerializer(customerInfo, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data) 
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)   
    elif request.method == 'DELETE':
        customerInfo.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

#sensor data
@api_view(['GET','PUT'])
def sensorData_list(request, format=None):
    if request.method == 'GET':
        sensorDatas = SensorData.objects.all()
        serializer = SensorDataSerializer(sensorDatas, many=True)
        return Response({'sensorDatas': serializer.data})
    if request.method == 'PUT':
        serializer = SensorDataSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(['GET','PUT', 'DELETE'])
def sensorData_details(request, id, format=None):
    sensorData = SensorData.objects.get(pk=id)
    if request.method == 'GET':
        serializer = SensorDataSerializer(sensorData)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = SensorDataSerializer(sensorData, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data) 
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)   
    elif request.method == 'DELETE':
        sensorData.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)




