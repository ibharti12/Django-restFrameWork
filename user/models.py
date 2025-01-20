from django.db import models

# Create your models here.
from django.db import models  
class User(models.Model):  
    first_name = models.CharField(max_length=100)  
    last_name = models.CharField(max_length=100)  
    email = models.EmailField(unique=True)  
    contact = models.CharField(max_length=15)  
    address=models.CharField(max_length=20)
    class Meta:  
        db_table = "user"