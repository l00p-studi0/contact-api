from django import forms
from .models import User
class UserForm(forms.ModelForm): 
    FirstName = forms.CharField(required=False , widget=forms.TextInput(attrs={'class': 'form-control'}))
    LastName = forms.CharField(required=False , widget=forms.TextInput(attrs={'class': 'form-control'}))
    Email = forms.CharField(label = "Email", required=False , widget=forms.TextInput(attrs={'class': 'form-control'}))
    Phone = forms.CharField(label = "Phone", required=False , widget=forms.TextInput(attrs={'class': 'form-control'}))
    Comment = forms.CharField(label = "Comment", required=False , widget=forms.Textarea(attrs={'class': 'form-control'}))
    class Meta:
        model = User
        fields =  ('FirstName','LastName','Email','Phone','Comment')