from django.shortcuts import render
from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser
from rest_framework import status
from django.shortcuts import render

from sevenshadesapp.models import MySubCategory
from sevenshadesapp.serializer import MySubCategorySerializer
from sevenshadesapp.serializer import MySubCategoryGetSerializer
from rest_framework.decorators import api_view


@api_view(['GET','POST','DELETE'])
def MySubCategory_Submit(request):
    try:
        if request.method=='POST':
            mysubcategory_serializer=MySubCategorySerializer(data=request.data)
        if(mysubcategory_serializer.is_valid()):
                mysubcategory_serializer.save()
                return JsonResponse({"message":'SubCategory Submitted Successfully',"status":True},safe=False)
        else:
             return JsonResponse({"message":'Fail to submit ',"status":False},safe=False)
    except Exception as e:
        print("Error submit:",e)
        return JsonResponse({"message":'Fail to submit ',"status":False},safe=False)
    



@api_view(['GET','POST','DELETE'])
def MySubCategory_List(request):
     try:
          if request.method=='GET':
            #    maincategory_list=MainCategory.get()
               mysubcategory_list=MySubCategory.objects.all()
               mysubcategory_serializer_list=MySubCategoryGetSerializer(mysubcategory_list,many=True)
            #    print(mysubcategory_serializer_list.data)
               return JsonResponse({"data":mysubcategory_serializer_list.data, "status":True})
          else:
               return JsonResponse({"data":[],"status":False},safe=False)
     except Exception as e :
          print('Error in Listing data',e)
          return JsonResponse({"data":[],"status":False},safe=False)



@api_view(['GET','POST','DELETE'])
def EditMySubCategory_Icon(request):
    try:
        if request.method=='POST':
                mysubcategory_data=MySubCategory.objects.get(pk=request.data['id'])
                mysubcategory_data.icon=request.data['icon']
                mysubcategory_data.save()
                return JsonResponse({"message":'SubCategory Icon Updated',"status":True},safe=False)
        else:
             return JsonResponse({"message":'Fail to update Icon ',"status":False},safe=False)
    except Exception as e:
        print("Error submit:",e)
        return JsonResponse({"message":'Fail to submit ',"status":False},safe=False)



@api_view(['GET','POST','DELETE'])
def EditMySubCategory_Data(request):
    try:
         if request.method=='POST':
                mysubcategory_data=MySubCategory.objects.get(pk=request.data['id'])
                mysubcategory_data.maincategoryid_id=request.data['maincategoryid']
                mysubcategory_data.subcategoryname=request.data['subcategoryname']
                mysubcategory_data.save()
                return JsonResponse({"message":'SubCategory Data Updated',"status":True},safe=False)
         else:
             return JsonResponse({"message":'Fail to update Data ',"status":False},safe=False)
    except Exception as e:
        print("Error submit:",e)
        return JsonResponse({"message":'Fail to delete ',"status":False},safe=False)



@api_view(['GET','POST','DELETE'])
def DeleteMySubCategory_Data(request):
    try:
        if request.method=='POST':
                mysubcategory_data=MySubCategory.objects.get(pk=request.data['id'])
               
                mysubcategory_data.delete()
                return JsonResponse({"message":'SubCategory Data Deleted',"status":True},safe=False)
        else:
             return JsonResponse({"message":'Fail to Delete Data ',"status":False},safe=False)
    except Exception as e:
        print("Error submit:",e)
        return JsonResponse({"message":'Fail to delete ',"status":False},safe=False)
