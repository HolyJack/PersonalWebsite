from django import forms

class ContactForm(forms.Form):
    full_name = forms.CharField(label='Name', max_length=100, widget=forms.TextInput(attrs={'class': 'input-field', 'placeholder': 'Full Name'}))
    email = forms.EmailField(label='Email', widget=forms.EmailInput(attrs={'class': 'input-field', 'placeholder': 'Example@hmail.com'}))
    message = forms.CharField(label='Message', widget=forms.Textarea(attrs={'class': 'textarea-field', 'placeholder': 'Write Message'}))