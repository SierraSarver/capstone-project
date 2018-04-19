from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User

class RegisterUserForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required = False, help_text='*')
    last_name = forms.CharField(max_length=30, required = False, help_text='*')
    email = forms.EmailField(max_length = 214, required = False, help_text = '*')

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2']

    def __init__(self, *args, **kwargs):
        super(RegisterUserForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update({
            'id': 'userName',
            'placeholder': 'username',
            'style': 'color:black'})
        self.fields['first_name'].widget.attrs.update({
            'id': 'first_name',
            'placeholder': 'first name',
            'style': 'color:black'})
        self.fields['last_name'].widget.attrs.update({
            'id': 'last_name',
            'placeholder': 'last name',
            'style': 'color:black'})
        self.fields['email'].widget.attrs.update({
            'id': 'email',
            'placeholder': 'email',
            'style': 'color:black'})
        self.fields['password1'].widget.attrs.update({
            'id': 'password',
            'placeholder': 'password',
            'style': 'color:black'})
        self.fields['password2'].widget.attrs.update({
            'id': 'repeat password',
            'placeholder': 'repeat password',
            'style': 'color:black'})

    #password password_validation
    def clean_password(self):
        cd = self.cleaned_data
        if cd['password2']  != cd['password']:
            raise ValidationError("passwords don't match")
        return cd['password']

class SignUpForm(AuthenticationForm):

    class Meta:
        model = User
        fields = ['username', 'password']

    def __init__(self, *args, **kwargs):
        super(SignUpForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update({
            'id': 'userName',
            'placeholder': 'username',
            'style': 'color:black'})
        self.fields['password'].widget.attrs.update({
            'id': 'password',
            'placeholder': 'password',
            'style': 'color:black'})
