from django.shortcuts import render
from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser
from rest_framework import status
from django.shortcuts import render

from sevenshadesapp.models import MySubCategory
from sevenshadesapp.models import Product
from sevenshadesapp.serializer import MySubCategorySerializer
from sevenshadesapp.serializer import MySubCategoryGetSerializer
from sevenshadesapp.serializer import ProductSerializer
from sevenshadesapp.serializer import ProductGetSerializer
from rest_framework.decorators import api_view


@api_view(['GET','POST','DELETE'])
def Product_Submit(request):
    try:
        if request.method=='POST':
            product_serializer=ProductSerializer(data=request.data)
        if(product_serializer.is_valid()):
                product_serializer.save()
                return JsonResponse({"message":'Product Submitted Successfully',"status":True},safe=False)
        else:
             return JsonResponse({"message":'Fail to submit ',"status":False},safe=False)
    except Exception as e:
        print("Error submit:",e)
        return JsonResponse({"message":'Fail to submit ',"status":False},safe=False)
    
    
@api_view(['GET','POST','DELETE'])
def mysubcategory_list_by_maincategoryid(request):
     try:
          if request.method=='POST':
            #    maincategory_list=MainCategory.get()
               maincategoryid=request.data['maincategoryid']
               mysubcategory_list=MySubCategory.objects.all().filter(maincategoryid=maincategoryid)
               mysubcategory_serializer_list=MySubCategoryGetSerializer(mysubcategory_list,many=True)
            #    print(mysubcategory_serializer_list.data)
               print("hey")
               return JsonResponse({"data":mysubcategory_serializer_list.data, "status":True})
          else:
               return JsonResponse({"data":[],"status":False},safe=False)
     except Exception as e :
          print('Error in Listing data',e)
          return JsonResponse({"data":[],"status":False},safe=False)

def Product_List(request):
     try:
          if request.method=='GET':
            #    maincategory_list=MainCategory.get()
               product_list=Product.objects.all()
               product_serializer_list=ProductGetSerializer(product_list,many=True)
            #    print(mysubcategory_serializer_list.data)
               return JsonResponse({"data":product_serializer_list.data, "status":True})
          else:
               return JsonResponse({"data":[],"status":False},safe=False)
     except Exception as e :
          print('Error in Listing data',e)
          return JsonResponse({"data":[],"status":False},safe=False)



@api_view(['GET','POST','DELETE'])
def EditProduct_Icon(request):
    try:
        if request.method=='POST':
                product_data=Product.objects.get(pk=request.data['id'])
                product_data.icon=request.data['icon']
                product_data.save()
                return JsonResponse({"message":'Product Icon Updated',"status":True},safe=False)
        else:
             return JsonResponse({"message":'Fail to update Icon ',"status":False},safe=False)
    except Exception as e:
        print("Error submit:",e)
        return JsonResponse({"message":'Fail to submit ',"status":False},safe=False)



@api_view(['GET','POST','DELETE'])
def EditProduct_Data(request):
    try:
         if request.method=='POST':
                product_data=Product.objects.get(pk=request.data['id'])
                product_data.maincategoryid_id=request.data['maincategoryid']
                product_data.subcategoryid_id=request.data['subcategoryid']
                product_data.brandid_id=request.data['brandid']
                product_data.productname=request.data['productname']
                product_data.description=request.data['description']
                product_data.save()
                return JsonResponse({"message":'Product Data Updated',"status":True},safe=False)
         else:
             return JsonResponse({"message":'Fail to update Data ',"status":False},safe=False)
    except Exception as e:
        print("Error submit:",e)
        return JsonResponse({"message":'Fail to update ',"status":False},safe=False)



@api_view(['GET','POST','DELETE'])
def DeleteProduct_Data(request):
    try:
        if request.method=='POST':
                product_data=Product.objects.get(pk=request.data['id'])
               
                product_data.delete()
                return JsonResponse({"message":'Product Data Deleted',"status":True},safe=False)
        else:
             return JsonResponse({"message":'Fail to Delete Data ',"status":False},safe=False)
    except Exception as e:
        print("Error submit:",e)
        return JsonResponse({"message":'Fail to delete ',"status":False},safe=False)
