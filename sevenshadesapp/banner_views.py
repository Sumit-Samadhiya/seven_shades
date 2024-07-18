from rest_framework.decorators import api_view
from django.core.files.storage import default_storage
from django.shortcuts import render
from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser
from rest_framework import status
from django.shortcuts import render
from sevenshadesapp.models import Banner
from sevenshadesapp.serializer import BannerSerializer



def Upload_Files(files):
     iconname=[]
     for uploaded_file in files.getlist('icon'):
          file_path = default_storage.save('static/' + uploaded_file.name,uploaded_file)
          print(file_path)
          iconname.append(uploaded_file.name)
     return ",".join(iconname)


@api_view(['GET','POST','DELETE'])
def Banner_Submit(request):
    try:
        if request.method=='POST':
            print("filesss",dict(request.FILES))
            filenames=Upload_Files(request.FILES)
            request.data['icon']=filenames
            print(request.data)
            banner_serializer=BannerSerializer(data=request.data)
        if(banner_serializer.is_valid()):
                banner_serializer.save()
                return JsonResponse({"message":'Banner Submitted Successfully',"status":True},safe=False)
        else:
             return JsonResponse({"message":'Fail to submit ',"status":False},safe=False)
    except Exception as e:
        print("Error submit:",e)
        return JsonResponse({"message":'Fail to submit ',"status":False},safe=False)