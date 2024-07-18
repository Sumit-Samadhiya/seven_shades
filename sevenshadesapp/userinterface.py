from django.shortcuts import render
from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser
from rest_framework import status
from django.shortcuts import render
from sevenshadesapp.models import MainCategory,MySubCategory,Brands,Product,Banner,ProductDetails
from sevenshadesapp.serializer import MainCategorySerializer,MySubCategorySerializer,MySubCategoryGetSerializer,BrandsSerializer,ProductGetSerializer,BannerSerializer,ProductDetailsGetSerializer
from rest_framework.decorators import api_view


@api_view(['GET','POST','DELETE'])
def User_MainCategory_List(request):
     try:
          if request.method=='GET':
            #    maincategory_list=MainCategory.get()
               maincategory_list=MainCategory.objects.all()
               maincategory_serializer_list=MainCategorySerializer(maincategory_list,many=True)
               return JsonResponse({"data":maincategory_serializer_list.data, "status":True})
          else:
               return JsonResponse({"data":[],"status":False},safe=False)
     except Exception as e :
          print('Error in Listing data',e)
          return JsonResponse({"data":[],"status":False},safe=False)
               
@api_view(['GET','POST','DELETE'])
def user_mysubcategory_list_by_maincategoryid(request):
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
     


@api_view(['GET','POST','DELETE'])
def Brands_List(request):
     try:
          if request.method=='POST':
            #    maincategory_list=MainCategory.get()
               sid=request.data['subcategoryid']
               mid=request.data['maincategoryid']
               product_list=Product.objects.all().filter(subcategoryid_id=sid, maincategoryid_id=mid)
               product_serializer_list=ProductGetSerializer(product_list,many=True)
               finalresult=fetchData('brandid',product_serializer_list.data)
               return JsonResponse({"data":finalresult, "status":True})
          else:
               return JsonResponse({"data":[],"status":False},safe=False)
     except Exception as e :
          print('Error in Listing data',e)
          return JsonResponse({"data":[],"status":False},safe=False)
     
def fetchData(field,data):
     data=list(data)
     result={}
     for row in data:
          mydata=dict(row)
          print(dict(mydata[field]))
          record=(dict(mydata[field]))
          result[record['id']]=record
     finalresult=list(result.values())
     return(finalresult)


   
@api_view(['GET','POST','DELETE'])
def Banner_List(request):
     try:
          if request.method=='GET':
            #    maincategory_list=MainCategory.get()
               banner_list=Banner.objects.all()
               banner_serializer_list=BannerSerializer(banner_list,many=True)
               return JsonResponse({"data":banner_serializer_list.data[0], "status":True})
          else:
               return JsonResponse({"data":[],"status":False},safe=False)
     except Exception as e :
          print('Error in Listing data',e)
          return JsonResponse({"data":[],"status":False},safe=False)
     

@api_view(['GET','POST','DELETE'])
def Subcategory_List(request):
     try:
          if request.method=='GET':
         
               mysubcategory_list=MySubCategory.objects.all()
               mysubcategory_serializer_list=MySubCategorySerializer(mysubcategory_list,many=True)
               return JsonResponse({"data":mysubcategory_serializer_list.data, "status":True})
          else:
               return JsonResponse({"data":[],"status":False},safe=False)
     except Exception as e :
          print('Error in Listing data',e)
          return JsonResponse({"data":[],"status":False},safe=False)
     
@api_view(['GET','POST','DELETE'])
def Category_List(request):
     try:
          if request.method=='GET':
         
               maincategory_list=MainCategory.objects.all()
               maincategory_serializer_list=MainCategorySerializer(maincategory_list,many=True)
               return JsonResponse({"data":maincategory_serializer_list.data, "status":True})
          else:
               return JsonResponse({"data":[],"status":False},safe=False)
     except Exception as e :
          print('Error in Listing data',e)
          return JsonResponse({"data":[],"status":False},safe=False)
     

@api_view(['GET','POST','DELETE'])
def Brands_List(request):
     try:
          if request.method=='GET':
         
               brand_list=Brands.objects.all()
               brand_serializer_list=BrandsSerializer(brand_list,many=True)
               return JsonResponse({"data":brand_serializer_list.data, "status":True})
          else:
               return JsonResponse({"data":[],"status":False},safe=False)
     except Exception as e :
          print('Error in Listing data',e)
          return JsonResponse({"data":[],"status":False},safe=False)
     

@api_view(['GET','POST','DELETE'])
def MainCategory_List(request):
     try:
          if request.method=='GET':
         
               maincategory_list=MainCategory.objects.all()
               maincategory_serializer_list=MainCategorySerializer(maincategory_list,many=True)
               return JsonResponse({"data":maincategory_serializer_list.data, "status":True})
          else:
               return JsonResponse({"data":[],"status":False},safe=False)
     except Exception as e :
          print('Error in Listing data',e)
          return JsonResponse({"data":[],"status":False},safe=False)
     

@api_view(['GET','POST','DELETE'])
def User_Products_Maincategory(request):
     try:
          if request.method=='POST':
            
               maincategoryid=request.data['maincategoryid']
               product_list=Product.objects.all().filter(maincategoryid=maincategoryid)
               product_serializer_list=ProductGetSerializer(product_list,many=True)
               
              
               return JsonResponse({"data":product_serializer_list.data, "status":True})
          else:
               return JsonResponse({"data":[],"status":False},safe=False)
     except Exception as e :
          print('Error in Listing data',e)
          return JsonResponse({"data":[],"status":False},safe=False)
     

@api_view(['GET','POST','DELETE'])
def User_ProductsDetails_By_Id(request):
     try:
          if request.method=='POST':
            
               productid=request.data['productid']
               productdetails_list=ProductDetails.objects.all().filter(productid_id=productid)
               productdetails_serializer_list=ProductDetailsGetSerializer(productdetails_list,many=True)
               print(productdetails_serializer_list.data)
               
              
               return JsonResponse({"data":productdetails_serializer_list.data, "status":True})
          else:
               return JsonResponse({"data":[],"status":False},safe=False)
     except Exception as e :
          print('Error in Listing data',e)
          return JsonResponse({"data":[],"status":False},safe=False)