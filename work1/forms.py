from .models import FormBuilder
from django import forms
import datetime

class FormBuilderForm(forms.ModelForm):
    class Meta:
        model = FormBuilder
        fields = ("hash_id",)