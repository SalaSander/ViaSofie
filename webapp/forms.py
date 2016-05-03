from django import forms
from django.forms import ModelForm
from django.contrib import admin
from webapp.models import *


class Stad(forms.ModelForm):
	class Meta:
		model = Stad
		fields = ['postcode', 'stadsnaam',]

class RegistrationForm(forms.ModelForm):
    """
    Form for registering a new account.
    """
    email = forms.EmailField(label="*E-mail", widget=forms.EmailInput(attrs={'placeholder': 'E-mail'}))
    password1 = forms.CharField(label="*Wachtwoord", widget=forms.PasswordInput(attrs={'placeholder': 'Wachtwoord'}))
    password2 = forms.CharField(label="*Wachtwoord (nogmaals)", widget=forms.PasswordInput(attrs={'placeholder': 'Wachtwoord'}))
    voornaam = forms.CharField(label="*Voornaam", widget=forms.TextInput(attrs={'placeholder': 'Voornaam'}))
    naam = forms.CharField(label="*Naam", widget=forms.TextInput(attrs={'placeholder': 'Naam'}))
    straatnaam = forms.CharField(label="*Straatnaam", widget=forms.TextInput(attrs={'placeholder': 'Straatnaam'}))
    huisnr = forms.CharField(label="*Huisnummer", widget=forms.NumberInput(attrs={'placeholder': 'Bijv: 1'}))
    busnr = forms.CharField(required=False, label="Busnummer", widget=forms.NumberInput(attrs={'placeholder': 'Bijv: 1'}))
    telefoonnr = forms.CharField(label="*Telefoonnummer", widget=forms.TextInput(attrs={'placeholder': 'Telefoonnr'}))

    class Meta:
        model = User
        fields = ['email', 'password1', 'password2', 'voornaam', 'naam', 'straatnaam', 'huisnr', 'postcode', 'busnr', 'telefoonnr', ]

    def clean(self):
        """
        Verifies that the values entered into the password fields match

        NOTE: Errors here will appear in ``non_field_errors()`` because it applies to more than one field.
        """
        cleaned_data = super(RegistrationForm, self).clean()
        if 'password1' in self.cleaned_data and 'password2' in self.cleaned_data:
            if self.cleaned_data['password1'] != self.cleaned_data['password2']:
                raise forms.ValidationError("Passwords don't match. Please enter both fields again.")
        return self.cleaned_data

    def save(self, commit=True):
        user = super(RegistrationForm, self).save(commit=False)
        user.set_password(self.cleaned_data['password1'])
        if commit:
            user.save()
        return user

class AuthenticationForm(forms.Form):
    """
    Login form
    """
    email = forms.EmailField(widget=forms.TextInput(attrs={'placeholder': 'Email'}))
    password = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Wachtwoord'}))

    class Meta:
        fields = ['email', 'password']

class FotoForm(forms.Form):

	# class Meta:
	# 	model: Foto
	# 	fields['docfile']
	docfile = forms.FileField(
		label='Select a file'
	)

class Ebookform(forms.ModelForm):
	class Meta:
		model = Ebook
		fields = ['naam', 'voornaam', 'email',]

class PandType(forms.ModelForm):
	class Meta:
		model = PandType
		fields = ['pandtype',]

class Handelstatus(forms.ModelForm):
	class Meta:
		model = Handelstatus
		fields = ['status',]

class Voortgang(forms.ModelForm):
	class Meta:
		model = Voortgang
		fields = ['status',]

class Pand(forms.ModelForm):
	class Meta:
		model = Pand
		fields = ['user', 'straatnaam', 'huisnr', 'postcodeID', 'pandtype', 'handelstatus', 'voortgang',]

class Tag(forms.ModelForm):
	class Meta:
		model = Tag
		fields = ['tagnaam', 'pand',]

class Log(forms.ModelForm):
	class Meta:
		model = Log
		fields = ['user', 'logText',]
		exclude = ['created',]

class Foto(forms.ModelForm):
	class Meta:
		model = Foto
		fields = ['url', 'pand']