from django import forms

class CreateGroupForm(forms.Form):
	name = forms.CharField(max_length=30)
	description = forms.CharField(max_length=100)

class CreateWebmapItemsForm(forms.Form):
	name = forms.CharField(max_length=30)
	description = forms.CharField(max_length=100)