from django import forms
from .models import FeedBack

class FeedBack(forms.ModelForm):
    class Meta:
        model = FeedBack
        fields = ('name', 'phone', 'email')
