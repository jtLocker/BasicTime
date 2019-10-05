from django.db import models
from  django.utils.timezone import now

# Create your models here.

class Visit(models.Model):
    image = models.ImageField(upload_to='images/')
    # char = models.CharField(max_length = 16)
    # time =  models.DateTimeField(auto_now_add=True)