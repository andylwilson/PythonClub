from django.urls import path
from . import views

# project url directs to this, which directs to the proper view
urlpatterns=[
    path('', views.index, name='index'),
    path('getResources/', views.getResources, name='resources'),
    path('getMeetings/', views.getMeetings, name='meetings'),
    path('meetingDetail/<int:id>', views.meetingDetail, name='meetingdetail'),
    path('newmeeting/', views.newmeeting, name='newmeeting'),
    path('newminutes/', views.newminutes, name='newminutes'),
    path('newresource/', views.newresource, name='newresource'),
    path('newevent/', views.newevent, name='newevent'),

]