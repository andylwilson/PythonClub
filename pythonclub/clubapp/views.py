from django.shortcuts import render, get_object_or_404
from .models import Meeting, Minutes, Resource, Event
from .forms import MeetingForm, MinutesForm, ResourceForm, EventForm
from django.contrib.auth.decorators import login_required

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

@login_required
def newmeeting(request):
     form=MeetingForm
     if request.method=='POST':
          form=MeetingForm(request.POST)
          if form.is_valid():
               post=form.save(commit=True)
               post.save()
               form=MeetingForm()
     else:
          form=MeetingForm()
     return render(request, 'clubapp/newmeeting.html', {'form': form})

@login_required
def newminutes(request):
     form=MinutesForm
     if request.method=='POST':
          form=MinutesForm(request.POST)
          if form.is_valid():
               post=form.save(commit=True)
               post.save()
               form=MinutesForm()
     else:
          form=MinutesForm()
     return render(request, 'clubapp/newminutes.html', {'form': form})

@login_required
def newresource(request):
     form=ResourceForm
     if request.method=='POST':
          form=ResourceForm(request.POST)
          if form.is_valid():
               post=form.save(commit=True)
               post.save()
               form=ResourceForm()
     else:
          form=ResourceForm()
     return render(request, 'clubapp/newresource.html', {'form': form})

@login_required
def newevent(request):
     form=EventForm
     if request.method=='POST':
          form=EventForm(request.POST)
          if form.is_valid():
               post=form.save(commit=True)
               post.save()
               form=EventForm()
     else:
          form=EventForm()
     return render(request, 'clubapp/newevent.html', {'form': form})

def loginMessage(request):
     return render(request,'clubapp/loginmessage.html')

def logoutMessage(request):
     return render(request, 'clubapp/logoutmessage.html')