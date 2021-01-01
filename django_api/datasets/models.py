from django.db import models

class DataCat(models.Model):
    kind=models.CharField(max_length=200, unique=True)

    class Meta:
        ordering=('kind',)

    def __str__(self):
        return self.kind

    objects=models.Manager()

class DataSet(models.Model):
    title=models.CharField(max_length=50)
    content=models.CharField(max_length=100)
    set=models.IntegerField(default=100)
    category=models.ForeignKey(DataCat,related_name='datasets',on_delete=models.CASCADE)
    inserted=models.DateTimeField(auto_now_add=True)

    #authentication
    owner=models.ForeignKey(
        'auth.User',
        related_name='datasets',
        on_delete=models.CASCADE
    )

    objects=models.Manager()

    class Meta:
        ordering=('title',)

class Researcher(models.Model):
    EUROPEAN='EU'
    NOTEU='noEU'
    CHOICES=(
        (EUROPEAN,'European'),
        (NOTEU,'Noteu'),
    )
    name=models.CharField(max_length=100)
    origin=models.CharField(max_length=4,choices=CHOICES,default=EUROPEAN)
    inserted=models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering=('name',)
    def __str__(self):
        return self.name

    objects = models.Manager()

class DataPackage(models.Model):
    researcher=models.ForeignKey(
        Researcher, related_name='datapackage',
        on_delete=models.CASCADE
    )
    dataset=models.ForeignKey(DataSet, on_delete=models.CASCADE)
    class_type=models.IntegerField()

    class Meta:
        ordering=('class_type',)

    objects = models.Manager()