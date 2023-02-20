from django.forms import ModelForm
from .models import Employee


class EmployeeForm(ModelForm):
    class Meta:
        model = Employee
        # especificamos los campos
        # fields = ['name', 'last_name', 'email']

        # especificamos todos los campos
        fields = '__all__'

        # si queremos otros campos usamos
        # extra_fields=['salary']

        # si queremos excluir algun campos usamos
        # exclude = ('email',)
