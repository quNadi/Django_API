from rest_framework import generics
from rest_framework.response import Response
from rest_framework.reverse import reverse

from datasets.views import DataCatList, DataList,DataPackList,ResearcherList


class ApiRoot2(generics.GenericAPIView):
    name='api-root'
    def get(self,request,*args,**kwargs):
        return Response({
            'kateogrie':reverse(DataCatList.name,request=request),
            'dane':reverse(DataList.name,request=request),
            'badacze':reverse(ResearcherList.name,request=request),
            'pakiety':reverse(DataPackList.name,request=request)
        })

