from django.db import models

class Student(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    college_name = models.CharField(max_length=100)
    department = models.CharField(max_length=100)
    pursuing_year = models.IntegerField()
    mail_id = models.EmailField()
    phone_number = models.CharField(max_length=20)
