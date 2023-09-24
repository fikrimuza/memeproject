from django.forms import ModelForm
from django import forms

from .models import Photo, Comment, Category


class CommentForm(ModelForm):
	photos_id = forms.IntegerField(widget=forms.HiddenInput())

	class Meta:
		model = Comment
		fields = ['comment']

class PostForm(ModelForm):
	class Meta:
		model = Photo
		fields = '__all__'
		exclude = (
				'comments',
				'users'
			)

class CategoriesForm(ModelForm):
	class Meta:
		model = Category
		fields = '__all__'
