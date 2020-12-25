from django.urls import include,path
from django.conf.urls import url

from .views import data_list,data_set_one

urlpatterns=[
    path('',data_list),
    path('<int:pk>',data_set_one)
]