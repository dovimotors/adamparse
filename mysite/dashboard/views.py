from django.shortcuts import render, HttpResponse
from .models import PartsInv
import pandas as pd
# Create your views here.


def index(request):
    parts = PartsInv.objects.all()
    context = {'value_list': parts}
    return render(request, 'dashboard/index.html', context)


