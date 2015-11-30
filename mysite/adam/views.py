from django.shortcuts import render
from django.http import HttpResponse
from dbftopandas import AdamImport
from .models import ADAMFiles

# Create your views here.
def index(request):
    #main view for /adam/ app.  returns all paths in the database with links
    path_list = ADAMFiles.objects.all()
    context = {'path_list': path_list}
    return render(request, 'adam/index.html', context)

def detail(request, path_id):
    #view for the adam/<id> page returns an html rendered dataframe
    #create the object to convert DBF to pandas
    ai = AdamImport()
    #get the id from the path and pull the correspoding DBF
    p = ADAMFiles.objects.get(id=path_id)
    p = str(p)
    #conver the DBF to a dataframe
    datafr = ai.convert(p)

    #*******************
    # modify the dataframe here before converting to HTML
    #*******************

    s = datafr.head()

    #*******************
    #*******************
    s_trunk = s.to_html()
    return HttpResponse(s_trunk)