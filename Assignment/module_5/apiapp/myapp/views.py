from django.shortcuts import render
from .serializers import *
from .models import*
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status


# Create your views here.
def index(request):
    return render(request,'index.html')

@api_view(['GET'])
def getall(request):
    bookdata=book.objects.all()
    serial=bookserial(bookdata,many=True)
    return Response(serial.data)

@api_view(['GET'])
def getbookid(request,id):
    try:
       bookid=book.objects.get(id=id)
    except book.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    serial=bookserial(bookid)
    return Response(serial.data,status=status.HTTP_200_OK)

@api_view(['DELETE','GET'])
def deletebookid(request,id):
    try:
        bookid=book.objects.get(id=id)
    except book.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method=='GET':
        serial=bookserial(bookid)
        return Response(serial.data,status=status.HTTP_200_OK)
    if request.method=='DELETE':
        book.delete(bookid)
        return Response(status=status.HTTP_202_ACCEPTED)
         

@api_view(['POST']) 
def insertdata(request):
    if request.method=="POST":
        serial=bookserial(data=request.data)
        if serial.is_valid():
            serial.save()
            return Response(status=status.HTTP_201_CREATED)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        

@api_view(['PUT','GET'])
def updatebookdata(request,id):
    try:
        bookid=book.objects.get(id=id)
    except book.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method=='GET':
        serial=bookserial(bookid)
        return Response(serial.data,status=status.HTTP_200_OK)
    if request.method=="PUT":
        serial=bookserial(data=request.data,instance=bookid)
        if serial.is_valid():
           serial.save()
           return Response(status=status.HTTP_202_ACCEPTED)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)


        
     








