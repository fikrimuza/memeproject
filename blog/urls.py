from django. urls import path 

from .views import (
		index, 
		add_post, 
		edit_post, 
		delete_post, 
		add_categories,
		edit_category,
		delete_category,
	)


urlpatterns = [
	path('', index, name='FunShere'),
	path('upload/', add_post, name='upload'),
	path('edit-post/<int:pk>', edit_post, name='edit'),
	path('delete-post/<int:pk>', delete_post, name='delete'),
	path('category/', add_categories, name='category'),
	path('edit-category/<int:pk>', edit_category, name='edit_category'),
	path('delete-category/<int:pk>', delete_category, name='delete_category'),
]