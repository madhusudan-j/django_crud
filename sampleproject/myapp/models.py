from django.db import models

class EmployeeDetails(models.Model):
    firstname = models.CharField(max_length = 30)
    secondname = models.CharField(max_length = 30)
    email = models.EmailField()
    password = models.CharField(max_length = 30)
    address = models.CharField(max_length = 100)

    def __str__(self):
        return self.email

