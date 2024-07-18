from django.shortcuts import render
from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser
from rest_framework import status
from django.shortcuts import render

from sevenshadesapp.models import MySubCategory
from sevenshadesapp.models import Product,ProductDetails,Brands

from sevenshadesapp.serializer import MySubCategorySerializer
from sevenshadesapp.serializer import MySubCategoryGetSerializer
from sevenshadesapp.serializer import ProductSerializer,ProductDetailsSerializer,ProductDetailsGetSerializer,BrandsSerializer
from sevenshadesapp.serializer import ProductGetSerializer
from rest_framework.decorators import api_view
from django.core.files.storage import default_storage



def Upload_Files(files):
     iconname=[]
     for uploaded_file in files.getlist('icon'):
          file_path = default_storage.save('static/' + uploaded_file.name,uploaded_file)
          print(file_path)
          iconname.append(uploaded_file.name)
     return ",".join(iconname)



@api_view(['GET','POST','DELETE'])
def ProductDetails_Submit(request):
    try:
        if request.method=='POST':
            print("filesss",dict(request.FILES))
            filenames=Upload_Files(request.FILES)
            request.data['icon']=filenames
            print(request.data)
            productdetails_serializer=ProductDetailsSerializer(data=request.data)
        if(productdetails_serializer.is_valid()):
                productdetails_serializer.save()
                return JsonResponse({"message":'Product Details Submitted Successfully',"status":True},safe=False)
        else:
             return JsonResponse({"message":'Fail to submit ',"status":False},safe=False)
    except Exception as e:
        print("Error submit:",e)
        return JsonResponse({"message":'Fail to submit ',"status":False},safe=False)
    
@api_view(['GET','POST','DELETE'])
def Productdetail_product_list_by_subcategoryid(request):
     try:
          if request.method=='POST':
            #    maincategory_list=MainCategory.get()
               sid=request.data['subcategoryid']
               product_list=Product.objects.all().filter(subcategoryid_id=sid)
               product_serializer_list=ProductGetSerializer(product_list,many=True)
               print(product_serializer_list.data)
               return JsonResponse({"data":product_serializer_list.data, "status":True})
          else:
               return JsonResponse({"data":[],"status":False},safe=False)
     except Exception as e :
          print('Error in Listing data',e)
          return JsonResponse({"data":[],"status":False},safe=False)
     
@api_view(['GET','POST','DELETE'])
def Productdetail_brand_list_by_productid(request):
     try:
          if request.method=='POST':
            #    maincategory_list=MainCategory.get()
               pid=request.data['productid']
               brand_list=Product.objects.all().filter(id=pid)
               brand_serializer_list=ProductGetSerializer(brand_list,many=True)
            #    print(brand_serializer_list.data)
               return JsonResponse({"data":brand_serializer_list.data, "status":True})
          else:
               return JsonResponse({"data":[],"status":False},safe=False)
     except Exception as e :
          print('Error in Listing data',e)
          return JsonResponse({"data":[],"status":False},safe=False)
     
def ProductDetails_List(request):
     try:
          if request.method=='GET':
            #    maincategory_list=MainCategory.get()
               productdetails_list=ProductDetails.objects.all()
               productdetails_serializer_list=ProductDetailsGetSerializer(productdetails_list,many=True)
               print(productdetails_serializer_list.data)
               return JsonResponse({"data":productdetails_serializer_list.data, "status":True})
          else:
               return JsonResponse({"data":[],"status":False},safe=False)
     except Exception as e :
          print('Error in Listing data',e)
          return JsonResponse({"data":[],"status":False},safe=False)


@api_view(['GET','POST','DELETE'])
def EditProductDetails_Icon(request):
    try:
        if request.method=='POST':
                productdetails_data=ProductDetails.objects.get(pk=request.data['id'])
                productdetails_data.icon=request.data['icon']
                productdetails_data.save()
                return JsonResponse({"message":'Product Icon Updated',"status":True},safe=False)
        else:
             return JsonResponse({"message":'Fail to update Icon ',"status":False},safe=False)
    except Exception as e:
        print("Error submit:",e)
        return JsonResponse({"message":'Fail to submit ',"status":False},safe=False)



@api_view(['GET','POST','DELETE'])
def EditProductDetails_Data(request):
    try:
         if request.method=='POST':
                productdetails_data=ProductDetails.objects.get(pk=request.data['id'])
                productdetails_data.maincategoryid_id=request.data['maincategoryid']
                productdetails_data.subcategoryid_id=request.data['subcategoryid']
                productdetails_data.brandid_id=request.data['brandid']
                productdetails_data.productid_id=request.data['productid']
                productdetails_data.productsubname=request.data['productsubname']
                productdetails_data.description=request.data['description']
                productdetails_data.qty=request.data['qty']
                productdetails_data.price=request.data['price']
                productdetails_data.color=request.data['color']
                productdetails_data.size=request.data['size']
                productdetails_data.offerprice=request.data['offerprice']
                productdetails_data.offertype=request.data['offertype']
                productdetails_data.save()
                return JsonResponse({"message":'Product Data Updated',"status":True},safe=False)
         else:
             return JsonResponse({"message":'Fail to update Data ',"status":False},safe=False)
    except Exception as e:
        print("Error submit:",e)
        return JsonResponse({"message":'Fail to update ',"status":False},safe=False)



@api_view(['GET','POST','DELETE'])
def DeleteProductDetails_Data(request):
    try:
        if request.method=='POST':
                productdetails_data=ProductDetails.objects.get(pk=request.data['id'])
               
                productdetails_data.delete()
                return JsonResponse({"message":'Product Data Deleted',"status":True},safe=False)
        else:
             return JsonResponse({"message":'Fail to Delete Data ',"status":False},safe=False)
    except Exception as e:
        print("Error submit:",e)
        return JsonResponse({"message":'Fail to delete ',"status":False},safe=False)
