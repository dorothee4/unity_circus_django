from django.db import models

# Create your models here.

class Donation(models.Model):
    First_name=models.CharField(null=False,max_length=20)
    Last_name=models.CharField(null=False,max_length=20)
    Email=models.EmailField(null=False)
    Message=models.TextField(null=False)

    def __str__(self):
        return self.First_name
