from django import forms
from .models import User_Attributes
class UserAttributeForm(forms.ModelForm):
    class Meta:
        model =User_Attributes
        fields=['age', 'gender', 'pneumonia',
                             'breathing',
            'pregnant',
            'smoker',
             'diabetic',
            'heart',
            'asthma',
            'blood',
            'obesity',
            'others']
class HospitalForm(forms.Form):
    hospital = forms.IntegerField()