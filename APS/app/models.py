from django.db import models

class Appointment(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    date_of_appointment = models.DateTimeField()
    phone_number = models.CharField(max_length=15)
    gender = models.CharField(max_length=10)
    message = models.CharField(max_length=1500)

    def __str__(self):
        return self.first_name + '_' + self.last_name + '_' + str(self.date_of_appointment)