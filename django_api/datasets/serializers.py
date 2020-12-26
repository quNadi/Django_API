from rest_framework import serializers
from .models import DataSet,DataCat,DataPackage,Researcher


class DataCatSerializer(serializers.HyperlinkedModelSerializer):
    datasets=serializers.HyperlinkedRelatedField(
        many=True,
        read_only=True,
        view_name='data-detail')
    class Meta:
        model=DataCat
        fields=(
            'url',
            'pk',
            'kind',
            'datasets'
        )



class DataSerializers(serializers.ModelSerializer):
    data_cat=serializers.SlugRelatedField(queryset=DataCat.objects.all(),slug_field='title')
    class Meta:
        model=DataSet
        fields=('url',
                'title',
                'content',
                'set',
                'category',
                'inserted')


class DataPackageSerial(serializers.HyperlinkedModelSerializer):
    dataset=DataSerializers()
    class Meta:
        model= DataPackage
        fields=(
            'url',
            'pk',
            'class_type'
            'dataset'
        )


class ResearcherSerial(serializers.HyperlinkedModelSerializer):
    datapack = DataPackageSerial()
    origin=serializers.ChoiceField(
        choices=Researcher.CHOICES
    )
    class Meta:
        model=Researcher
        fields=(
            'url',
            'name',
            'origin',
            'inserted',
            'datapack'
        )

class ResearcherPackageSerial(serializers.ModelSerializer):
    researcher=serializers.SlugRelatedField(queryset=Researcher.objects.all(),slug_field='name')
    dataset=serializers.SlugRelatedField(queryset=DataSet.objects.all(),slug_field='title')

    class Meta:
        model=DataPackage
        fields=(
            'url',
            'pk',
            'class_type',
            'researcher',
            'dataset'
        )
#    def create(self, validated_data):
#        return DataSet.objects.create(**validated_data)
#
#    def update(self,instance,validated_date):
#        instance.title=validated_date.get('title',instance.title)
#        instance.content=validated_date.get('content',instance.content)
#        instance.set=validated_date.get('set',instance.set)
#        instance.save()
#        return instance