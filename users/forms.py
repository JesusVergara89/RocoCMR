from django import forms
from django.contrib.auth.models import User
from .models import Profile
from django.contrib.auth.forms import UserCreationForm

class CustomUserCreationForm(UserCreationForm):
    phone = forms.CharField(max_length=15, required=False)
    name = forms.CharField(max_length=30, required=False)
    email = forms.EmailField(required=True)
    address = forms.CharField(max_length=100, required=False)

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2', 'phone', 'name', 'address')   

    def save(self, commit=True):
        user = super().save(commit)
        profile = Profile(user=user)
        profile.phone = self.cleaned_data.get('phone')
        profile.name = self.cleaned_data.get('name')
        profile.address = self.cleaned_data.get('address')
        if commit:
            user.save()
            profile.save()
        return user
