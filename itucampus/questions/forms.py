from .models import Question,Answer
from django import forms

class QuestionForm(forms.ModelForm):
    class Meta:
        model=Question
        fields=['question','author','title','body']

class AnswerForm(forms.ModelForm):
    class Meta:
        model=Answer
        fields=['answer','body']
