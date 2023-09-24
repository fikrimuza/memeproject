from django.shortcuts import render

def index(request):
	context = {
		'judul': 'Home',
		'heading': 'Selamat datang di halaman utama'
	}
	return render(request, 'index.html', context)
	