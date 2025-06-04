from django.apps import AppConfig
from django.db.utils import OperationalError

class PamsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'pams'

    def ready(self):
        from .models import Patient
        try:
            if Patient.objects.count() == 0:
                Patient.objects.bulk_create([
                    Patient(full_name='Karuna', age=22, gender='F', insurance_provider='HealthCare Inc', policy_number='HC12345'),
                    Patient(full_name='Pranay', age=25, gender='M', insurance_provider='MediPlus', policy_number='MP98765'),
                    Patient(full_name='Pavi', age=20, gender='F', insurance_provider='LifeSecure', policy_number='LS45678'),
                    Patient(full_name='Satvika', age=18, gender='F', insurance_provider='HealthCare Inc', policy_number='HC67890'),
                    Patient(full_name='Prashanth', age=20, gender='M', insurance_provider='MediPlus', policy_number='MP23456'),
                ])
        except OperationalError:
            # This will occur if migrations have not run yet
            pass
