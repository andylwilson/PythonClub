from django.shortcuts import render
from .models import Meeting, Minutes, Resource, Event

# Create your views here.
def index(request):
    return render(request, 'clubapp/index.html')

def getResources(request):
    resource_list=Resource.objects.all()
    context={'resource_list' : resource_list}
    return render(request, 'clubapp/resources.html', context=context)