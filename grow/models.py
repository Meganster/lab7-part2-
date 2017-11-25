from django.db import models


# Create your models here.

class Department(models.Model):
    name = models.CharField(max_length=30)
    about = models.TextField()

    def __unicode__(self):
        return self.name

class Employee(models.Model):
    firstName = models.CharField(max_length=30)
    lastName = models.CharField(max_length=30)
    about = models.TextField()
    email = models.EmailField()
    phone_number = models.CharField(max_length=50)
    department = models.ForeignKey("Department")
