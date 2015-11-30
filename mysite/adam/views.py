from django.shortcuts import render
from django.http import HttpResponse
from dbftopandas import AdamImport
from .models import ADAMFiles

# Create your views here.
def index(request):
    path_list = ADAMFiles.objects.all()
    context = {'path_list': path_list}
    return render(request, 'adam/index.html', context)

def detail(request, path_id):
    ai = AdamImport()
    p = ADAMFiles.objects.get(id=path_id)
    p = str(p)
    inv = ai.convert(p)
    s = inv.head()
    s_trunk = s.to_html()
    return HttpResponse(s_trunk)