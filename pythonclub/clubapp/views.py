from django.shortcuts import render, get_object_or_404
from .models import Meeting, Minutes, Resource, Event

# Create your views here.
def index(request):
    return render(request, 'clubapp/index.html')

def getResources(request):
    resource_list=Resource.objects.all()
    context={'resource_list' : resource_list}
    return render(request, 'clubapp/resources.html', context=context)

def getMeetings(request):
    meeting_list=Meeting.objects.all()
    return render(request,'clubapp/meetings.html',{'meeting_list' : meeting_list})

def meetingDetail(request, id):
    meet=get_object_or_404(Meeting, pk=id)
    context={'meet' : meet,}
    return render(request, 'clubapp/meetingdetail.html', context=context)