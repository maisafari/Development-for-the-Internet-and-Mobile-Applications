from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from .models import Aluno

class UserRegistoForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2', 'email']

class AlunoForm(forms.ModelForm):
    class Meta:
        model = Aluno
        fields = ['curso' , 'grupo']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['curso'].required = True