from django import forms


class suscformulario(forms.Form):
    nombre= forms.CharField(max_length=30)
    email= forms.EmailField()


class betaformulario(forms.Form):   
    nombre= forms.CharField(max_length=30)
    email= forms.EmailField()


class inscformulario(forms.Form):   
    nombre= forms.CharField(max_length=30)
    email= forms.EmailField()