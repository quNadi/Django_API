from rest_framework import serializers
from .models import DataSet


class DataSerializers(serializers.Serializer):
    pk=serializers.IntegerField(read_only=True)
    title=serializers.CharField(max_length=50)
    content=serializers.CharField(max_length=100)
    set=serializers.IntegerField()

    def create(self, validated_data):
        return DataSet.objects.create(**validated_data)

    def update(self,instance,validated_date):
        instance.title=validated_date.get('title',instance.title)
        instance.content=validated_date.get('content',instance.content)
        instance.set=validated_date.get('set',instance.set)
        instance.save()
        return instance