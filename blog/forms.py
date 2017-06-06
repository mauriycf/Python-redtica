from django.contrib.auth.models import User
from django import forms

class UserForm(forms.ModelForm):
	password = forms.CharField(widget=forms.PasswordInput)

	class Meta:
		model = User
		fields = ['username','email','password']
	

class PerfilForm(forms.ModelForm):
	age = forms.CharField()
	cellphone = forms.CharField()
	address = forms.CharField()
	job_info = forms.CharField()
	education = forms.CharField()
	biography = forms.CharField()
	social_network = forms.CharField()

	class Meta:
		model = User
		fields = ['age','cellphone','address','job_info','education','biography','social_network']
