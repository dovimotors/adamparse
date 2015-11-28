from django.shortcuts import render
from django.http import HttpResponse
from dbftopandas import AdamImport

# Create your views here.
def index(request):
    ai = AdamImport()
    inv = ai.convert('C:\\apps\\adamparse\INVEN.DBF')
    s = inv.head()
    s_trunk = s.to_html()
    return HttpResponse(s_trunk)