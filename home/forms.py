from django import forms
from .models import *
from django.contrib.auth.forms import UserCreationForm
# Create your forms here.

class ContactForm(forms.ModelForm):
	class Meta:
		model = Contact
		exclude = ()
		feilds = ['subject', 'name', 'email', 'message']
		
	subject = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control' }))

	name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control' }))
	email = forms.EmailField(widget=forms.EmailInput(attrs={'class':'form-control' }))
	message = forms.CharField(widget = forms.Textarea(attrs={'class':'form-control' }))
class CustomerForm(forms.ModelForm):
	class Meta:
		model = Customer
        
		exclude = ('user',)
		feilds = ['name', 'last','email','phone']
		name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control' }))
		last = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control' }))
		email = forms.EmailField(widget=forms.EmailInput(attrs={'class':'form-control' }))
		phone = forms.CharField(widget = forms.Textarea(attrs={'class':'form-control' }))
class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']