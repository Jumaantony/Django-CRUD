from django.db import models
import uuid
from phonenumber_field.modelfields import PhoneNumberField


# Create your models here.
class Employee(models.Model):
    ID = models.UUIDField(primary_key=True,
                          default=uuid.uuid4,
                          editable=True)
    Date_of_Employement = models.DateTimeField()
    Name = models.CharField(max_length=50)
    Email = models.EmailField()
    Phone_Number = PhoneNumberField()
    Job = models.ForeignKey('Job', on_delete=models.CASCADE)

    def __str__(self):
        return self.Name


class Job(models.Model):
    id = models.UUIDField(primary_key=True,
                          default=uuid.uuid4,
                          editable=True)
    name = models.CharField(max_length=50)
    date = models.DateTimeField()

    def __str__(self):
        return self.name