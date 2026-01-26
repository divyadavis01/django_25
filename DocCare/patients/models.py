from django.db import models

# Create your models here.
class Patient(models.Model):
    GENDER_CHOICES=(
        ("male","Male"),
        ("female","Female"),
        ("other","Other")
    )
    patient_code =models.CharField(max_length=20,unique=True)
    name=models.CharField(max_length=60)
    dob=models.DateField()
    gender=models.CharField(max_length=10,choices=GENDER_CHOICES)
    phone=models.CharField(max_length=14)
    address=models.TextField()
    created_at=models.DateField(auto_now_add=True)
    is_active=models.BooleanField(default=True)