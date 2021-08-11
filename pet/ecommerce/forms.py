from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class User_creation_form(UserCreationForm):
    class Meta:
        model = User
        fields = ['email', 'password1', 'password2']
