from django import forms
from .models import Contact
from django.contrib.auth.forms import UserCreationForm



# class ContactForm(forms.Form):
#     name = forms.CharField(widget=forms.TextInput(
#         attrs={'placeholder': 'Name',
#                'class':'form-control'}))
#
#     email = forms.EmailField(widget=forms.EmailInput(
#         attrs={'placeholder': 'Email',
#                'class':'form-control'}))
#
#     subject = forms.CharField(widget=forms.Textarea(
#         attrs={'placeholder': 'Subject',
#                'class':'form-control'}))
#
#     message = forms.CharField(widget=forms.Textarea(
#         attrs={'placeholder': 'Message',
#                'class':'form-control'}))



class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ('name', 'email', 'subject', 'message')
        widgets = {
            'name': forms.TextInput(
                attrs={'placeholder': 'Name','class': 'form-control'}),
            'email': forms.EmailInput(
                attrs={'placeholder': 'Email', 'class': 'form-control'
                }),
            'subject': forms.TextInput(
                attrs={
                    'placeholder': 'Subject',
                    'class': 'form-control'
                    }
                ),
            'message': forms.Textarea(
                attrs={
                    'placeholder': 'Message',
                    'class': 'form-control'
                    }
                ),
        }