from django.urls import path
from . import views

urlpatterns = [
    path('', views.display, name = 'display'),
    path('upload/', views.upload, name = 'upload-book'),
    path('update/<int:book_id>', views.update_book),
    path('delete/<int:book_id>', views.delete_book)
]
