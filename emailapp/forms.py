from django import forms

class Emailapp(forms.Form):
    Email = forms.EmailField()

    def __str__(self):
        return self.Email
