from django.shortcuts import render
from django.http import HttpResponse
from Covid19.Scrapper import getDataTable




def index(request):
    return HttpResponse( getDataTable().prettify() )

