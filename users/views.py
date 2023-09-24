from django.shortcuts import render, redirect

from blog.models import Photo, Category
from .forms import UserForm
from .models import User

# Create your views here.
def show_profile(request, pk):
	user = User.objects.get(id=pk)
	categories = Category.objects.all()
	posts = Photo.objects.filter(users_id=user.id)
	context = {
		'user': user,
		'posts': posts,
		'categories': categories,
	}

	return render(request, 'users/show_profile.html', context)

def edit_profile(request, pk: int):
	user = User.objects.get(id=pk)
	form = UserForm(instance=user)
	if request.method == 'POST':
		form = UserForm(request.POST, request.FILES, instance=user)
		if form.is_valid():
			form.save()
			return redirect('show_profile')
	context = {
		'user': user,
		'form': form,
	}

	return render(request, 'users/edit_profile.html', context)

