from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from .models import DataSet

from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from rest_framework import status
from .serializers import DataSerializers

from django.core.exceptions import ObjectDoesNotExist

from rest_framework.decorators import api_view
from rest_framework.response import Response

#class JSONResponse(HttpResponse):
#    def __init__(self,data,**kwargs):
#        content=JSONRenderer().render(data)
#        kwargs['content_type']="application/json"
#        super(JSONResponse,self).__init__(content,**kwargs)

#@csrf_exempt
@api_view(['GET','POST'])
def data_list(request):
    if request.method=='GET':
        datasets=DataSet.objects.all()
        dataserial=DataSerializers(datasets,many=True)
        return Response(dataserial.data)
    elif request.method=='POST':
        dataserial=DataSerializers(data=request.data)
        if dataserial.is_valid():
            dataserial.save()
            return Response(dataserial.data,status=status.HTTP_201_CREATED)
        return Response(dataserial.errors,status=status.HTTP_400_BAD_REQUEST)

#@csrf_exempt
@api_view(['GET','PUT','DELETE'])
def data_set_one(request,pk):
    try:
        dataset=DataSet.objects.get(pk=pk)
    except ObjectDoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method=='GET':
        dataserial=DataSerializers(dataset)
        return Response(dataserial.data)

    elif request.method=="PUT":
        dataserial=DataSerializers(dataset,data=request.data)
        if dataserial.is_valid():
            dataserial.save()
            return Response(dataserial.data)
        return Response(dataserial.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method=="DELETE":
        dataset.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

