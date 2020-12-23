from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from .models import DataSet

from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from rest_framework import status
from .serializers import DataSerializers

from django.core.exceptions import ObjectDoesNotExist

class JSONResponse(HttpResponse):
    def __init__(self,data,**kwargs):
        content=JSONRenderer().render(data)
        kwargs['content_type']="application/json"
        super(JSONResponse,self).__init__(content,**kwargs)

@csrf_exempt
def data_list(request):
    if request.method=='GET':
        datasets=DataSet.objects.all()
        dataserial=DataSerializers(datasets,many=True)
        return JSONResponse(dataserial.data)
    elif request.method=='POST':
        data_set=JSONParser().parse(request)
        dataserial=DataSerializers(data=data_set)
        if dataserial.is_valid():
            dataserial.save()
            return JSONResponse(dataserial.data,status=status.HTTP_201_CREATED)
        return JSONResponse(dataserial.errors,status=status.HTTP_400_BAD_REQUEST)

@csrf_exempt
def data_set_one(request,pk):
    try:
        dataset=DataSet.objects.get(pk=pk)
    except ObjectDoesNotExist:
        return HttpResponse(status=status.HTTP_404_NOT_FOUND)

    if request.method=='GET':
        dataserial=DataSerializers(dataset)
        return JSONResponse(dataserial.data)

    elif request.method=="PUT":
        data_set=JSONParser().parse(request)
        dataserial=DataSerializers(dataset,data=data_set)
        if dataserial.is_valid():
            dataserial.save()
            return JSONResponse(dataserial.data)
        return JSONResponse(dataserial.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method=="DELETE":
        dataset.delete()
        return HttpResponse(status=status.HTTP_204_NO_CONTENT)

