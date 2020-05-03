from django.forms import ModelForm,TextInput
from .models import City

class cityform(ModelForm):
    class Meta:
        model=City
        fields=['city']
        widgets={'city':TextInput(attrs={'class':'input','placeholder':'Enter city name'})}