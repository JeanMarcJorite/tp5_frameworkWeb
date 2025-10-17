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
    path('book/<int:id>/addReview/', views.new_review, name='new_review'),
    path('book/<int:book_id>/editReview/<int:review_id>/', views.modify_review, name="modify_review"),
    path('book/<int:book_id>/deleteReview/<int:review_id>/', views.delete_review, name="delete_review")
]