from django.forms import ModelForm
from .models import Todo


class TodoForm(ModelForm):
    class Meta:
        form = Todo
        fields = '__all__'
