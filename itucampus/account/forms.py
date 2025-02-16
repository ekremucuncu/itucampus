from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class RegisterForm(UserCreationForm):
    email = forms.EmailField()


    class Meta:
	       model = User
	       fields = ["username","email", "password1", "password2"]

    def save(self, commit=True):
        user = super(UserCreationForm, self).save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        user.username=user.username.lower()
        if commit:
            user.save()
        return user

    def clean_email(self):
        email = self.cleaned_data['email']
        if "@itu.edu.tr" not in email:
            raise forms.ValidationError("You must include @itu.edu.tr")
        return email
