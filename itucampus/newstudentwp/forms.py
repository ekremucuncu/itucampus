from django import forms
from .models import WPGroup


class WPGroupForm(forms.ModelForm):
    class Meta:
        model=WPGroup
        fields=['name','number','bolum','mail']


    def clean_mail(self):
        email = self.cleaned_data['mail']
        if "@itu.edu.tr" not in email:
            raise forms.ValidationError("You must include @itu.edu.tr")
        return email
