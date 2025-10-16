from django.urls import path
from . import views

urlpatterns = [
    path('', views.welcome, name='welcome'),
    path('about/', views.about, name='about'),
    path('book/', views.book_list, name='book_list'),
    path('book/<int:id>/', views.book_detail, name='book_detail'),
    path('new_book/', views.new_book, name='new_book'),
    path('book/delete/<int:id>/', views.delete_book, name='delete_books'),
    path('book/<int:id>/delete/', views.delete_book, name='delete_book'),
    path('book/modify/<int:id>/', views.modify_book, name='modify_books'),
    path('book/<int:id>/modify/', views.modify_book, name='modify_book'),
  
]