from django.db import models

# Create your models here.
class Therapist(models.Model):
    clinic_name = models.CharField(max_length=100)
    