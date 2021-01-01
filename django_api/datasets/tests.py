from django.utils.http import urlencode
from django.urls import reverse

from rest_framework import status
from rest_framework.test import APITestCase

from datasets.models import DataCat
from datasets import views

class DataCatTest(APITestCase):
    def post_category(self,kind):
        url=reverse(views.DataCatList.name)
        data={"kind":kind}
        response=self.client.post(url,data,format='json')
        return response

    def test_post_get_category(self):
        new_cat='newtest'
        response=self.post_category(new_cat)
        assert response.status_code == status.HTTP_201_CREATED
        assert DataCat.objects.count() ==1
        assert DataCat.objects.get().kind== new_cat

    def test_post_exist_cat(self):
        url=reverse(views.DataCatList.name)
        new_cat="duplicated"
        data={'kind':new_cat}
        res1=self.post_category(new_cat)
        assert res1.status_code == status.HTTP_201_CREATED
        res2=self.post_category(new_cat)
        print(res2)
        assert res2.status_code == status.HTTP_400_BAD_REQUEST

    def test_filter_cat(self):
        cat_name='newtest'
        self.post_category(cat_name)
        cat_name2=''
        self.post_category(cat_name2)
        filter_by_kind={'kind':cat_name}
        url='{0}?{1}'.format(reverse(views.DataCatList.name),urlencode(filter_by_kind))
        print(url)
        res=self.client.get(url,format='json')
        assert res.status_code == status.HTTP_200_OK
        assert res.data['count'] == 1
        assert res.data['results'][0]['kind']==cat_name
