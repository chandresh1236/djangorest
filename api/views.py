from django.shortcuts import render
from rest_framework.response import Response
from .models import Songs
from .serializers import SongsSerializer
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.renderers import JSONRenderer
# Create your views here.

class SongsAPI(APIView):
 def get(self, request, pk=None, format=None):
  id = pk
  print(id)
  if id:
   stu = Songs.objects.filter(platform=id)
   serializer = SongsSerializer(stu,many=True)
   print(type(serializer.data))
   
   return Response({"artist_name": serializer.validated_data})
   print(stu)

  #stu = Songs.objects.all()
  stu = Songs.objects.all()
  s = []
  for i in stu:
      m = Songs( song_title=str(i.song_title))
      
  
  
  
#   for i in stu:
#       s.append(i)
  print(s)     
  
  serializer = SongsSerializer(stu,many=True)
#   json_data = JSONRenderer().render(serializer.data)
#   print(json_data)
  return Response({"song_title": serializer.data[0][]})

 def post(self, request, format=None):
  serializer = SongsSerializer(data=request.data)
  if serializer.is_valid():
   serializer.save()
   return Response({'msg':'Data Created'}, status=status.HTTP_201_CREATED)
  return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

 def put(self, request, pk, format=None):
  id = pk
  stu = Songs.objects.get(pk=id)
  serializer = SongsSerializer(stu, data=request.data)
  if serializer.is_valid():
   serializer.save()
   return Response({'msg':'Complete Data Updated'})
  return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

 def patch(self, request, pk, format=None):
  id = pk
  stu = Songs.objects.get(pk=id)
  serializer = SongsSerializer(stu, data=request.data, partial=True)
  if serializer.is_valid():
   serializer.save()
   return Response({'msg':'Partial Data Updated'})
  return Response(serializer.errors)

 def delete(self, request, pk, format=None):
  id = pk
  stu = Songs.objects.get(pk=id)
  stu.delete()
  return Response({'msg':'Data Deleted'})