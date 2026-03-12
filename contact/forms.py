from django.core.exceptions import ValidationError
from django.shortcuts import render, get_object_or_404, redirect
from django import forms
from . import models

class ContactForm(forms.ModelForm):
    picture = forms.ImageField(
        widget=forms.FileInput(
            attrs={
                'accept': 'image/*',
            }
        )
    )

    class Meta:
        model = models.Contact
        fields = (
            'first_name', 'last_name', 'phone',
            'email', 'description', 'category', 
            'picture',
        )
    def clean(self):
        cleaned_data = self.cleaned_data 
        first_name = cleaned_data.get('first_name')

        if first_name == 'ABC':
            self.add_error(
                'first_name',
                ValidationError(
                    'ERRADO',
                    code='invalid'
                    )
            )

        return super().clean()

    def clean_first_name(self):
        first_name = self.cleaned_data.get('first_name')

        if first_name == 'ABC':
            self.add_error(
                'first_name',
                ValidationError(
                    'add_error',
                    code='Invalid_name',
                )
            )

        return first_name
