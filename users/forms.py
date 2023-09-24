from django.forms import ModelForm

from .models import User 
from blog.models import Photo


class UserForm(ModelForm):
	class Meta:
		model = User
		fields = '__all__'


class PostForm(ModelForm):
	class Meta:
		model = Photo
		fields = '__all__'