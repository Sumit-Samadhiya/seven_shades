from django.shortcuts import render
from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser
from rest_framework import status
from django.shortcuts import render

from sevenshadesapp.models import SignUp,UserAddress
from sevenshadesapp.serializer import SignUpSerializer,UserAddressGetSerializer,UserAddressSerializer
from rest_framework.decorators import api_view

@api_view(['GET','POST','DELETE'])
def SignUp_Submit(request):
    try:
        if request.method=='POST':
            signup_serializer=SignUpSerializer(data=request.data)
        if(signup_serializer.is_valid()):
                signup_serializer.save()
                return JsonResponse({"message":'SignUp Successfully',"status":True},safe=False)
        else:
             return JsonResponse({"message":'Fail to SignUp ',"status":False},safe=False)
    except Exception as e:
        print("Error submit:",e)
        return JsonResponse({"message":'Fail to SignUp ',"status":False},safe=False)
    
@api_view(['GET','POST','DELETE'])
def CheckCostumerLogin(request):
    try:
        if request.method=='POST':
            mobile=request.data['mobileno']
            pwd = request.data['password']
           
            costumerLogin=SignUp.objects.all().filter(mobileno=mobile,password=pwd)
            costumer_serializer=SignUpSerializer(costumerLogin,many=True)
            if(len(costumer_serializer.data)==1):
                
                return JsonResponse({"data":costumer_serializer.data,"message":'Success',"status":True},safe=False)
        else:
             return JsonResponse({"data":[],"message":'Fail ',"status":False},safe=False)
    except Exception as e:
        print("Error submit:",e)
        return JsonResponse({"message":'Fail',"status":False},safe=False)
    

@api_view(['GET','POST','DELETE'])
def FetchUserAddress(request):
    try:
        if request.method=='POST':
            mobile=request.data['mobile']
            
           
            userAddress=UserAddress.objects.all().filter(mobileno=mobile)
            user_AddressSerializer=UserAddressGetSerializer(userAddress,many=True)
            
            if(len(user_AddressSerializer.data)>0):    
             return JsonResponse({"data":user_AddressSerializer.data,"status":True},safe=False)
            else:
             return JsonResponse({"data":user_AddressSerializer.data,"status":False},safe=True)   
        else:
             return JsonResponse({"data":[],"message":'Fail ',"status":False},safe=False)
    except Exception as e:
        print("Error submit:",e)
        return JsonResponse({"message":'Fail',"status":False},safe=False)
    

@api_view(['GET','POST','DELETE'])
def Address_Submit(request):
    try:
        
        if request.method=='POST':
            address_serializer=UserAddressSerializer(data=request.data)
        if(address_serializer.is_valid()):
                address_serializer.save()
                return JsonResponse({"message":'Data Submitted Successfully',"status":True},safe=False)
        else:
             return JsonResponse({"message":'Fail to submit ',"status":False},safe=False)
    except Exception as e:
        print("Error submit:",e)
        return JsonResponse({"message":'Fail to submit ',"status":False},safe=False)