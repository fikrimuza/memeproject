from django.urls import path 

from .views import show_profile, edit_profile


urlpatterns = [
	path('<int:pk>', show_profile, name='show_profile'),
	path('edit/<int:pk>', edit_profile, name='edit_profile'),
]