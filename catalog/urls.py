from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name = 'index'),
    path('books/', views.books, name='books'),
    path('books/<int:pk>', views.bookDetails, name='bookDetails'),
    path('authors/', views.authors, name='authors'),
    path('authors/<int:pk>', views.authorDetails, name='authorDetails')
]