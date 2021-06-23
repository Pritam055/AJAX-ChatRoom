from django import forms
from django.core.exceptions import ValidationError
 
from .models import Room

class Form1(forms.Form):
    room_name = forms.CharField(max_length=10, label="Room name", widget=forms.TextInput(attrs={'class':'form-control','required':'True'}))
    username = forms.CharField(max_length=20, label="Username",widget=forms.TextInput(attrs={'class':'form-control','required':'True'}))

    def clean(self):
        self.cleaned_data = super().clean()
        room_name = self.cleaned_data.get('room_name')
        username = self.cleaned_data.get("username") 
        if room_name is None or username is None:
            raise forms.ValidationError("Empty forms") 
  
    """ def clean(self):
        room_name = self.cleaned_data.get('name')
        if room_name is None:
            self._errors['name'] =self.error_class(['Empty form!!!'])
        elif Room.objects.filter(name__iexact=room_name).exists():
            self._errors['name'] = self.error_class(['Room of this name already created.'])
        
        return self.cleaned_data """