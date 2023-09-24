from django.db import models
from users.models import User


# Create your models here.
class Comment(models.Model):
	comment = models.CharField(max_length=255, blank=True, null=True)
	photos = models.ForeignKey('Photo', on_delete=models.CASCADE)
	users = models.ForeignKey(User, on_delete=models.CASCADE)

	def __str__(self):
		return (f'{self.users} - {self.comment}')

class Photo(models.Model):
	caption = models.CharField(max_length=200)
	users = models.ForeignKey(User, on_delete=models.CASCADE)
	meme_photo = models.ImageField()
	upload = models.DateTimeField(auto_now_add=True)
	comments = models.ForeignKey('Comment', on_delete=models.CASCADE, null=True, blank=True)
	category = models.ForeignKey('Category', on_delete=models.CASCADE, null=True, blank=True)

	def __str__(self):
		return (f'{self.caption}')
		
class Category(models.Model):
	name = models.CharField(max_length=255, unique=True)
	category_image = models.ImageField(upload_to='Category_img/')

	def __str__(self):
		return (f'{self.id}. {self.name}')
