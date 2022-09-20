
from email.mime import image
from email.policy import default
from django.db import models

# Create your models here.

class Metro(models.Model): 
    id  = models.IntegerField(primary_key=True)
    Name = models.CharField(max_length=150)
    LineId = models.IntegerField()
    LineName = models.CharField(max_length=10)
    Description = models.CharField(max_length=120)
    Order = models.IntegerField()
    IsActive = models.BooleanField(default=True)
    BabyRoom =  models.BooleanField(default=True)
    WC = models.BooleanField(default=True)
    Masjid = models.BooleanField(default=True)
    Longitude = models.CharField(max_length=120 )
    Latitude = models.CharField(max_length=120)
    image = models.ImageField(upload_to="img/%Y/%m/%d/" ,default="./static/img/Istanbul_Metro_Logo.svg.png")

    class Meta:  
        db_table = "Metro" 
        

    def __str__(self):
        return self.Description



