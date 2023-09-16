from django import forms
from .models import TaskList

class TaskListForm(forms.ModelForm):
    class Meta:
        model = TaskList
        fields = ['title', 'description', 'completed']
