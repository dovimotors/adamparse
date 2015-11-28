from django.shortcuts import render
from django.http import HttpResponse
from dbftopandas import AdamImport

# Create your views here.
def index(request):
    ai = AdamImport()
    inv = ai.convert('C:\\adamparse\INVEN.DBF')
    s = inv.head()
    return HttpResponse(s)