# from django import forms
# from django.contrib.auth.models import User
# from django.contrib.auth.forms import UserCreationForm
#
#
# class SignUpForm(UserCreationForm):
#     username = forms.CharField(max_length=30)
#     email = forms.EmailField(max_length=200)
#
#     class Meta:
#         model = User
#         fields = ('username', 'email', 'password1', 'password2', )

# from django import forms
# from django.contrib.auth.models import User
# from django.contrib.auth.forms import UserCreationForm
#
#
# class UserRegisterForm(UserCreationForm):
#     email = forms.EmailField()
#     phone_no = forms.CharField(max_length=20)
#     first_name = forms.CharField(max_length=20)
#     last_name = forms.CharField(max_length=20)
#
#     class Meta:
#         model = User
#         fields = ['username', 'email', 'phone_no', 'password1', 'password2']