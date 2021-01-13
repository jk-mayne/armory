from django.shortcuts import render
from django.http import HttpResponse
from armory2.armory_main.models import *
from django.shortcuts import render, get_object_or_404
from django.template.defaulttags import register
from django.template import loader
from django.views.decorators.csrf import csrf_exempt

# from armory2.


def index(request):

   # basedomains = BaseDomain.objects.all().order_by('name')
    #p.meta.get('Gowitness')
    #p.meta.get('Gowitness')
    #print(meta)


    #data[p.id].append('Gowitness')

    return render(request, 'gowitnessPage/index.html')

def get_gowitness(request, port_id):

    port = Port.objects.get(id=port_id)

    return render(request, 'host_summary/gowitness.html', {'port':port})