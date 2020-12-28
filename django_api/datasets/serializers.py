from rest_framework import serializers

from .models import DataSet, DataCat, DataPackage, Researcher

from django.contrib.auth.models import User

class UserDataSerial(serializers.HyperlinkedModelSerializer):
    class Meta:
        model=DataSet
        fields=(
            'url',
            'title'
        )

class UserSerial(serializers.HyperlinkedModelSerializer):
    datasets=UserDataSerial( many=True, read_only=True)
    class Meta:
        model=User
        fields=(
            'url',
            'pk',
            'username',
            'datasets'
        )

class DataCatSerializer(serializers.HyperlinkedModelSerializer):
    datasets=serializers.HyperlinkedRelatedField(
        many=True,
        read_only=True,
        view_name='dataset-detail')
    class Meta:
        model=DataCat
        fields=(
            'url',
            'pk',
            'kind',
            'datasets'
        )



class DataSerializers(serializers.ModelSerializer):
    category=serializers.SlugRelatedField(queryset=DataCat.objects.all(),slug_field='kind')
    #user auth
    owner=serializers.ReadOnlyField(source='owner.username')
    class Meta:
        model=DataSet
        fields=('url',
                'title',
                'owner',
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
            'class_type' ,
            'dataset'
        )


class ResearcherSerial(serializers.HyperlinkedModelSerializer):
    datapack = DataPackageSerial(many=True,read_only=True)
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