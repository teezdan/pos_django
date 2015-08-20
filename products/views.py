from django.shortcuts import render
from django.http import  HttpResponse
import json
from .models import Category, Product
from django.core import serializers
# Create your views here.


def categories(request):
    cats = Category.objects.all().values('id', 'name')
    data = list(cats)
    return HttpResponse(json.dumps(data), content_type="application/json")


def items(request):
    cats = Product.objects.all().values('id', 'name', 'desc', 'category')
    data = list(cats)
    return HttpResponse(json.dumps(data), content_type="application/json")