from django import forms
from .models import user_details
from django.forms import DateInput
class userform(forms.ModelForm):
    class Meta:
        model = user_details
        fields = '__all__'
        widgets = {
            'date_time_field': DateInput(attrs={'type': 'date'})
        }
        