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
        print("pk {0}".format(DataCat.objects.get().pk))
        assert DataCat.objects.count() ==1
        assert DataCat.objects.get().name== new_cat
