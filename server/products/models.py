from datetime import datetime
from email.policy import default
from django.db import models
# Create your models here.



class Product (models.Model):
    name = models.CharField( max_length=50, blank=False)
    price = models.DecimalField( max_digits=5, decimal_places=2, null=False, blank=False)
    created_at = models.DateTimeField( default=datetime.now())
    image = models.ImageField(upload_to='uploads/images', height_field=None, width_field=None, max_length=None)
    description = models.TextField()
    category = models.CharField(blank=True, max_length=50, null=True)
    def __str__(self):
        return self.name
        
