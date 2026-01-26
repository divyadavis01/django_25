from django.db.models.signals import pre_save
from django.dispatch import receiver
from patients.models import Patient
from django.core.exceptions import ObjectDoesNotExist
@receiver(signal=pre_save,sender=Patient)
def before_patient_save(instance,*args,**kwargs):
    try:
        latest_patient=Patient.objects.latest("id")
        new_patient_id=latest_patient.id+1
    except ObjectDoesNotExist:
        new_patient_id=1

        
    code=f"HSP-{new_patient_id}"
    print(code)
    if not instance.patient_code:
        instance.patient_code=code
        