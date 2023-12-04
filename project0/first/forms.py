from django import forms
# from first.models import Student

class SignupForm(forms.Form):
    name=forms.CharField()
    email=forms.EmailField()
    password=forms.CharField(widget=forms.PasswordInput())


class SigninForm(forms.Form):
    name=forms.CharField()
    password1=forms.CharField(widget=forms.PasswordInput())
    password2=forms.CharField(widget=forms.PasswordInput())


class StudentForm(forms.Form):
    name=forms.CharField()
    place=forms.CharField()
    subject=forms.CharField()
    age=forms.IntegerField()
    gender=forms.CharField()


class BookForm(forms.Form):
    title=forms.CharField()
    author=forms.CharField()
    p_year=forms.IntegerField()
    genre=forms.CharField()