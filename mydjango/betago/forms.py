from django import forms
from .models import chaiVarity

class ChaivarityFrom(forms.Form):
    chai_varity = forms.ModelChoiceField(queryset=chaiVarity.objects.all(), label="Select chai varity")