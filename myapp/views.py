from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

# Create your views here.

def index(request):
    template = loader.get_template("index.html.twig")
    data = {"materielsinfo" : ["imprimante", "Laptop", "Ipad", "Ipod"], "age" : 12}
    return HttpResponse(template.render(data))