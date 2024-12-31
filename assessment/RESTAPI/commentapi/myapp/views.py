from django.shortcuts import render
from .models import*
from  .serializers import*
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view


# Create your views here.

def index(request):
    return render(request,'index.html')

@api_view(['GET'])
def getallcomments(request):
    commentdata=commentmodel.objects.all()
    serial=comentserializers(commentdata,many=True)
    return Response(serial.data)

@api_view(['POST'])    
def insertcomments(request):
    if request.method=='POST':
        serial=comentserializers(data=request.data)
        if serial.is_valid():
            serial.save()
            return Response(status=status.HTTP_201_CREATED)
        else :
            return Response(status=status.HTTP_400_BAD_REQUEST)
        

@ api_view(['PUT','GET'])
def updatecomments(request,id):
    try:
         commentid=commentmodel.objects.get(id=id)
    except commentmodel.DoesNotExist:
        return Response( status=status.HTTP_404_NOT_FOUND)
    if request.method=='GET':
        serial=comentserializers(commentid)
        return Response(serial.data,status=status.HTTP_200_OK)
    if request.method=='PUT':
        serial=comentserializers(data=request.data,instance=commentid)
        if serial.is_valid():
            serial.save()
            return Response(status=status.HTTP_202_ACCEPTED)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)  

@api_view(['DELETE','GET'])
def deletecomments(request,id):
    try:
        commentid=commentmodel.objects.get(id=id)
    except commentmodel.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method=='GET':
        serial=comentserializers(commentid)
        return Response(serial.data,status=status.HTTP_200_OK)
    if request.method=='DELETE':
        commentmodel.delete(commentid)
        return Response(status=status.HTTP_202_ACCEPTED)    




        
