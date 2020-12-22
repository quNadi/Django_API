from django.http import HttpResponse
from .models import DataSet

def index(request,pid):
    dataset=DataSet.objects.get(id=pid)
    return HttpResponse(
        content={
            'id':dataset.id,
            'title': dataset.title,
            'content': dataset.content,
            'set':dataset.set,
        }
    )
