from django.shortcuts import render
from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser
from rest_framework import status
from django.shortcuts import render
from sevenshadesapp.models import MainCategory,Brands,Product
from sevenshadesapp.serializer import MainCategorySerializer,BrandsSerializer
from rest_framework.decorators import api_view


@api_view(['GET','POST','DELETE'])
def Brands_Submit(request):
    try:
        if request.method=='POST':
            brands_serializer=BrandsSerializer(data=request.data)
        if(brands_serializer.is_valid()):
                brands_serializer.save()
                return JsonResponse({"message":'Brands Submitted Successfully',"status":True},safe=False)
        else:
             return JsonResponse({"message":'Fail to submit ',"status":False},safe=False)
    except Exception as e:
        print("Error submit:",e)
        return JsonResponse({"message":'Fail to submit ',"status":False},safe=False)
    
@api_view(['GET','POST','DELETE'])
def Brands_List(request):
     try:
          if request.method=='GET':
            #    maincategory_list=MainCategory.get()
               brands_list=Brands.objects.all()
               brands_serializer_list=BrandsSerializer(brands_list,many=True)
               return JsonResponse({"data":brands_serializer_list.data, "status":True})
          else:
               return JsonResponse({"data":[],"status":False},safe=False)
     except Exception as e :
          print('Error in Listing data',e)
          return JsonResponse({"data":[],"status":False},safe=False)
               
@api_view(['GET','POST','DELETE'])
def EditBrands_Icon(request):
    try:
        if request.method=='POST':
                brands_data=Brands.objects.get(pk=request.data['id'])
                brands_data.icon=request.data['icon']
                brands_data.save()
                return JsonResponse({"message":'Brand Icon Updated',"status":True},safe=False)
        else:
             return JsonResponse({"message":'Fail to update Icon ',"status":False},safe=False)
    except Exception as e:
        print("Error submit:",e)
        return JsonResponse({"message":'Fail to submit ',"status":False},safe=False)



@api_view(['GET','POST','DELETE'])
def EditBrands_Data(request):
    try:
         if request.method=='POST':
                brands_data=Brands.objects.get(pk=request.data['id'])
                brands_data.brandname=request.data['brandname']
                brands_data.save()
                return JsonResponse({"message":'Brand Data Updated',"status":True},safe=False)
         else:
             return JsonResponse({"message":'Fail to delete Data ',"status":False},safe=False)
    except Exception as e:
        print("Error submit:",e)
        return JsonResponse({"message":'Fail to delete ',"status":False},safe=False)



@api_view(['GET','POST','DELETE'])
def DeleteBrands_Data(request):
    try:
        if request.method=='POST':
                brands_data=Brands.objects.get(pk=request.data['id'])
               
                brands_data.delete()
                return JsonResponse({"message":'Brands Data Deleted',"status":True},safe=False)
        else:
             return JsonResponse({"message":'Fail to Delete Data ',"status":False},safe=False)
    except Exception as e:
        print("Error submit:",e)
        return JsonResponse({"message":'Fail to delete ',"status":False},safe=False)
