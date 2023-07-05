from django.db import models

# Create your models here.
class Gpx(models.Model):
    start_location = models.CharField(max_length=500)
    end_location = models.CharField(max_length=500)
    transport_choices = (('walking', 'Walking'), ('bicycling', 'Cycling'))
    transport_method = models.CharField(max_length=9, choices=transport_choices, default='Walking')
    gpxfile = models.FileField(null=True, blank=True)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.start_location + ' -> ' + self.end_location