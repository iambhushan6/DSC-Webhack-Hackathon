from django.db import models

# Create your models here.

STATE = {
    ('Maharashtra','Maharashtra')
}

CITY = {
    ('Pune','Pune'),
    ('Mumbai','Mumbai'),
    ('Nagpur','Nagpur'),
}

TIMESLOT = {
    ('10am to 1am','10am to 1am'),
    ('2pm to 6pm','2pm to 6pm')
}

class Vac_center(models.Model):


    name = models.CharField(max_length=256)
    state = models.CharField(max_length=256,choices=STATE)
    city = models.CharField(max_length=256,choices=CITY)
    centerid = models.IntegerField()
    vaccines_av = models.IntegerField()
    update = models.CharField(max_length=256)

    def __str__(self):
        return self.name

class Citizen(models.Model):

    name = models.CharField(max_length=256)
    mobno = models.CharField(max_length=256)
    age = models.IntegerField()
    state = models.CharField(max_length=256, choices=STATE )
    city = models.CharField(max_length=256, choices=CITY)
    center = models.CharField(max_length=256)
    centername = models.ForeignKey('Vac_center',on_delete=models.CASCADE)
    date = models.DateField()
    timeslot = models.CharField(max_length=256, choices=TIMESLOT)

    def __str__(self):
        return self.name
