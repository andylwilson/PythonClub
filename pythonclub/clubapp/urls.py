from django.urls import path
from . import views

# project url directs to this, which directs to the proper view
urlpatterns=[
    path('', views.index, name='index'),
    path('getResources/', views.getResources, name='resources'),
    path('getMeetings/', views.getMeetings, name='meetings'),
    path('meetingDetail/<int:id>', views.meetingDetail, name='meetingdetail'),

]