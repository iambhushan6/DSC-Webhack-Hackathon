from django import forms
from main import models

class Citizenform(forms.ModelForm):
    
    class Meta:
        model = models.Citizen
        fields = "__all__"
        
class Vac_centerform(forms.ModelForm):
    
    class Meta:
        model = models.Vac_center
        fields = "__all__"
