from django.db import models
from departments.models import Department

# Create your models here.
class Doctor(models.Model):
    GENDER_CHOICES=(
        ("male","Male"),
        ("female","Female"),
        ("other","Other")
    )
    name=models.CharField(max_length=50)
    department=models.ForeignKey(Department,on_delete=models.PROTECT)
    dob=models.DateField()
    gender=models.CharField(max_length=10,choices=GENDER_CHOICES)
    join_date=models.DateField()
    salary=models.DecimalField(max_digits=10,decimal_places=2)
    qualification=models.CharField(max_length=70)
    about=models.TextField()
    image=models.ImageField(upload_to="doctors",default="doctors/doctor_default.jpg")

    def __str__(self):
        return f"{self.name} - {self.id}"
