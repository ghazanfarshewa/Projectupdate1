from django.db import models

class Member(models.Model):
  tasks = models.CharField(max_length=255)
  date = models.DateField(max_length=255)


  