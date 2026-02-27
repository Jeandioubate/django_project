
from django import forms
from .models import Question


class QuestionForm(forms.ModelForm):

    choice1 = forms.CharField(required=False, label="Choix 1")
    choice2 = forms.CharField(required=False, label="Choix 2")
    choice3 = forms.CharField(required=False, label="Choix 3")
    choice4 = forms.CharField(required=False, label="Choix 4")
    choice5 = forms.CharField(required=False, label="Choix 5")

    class Meta:
        model = Question
        fields = ['question_text', 'pub_date']