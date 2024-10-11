from django.shortcuts import render
from django.http import HttpResponse

import os
# Create your views here.



def index(request):
    return render(request, 'core/index.html')

def about_us(request):
    return render(request, "core/about_us.html")

