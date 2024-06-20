from django import forms
from task.models import Task

CHOICES = (
    ('1', 'Yes'),
    ('0', 'No'),
)

class TaskForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        instance = kwargs.get('instance')
        if instance:
            self.fields['is_completed'].initial = instance.is_completed

    class Meta:
        model = Task
        fields = "__all__"
        widgets = {
            'category': forms.SelectMultiple(attrs={'class': 'select2'}),
            'is_completed': forms.Select(choices=CHOICES, attrs={'class': 'select2'}),
            'task_assign_date': forms.DateInput(attrs={'type': 'date'}),
        }
