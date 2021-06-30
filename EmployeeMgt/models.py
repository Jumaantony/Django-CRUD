from django.db import models
from django.utils import timezone
import uuid

# Create your models here.
class Employee(models.Model):
    ID = models.UUIDField(primary_key = True, default = uuid.uuid4,
         editable = True)
    Date_of_Employement = models.DateTimeField()
    Name = models.CharField(max_length=50)
    Email = models.EmailField()
    Phone_Number = models.IntegerField()
    Job = models.CharField(max_length=50)
