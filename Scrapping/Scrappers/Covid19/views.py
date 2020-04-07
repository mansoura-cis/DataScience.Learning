from django.shortcuts import render
from django.http import HttpResponse
from Covid19.Scrapper import Covid19Extractor

def index(request):
    return render(request , 'Home.html' , {'name' : 'Ahmed'})

