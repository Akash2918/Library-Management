from django import forms
from django.contrib.auth.models import User
from . import models

class AdminSigupForm(forms.ModelForm):
    class Meta:
        model=User
        fields=['first_name','last_name','username','password']



class StudentUserForm(forms.ModelForm):
    class Meta:
        model=User
        fields=['first_name','last_name','username','password']

class MemberForm(forms.ModelForm):
    class Meta:
        model=models.Member
        fields=['enrollment','branch']

class BookForm(forms.ModelForm):
    class Meta:
        model=models.Book
        fields=['name','isbn','author','category','no_of_copies_available']
class IssueForm(forms.Form):
    #to_field_name value will be stored when form is submitted.....__str__ method of book model will be shown there in html
    isbn2=forms.ModelChoiceField(queryset=models.Book.objects.all(),empty_label="Name of the book and author", to_field_name="isbn",label='Name of the book')
    enrollment2=forms.ModelChoiceField(queryset=models.Member.objects.all(),empty_label="Name of the student and enrollment",to_field_name='enrollment',label='Name of the student')
