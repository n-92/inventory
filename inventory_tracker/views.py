from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
    return HttpResponse('<p> In Index View</p>')

def item_detail(request, id):
    return HttpResponse('<p> In item_detail view with id {0}'.format(id))