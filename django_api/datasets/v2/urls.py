from django.urls import path


from datasets.views import DataPackList,DataList,DataDetail,DataCatDetail,DataCatList,DataPackDetail,ResearcherDetail,ResearcherList,ApiRoot
import datasets.v2.views as views2

app_name='v2'

urlpatterns=[
    path('kategorie/',DataCatList.as_view(),name=DataCatList.name),
    path('kategorie/<int:pk>',DataCatDetail.as_view(),name=DataCatDetail.name),
    path('dane/',DataList.as_view(),name=DataList.name),
    path('dane/<int:pk>',DataDetail.as_view(),name=DataDetail.name),
    path('badacze/',ResearcherList.as_view(),name=ResearcherList.name) ,
    path('badacze/<int:pk>',ResearcherDetail.as_view(),name=ResearcherDetail.name) ,
    path('pakiety/',DataPackList.as_view(),name=DataPackList.name) ,
    path('pakiety/<int:pk>',DataPackDetail.as_view(),name=DataPackDetail.name),
    path('',views2.ApiRoot2.as_view(),name=views2.ApiRoot2.name) ,]