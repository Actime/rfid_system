from registration.forms import RegistrationFormUniqueEmail
from django import forms

class UserProfileRegistrationForm(RegistrationFormUniqueEmail):
    field = forms.CharField()