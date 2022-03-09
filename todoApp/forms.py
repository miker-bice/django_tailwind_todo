from django import forms
from django.forms import ModelForm
from .models import TodoList


# Todo Form
class TodoForm(ModelForm):
    class Meta:
        model = TodoList
        fields = ('item', 'description', 'complete')

        widgets = {
            'item': forms.TextInput(attrs={'class': "bg-slate-800 rounded-full focus:ring-blue-400 px-4 w-full mb-4 "
                                                    "block"}),
            'description': forms.Textarea(attrs={'class': "block mb-4 p-2.5 w-full text-md text-gray-900 bg-gray-50 "
                                                          "rounded-lg border border-gray-300 focus:ring-blue-500 "
                                                          "focus:border-blue-500 dark:bg-gray-700 "
                                                          "dark:border-gray-600 dark:placeholder-gray-400 "
                                                          "dark:text-white dark:focus:ring-blue-500 "
                                                          "dark:focus:border-blue-500"}),
            'complete': forms.CheckboxInput(attrs={'class': "ml-6 w-4 h-4 bg-gray-50 rounded border "
                                                            "border-gray-300 "
                                                            "focus:ring-3 focus:ring-blue-300 dark:bg-gray-700 "
                                                            "dark:border-gray-600 dark:focus:ring-blue-600 "
                                                            "dark:ring-offset-gray-800"})
        }
