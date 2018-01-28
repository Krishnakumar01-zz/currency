from django import forms

class CurrencyForm(forms.Form):
	fromm=forms.CharField(max_length=3)
	to=forms.CharField(max_length=3)
	fiels=('from','to')