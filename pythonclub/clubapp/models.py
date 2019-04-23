from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Meeting(models.Model):
    meetingtitle=models.CharField(max_length=255)
    meetingdate=models.DateField()
    meetingtime=models.TimeField()
    location=models.CharField(max_length=255)
    agenda=models.TextField()

    def __str__(self):
        return self.meetingtitle

    class Meta:
        db_table='meeting'
        verbose_name_plural='meetings'

class Minutes(models.Model):
    meetingid=models.ForeignKey(Meeting, on_delete=models.DO_NOTHING)
    attendance=models.ManyToManyField(User)
    minutes=models.TextField()

    def __str__(self):
        return self.minutes

    class Meta:
        db_table='minutes'
        verbose_name_plural='minutes'

class Resource(models.Model):
    resourcename=models.CharField(max_length=255)
    resourcetype=models.CharField(max_length=255)
    resourceURL=models.URLField(null=True, blank=True)
    dateentered=models.DateField()
    userid=models.ForeignKey(User, on_delete=models.DO_NOTHING)
    description=models.TextField()

    def __str__(self):
        return self.resourcename

    class Meta:
        db_table='resource'
        verbose_name_plural='resources'

class Event(models.Model):
    eventtitle=models.CharField(max_length=255)
    location=models.CharField(max_length=255)
    date=models.DateField()
    time=models.TimeField()
    description=models.TextField()
    userid=models.ForeignKey(User, on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.eventtitle

    class Meta:
        db_table='event'
        verbose_name_plural='events'