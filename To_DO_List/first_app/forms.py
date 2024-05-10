from django import forms
from first_app.models import TaskModel

class TaskMoelForm(forms.ModelForm):
    class Meta:
        model = TaskModel
        fields = ['taskTittle','task_description']