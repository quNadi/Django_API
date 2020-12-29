from django.http import HttpResponse
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.reverse import reverse
from django.views.decorators.csrf import csrf_exempt
from .models import DataSet,DataPackage,DataCat,Researcher

from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from rest_framework import status,generics
from .serializers import DataSerializers ,DataCatSerializer,DataPackageSerial,ResearcherSerial,ResearcherPackageSerial

from django.core.exceptions import ObjectDoesNotExist

from rest_framework.decorators import api_view
from rest_framework.response import Response

from rest_framework import permissions
from .permissionsuser import IsUserOwnerReadOnly

from rest_framework.authentication import  TokenAuthentication
from rest_framework.permissions import IsAuthenticated

class DataCatList(generics.ListCreateAPIView):
    queryset =DataCat.objects.all()
    serializer_class = DataCatSerializer
    name='datacat-list'
    filter_fields=(
        'kind' ,
    )
    search_fields=(
        'kind'   ,
    )
    ordering_fields=(
        'kind' ,
    )

class DataCatDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset =DataCat.objects.all()
    serializer_class = DataCatSerializer
    name='datacat-detail'

class DataList(generics.ListCreateAPIView):
    queryset = DataSet.objects.all()
    serializer_class = DataSerializers
    name='dataset-list'
    filter_fields=(
        'title',
        'category',
        'set',
        'content',
        'inserted' ,
    )
    search_fields=(
        '^title',
    )
    ordering_fields=(
        'title',
        'inserted',
    )

    permission_classes = (
        permissions.IsAuthenticatedOrReadOnly,
        IsUserOwnerReadOnly,
    )

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

class DataDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = DataSet.objects.all()
    serializer_class = DataSerializers
    name = 'dataset-detail'

    permission_classes = (
        permissions.IsAuthenticatedOrReadOnly,
        IsUserOwnerReadOnly,
    )

class ResearcherList(generics.ListCreateAPIView):
    queryset = Researcher.objects.all()
    serializer_class = ResearcherSerial
    name='researcher-list'
    filter_fields=(
        'name',
        'origin',
        'inserted'  ,
    )
    search_fields=(
        '^name' ,
    )
    ordering_fields=(
        'name',
        'inserted',
    )

    authentication_classes = (
        TokenAuthentication,
    )
    permission_classes = (
        IsAuthenticated,
    )

class ResearcherDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Researcher.objects.all()
    serializer_class = ResearcherSerial
    name="researcher-detail"

    authentication_classes = (
        TokenAuthentication,
    )
    permission_classes = (
        IsAuthenticated,
    )

class DataPackList(generics.ListCreateAPIView):
    queryset = DataPackage.objects.all()
    serializer_class = ResearcherPackageSerial
    name='pack-list'

    ordering_fields=(
        'type_class'   ,
    )

class DataPackDetail(generics.RetrieveUpdateDestroyAPIView):
    query_set=DataPackage.objects.all()
    serializer_class = ResearcherPackageSerial
    name='pack-detail'



class ApiRoot(generics.GenericAPIView):
    name='api-root'
    def get(self,request,*args,**kwargs):
        return Response({
            'data-categories':reverse(DataCatList.name,request=request),
            'datasets':reverse(DataList.name,request=request)  ,
            'researchers':reverse(ResearcherList.name,request=request)  ,
            'packages':reverse(DataPackList.name,request=request)
        })


#class JSONResponse(HttpResponse):
#    def __init__(self,data,**kwargs):
#        content=JSONRenderer().render(data)
#        kwargs['content_type']="application/json"
#        super(JSONResponse,self).__init__(content,**kwargs)

#@csrf_exempt
#@api_view(['GET','POST'])
#def data_list(request):
#    if request.method=='GET':
#        datasets=DataSet.objects.all()
#        dataserial=DataSerializers(datasets,many=True)
#        return Response(dataserial.data)
#    elif request.method=='POST':
#        dataserial=DataSerializers(data=request.data)
#        if dataserial.is_valid():
#            dataserial.save()
#            return Response(dataserial.data,status=status.HTTP_201_CREATED)
#        return Response(dataserial.errors,status=status.HTTP_400_BAD_REQUEST)
#
##@csrf_exempt
#@api_view(['GET','PUT','DELETE'])
#def data_set_one(request,pk):
#    try:
#        dataset=DataSet.objects.get(pk=pk)
#    except ObjectDoesNotExist:
#        return Response(status=status.HTTP_404_NOT_FOUND)
#
#    if request.method=='GET':
#        dataserial=DataSerializers(dataset)
#        return Response(dataserial.data)
#
#    elif request.method=="PUT":
#        dataserial=DataSerializers(dataset,data=request.data)
#        if dataserial.is_valid():
#            dataserial.save()
#            return Response(dataserial.data)
#        return Response(dataserial.errors, status=status.HTTP_400_BAD_REQUEST)
#    elif request.method=="DELETE":
#        dataset.delete()
#        return Response(status=status.HTTP_204_NO_CONTENT)

