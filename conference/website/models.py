from django.db import models
from datetime import datetime

# Create your models here.

class BannerImage(models.Model):
    image = models.ImageField(null=True, blank=True)


class Counter(models.Model):
    date = models.DateField(default=datetime.now, blank = True)
    time = models.TimeField(default=datetime.now, blank = True)


class Join(models.Model):
    name = models.CharField(max_length=100, null=True, blank=True)
    email = models.CharField(max_length=100, null=True, blank=True)
    phone = models.CharField(max_length=100, null=True, blank=True)
    
    def __str__(self):
        return self.name


class DetailOfConferernce(models.Model):
    icon =  models.CharField(max_length=100, null=True, blank=True)
    heading =  models.CharField(max_length=100, null=True, blank=True)
    description = models.TextField(default='describe here')

    def __str__(self):
        return self.heading


class SideImage(models.Model):
    image = models.ImageField(null=True, blank=True)


class ConferenceDay(models.Model):
    day = models.CharField(max_length=100, null=True, blank=True)
    date = models.DateField(default=datetime.now, blank = True)

    def __str__(self):
        return self.day


class ConferenceSchedule(models.Model):
    heading = models.CharField(max_length=100, null=True, blank=True)
    about = models.TextField(default='describe hehe')
    description = models.TextField(default='describe hehe')
    image =  models.ImageField(null=True, blank=True)
    start_time = models.TimeField(default=datetime.now, blank = True)
    end_time = models.TimeField(default=datetime.now, blank = True)
    date = models.DateField(default=datetime.now, blank = True)
    location = models.CharField(max_length=100, null=True, blank=True)
    posted_by = models.CharField(max_length=100, null=True, blank=True)
    position = models.CharField(max_length=100, null=True, blank=True)
    conference_day = models.ForeignKey(ConferenceDay, on_delete=models.CASCADE, related_name='conference_day', null =True, blank=True)

    def __str__(self):
        return self.heading


class Gallery(models.Model):
    image = models.ImageField(null=True, blank=True)


class HappyClients(models.Model):
    image = models.ImageField(null=True, blank=True)
    name = models.CharField(max_length=100, null=True, blank=True)
    details = models.TextField(default='here')
    position = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return  self.name

class Active(models.Model):
    name = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return  self.name


class Pricing(models.Model):
    types = models.CharField(max_length=100, null=True, blank=True)
    price = models.IntegerField()
    about = models.CharField(max_length=100, null=True, blank=True)
    features = models.TextField(default='here')
    active = models.ForeignKey(Active, on_delete=models.CASCADE, related_name='active', null =True, blank=True)

    def __str__(self):
        return self.types


class AboutCounter(models.Model):
    speaker = models.IntegerField()
    sponsor = models.IntegerField()
    total_seats = models.IntegerField()
    topic = models.IntegerField()




class Speakers(models.Model):
    name = models.CharField(max_length=100, null=True, blank=True)
    profession = models.CharField(max_length=100, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)
    description = models.TextField(default='here')

    def __str__(self):
        return self.name


class BlogSingle(models.Model):
    image = models.ImageField(null=True, blank=True)
    heading = models.CharField(max_length=100, null=True, blank=True)
    description = models.TextField(default='here')
    date = models.DateField(default=datetime.now, blank = True)
    posted_by = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return self.heading


class Comment(models.Model):
    name = models.CharField(max_length=100, null=True, blank=True)
    email = models.CharField(max_length=100, null=True, blank=True)
    message = models.TextField(default='here')
    date = models.DateField(default=datetime.now, blank=True)
    time =  models.TimeField(default=datetime.now, blank =True)

    def __str__(self):
        return self.name

class Contact(models.Model):
    name = models.CharField(max_length=100, null=True, blank=True)
    email = models.CharField(max_length=100, null=True, blank=True)
    subject = models.CharField(max_length=100, null=True, blank=True)
    message = models.TextField(default='here')

    def __str__(self):
        return self.name
