from rest_framework import serializers
from .models import DataSet


class DataSerializers(serializers.ModelSerializer):
    class Meta:
        model=DataSet
        fields=('id',
                'title',
                'content',
                'set')


#    def create(self, validated_data):
#        return DataSet.objects.create(**validated_data)
#
#    def update(self,instance,validated_date):
#        instance.title=validated_date.get('title',instance.title)
#        instance.content=validated_date.get('content',instance.content)
#        instance.set=validated_date.get('set',instance.set)
#        instance.save()
#        return instance