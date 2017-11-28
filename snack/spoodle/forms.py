from django import forms

from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _

from .models import Todo, Class, Note

'''
class TodoForm(forms.Form):
	todotext = forms.CharField(help_text="Write your todo item here.")
	def clean_todotext(self):
		data = self.cleaned_data['todotext']
		return data
'''
class TodoForm(forms.ModelForm):
	def clean_activity(self):
		data = self.cleaned_data['activity']
		return data
	class Meta:
		model = Todo
		fields = ("activity",)
		#todotext = forms.CharField(help_text="Write your todo item here.")

class ClassChatForm(forms.ModelForm):
	def clean_chat(self):
		data = self.cleaned_data['chat']
		return data
	class Meta:
		model = Class
		fields = ("chat",)

class NoteForm(forms.ModelForm):
	def clean_note(self):
		data = self.cleaned_data["note","classes", "title"]
		return data
	class Meta:
		model = Note
		fields = ("note","classes", "title")
