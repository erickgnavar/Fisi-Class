from django import forms
from .models import Author


class AuthorForm(forms.ModelForm):

	def clean_name(self):
		name = self.cleaned_data.get('name')
		if len(name) >= 5:
			return name
		else:
			raise forms.ValidationError('se requiere como minimo 5 letras')

	class Meta:
		model = Author