from django.db import models

class Doctor(models.Model):
    name = models.CharField(max_length=100)
    # Add any other fields as needed

    def __str__(self):
        return self.name

class Appointment(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    date = models.DateField()
    time = models.TimeField()
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    message = models.TextField(blank=True)

    def __str__(self):
        return f"{self.name} - {self.doctor.name} on {self.date}"
