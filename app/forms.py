from django import forms
from app.models import EmailDatabase

class UserForm(forms.ModelForm):
	password = forms.CharField(widget=forms.PasswordInput)
	class Meta:
	    model = EmailDatabase

