from .models import Award
from django import forms
class NewAwardForm(forms.ModelForm):
    class Meta:
        model = Image
        fields = ['title','description','url_link','profile','image']