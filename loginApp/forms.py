from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms


class UserRegistrationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

        widgets = {
            'username': forms.TextInput(attrs={
                'class': "bg-gray-50 border border-gray-300 text-gray-900 text-sm "
                         "rounded-lg focus:ring-blue-500 focus:border-blue-500 block "
                         "w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 "
                         "dark:placeholder-gray-400 dark:text-white "
                         "dark:focus:ring-blue-500 dark:focus:border-blue-500",
                'autocomplete': 'off'}),
            'email': forms.EmailInput(attrs={
                'class': "bg-gray-50 border border-gray-300 text-gray-900 text-sm "
                         "rounded-lg focus:ring-blue-500 focus:border-blue-500 block "
                         "w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 "
                         "dark:placeholder-gray-400 dark:text-white "
                         "dark:focus:ring-blue-500 dark:focus:border-blue-500",
                'placeholder': "samplemail@email.com",
                'autocomplete': 'off'}),
            'password1': forms.PasswordInput(attrs={
                'class': "bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 "
                         "focus:border-blue-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 "
                         "dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500"
                         "dark:focus:border-blue-500"}),
            'password2': forms.PasswordInput(attrs={
                'class': "bg-gray-50 border border-gray-300 text-gray-900 text-sm "
                         "rounded-lg focus:ring-blue-500 focus:border-blue-500 "
                         "block w-full p-2.5 dark:bg-gray-700 "
                         "dark:border-gray-600 dark:placeholder-gray-400 "
                         "dark:text-white dark:focus:ring-blue-500 "
                         "dark:focus:border-blue-500"})
        }

# natapos ka sa paghahanap ng paraan kung paano i style yung forms
