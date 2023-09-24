from django.shortcuts import render, redirect

from .forms import CommentForm, PostForm, CategoriesForm
from .models import Photo, Category

# Create your views here.
def index(request):
	posts = Photo.objects.all()
	categories = Category.objects.all()

	comment_form = CommentForm()

	if request.method == "POST":
		comment_form = CommentForm(request.POST)

		# validate Comment form
		if comment_form.is_valid():
			comment_post = comment_form.save(commit=False)
			if request.user.is_authenticated:
				comment_post.users = request.user 
				comment_post.photos_id = comment_form.cleaned_data['photos_id']
				comment_post.save()
		return redirect('FunShere')

	context = {
		'posts': posts,
		'categories': categories,
		'comment_form': comment_form,
	}
	return render(request, 'blog/index.html', context)
	

def add_post(request):
	form = PostForm()
	if request.method == 'POST':
		form = PostForm(request.POST, request.FILES)
		if form.is_valid():
			form_post = form.save(commit=False)
			if request.user.is_authenticated:
				form_post.users = request.user
				form_post.save()
				return redirect('FunShere')

	context = {
		'form': form,
	}

	return render(request, 'blog/add_post.html', context)

def edit_post(request, pk: int):
	posts = Photo.objects.get(id=pk)
	form = PostForm(instance=posts)
	if request.method == 'POST':
		form = PostForm(request.POST, request.FILES, instance=posts)
		if form.is_valid():
			form.save()
			return redirect('FunShere')

	context = {
		'form': form,
		'post_item': posts
	}

	return render(request, 'blog/edit_post.html', context)

def delete_post(request, pk):
	post = Photo.objects.get(id=pk)
	if request.method == 'POST':
		post.delete()
		return redirect('FunShere')
	context = {
		'post_item': post,
	}

	return render(request,'blog/delete_post.html', context)

def add_categories(request):
	form = CategoriesForm()
	if request.method == 'POST':
		form = CategoriesForm(request.POST, request.FILES)
		if form.is_valid():
			form.save()
			return redirect('FunShere')
	context = {
		'category_form': form,
	}

	return render(request, 'blog/add_category.html', context)

def category_list(request):
	categories = Category.objects.all()
	context = {
		'categories': categories
	}
	return render(request, 'users/show_profile.html', context)

def edit_category(request, pk:int):
	category = Category.objects.get(id=pk)
	form = CategoriesForm(instance=category)
	if request.method == 'POST':
		form = CategoriesForm(request.POST, request.FILES, instance=category)
		if form.is_valid():
			form.save()
			return redirect('FunShere')
	context = {
		'category_form': form,
	}
	return render(request, 'blog/edit_category.html', context)

def delete_category(request, pk:int):
	category = Category.objects.get(id=pk)
	if request.method == 'POST':
		category.delete()
		return redirect('FunShere')
	context = {
		'category_form': category
	}
	return render(request, 'blog/delete_category.html', context)