# from django.shortcuts import render
# from django.http.response import JsonResponse
# from rest_framework.parsers import JSONParser
# from rest_framework import status
# from django.shortcuts import render
# from sevenshadesapp.models import Search
# from sevenshadesapp.serializer import SearchSerializer
# from rest_framework.decorators import api_view


# @api_view(['GET','POST','DELETE'])
# def Search_Product(request):
#     try:
#         if request.method=='POST':
#             names=request.data['name']
           
#             adminLogin=AdminLogin.objects.all().filter(name=names)
#             admin_serializer=AdminLoginSerializer(adminLogin,many=True)
#             if(len(admin_serializer.data)==1):
                
#                 return JsonResponse({"data":admin_serializer.data,"message":'Success',"status":True},safe=False)
#         else:
#              return JsonResponse({"data":[],"message":'Fail ',"status":False},safe=False)
#     except Exception as e:
#         print("Error submit:",e)
#         return JsonResponse({"message":'Fail',"status":False},safe=False)