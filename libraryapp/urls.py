from django.urls import path
from . import views

urlpatterns = [
    path('', views.book_list, name='book_list'),
    path('book/add/', views.book_create, name='book_add'),
    path('book/update/<int:b_id>/', views.book_update, name='book_update'),
    path('book/delete/<int:b_id>/', views.book_delete, name='book_delete'),
    path('members/', views.member_list, name='member_list'),
    path('member/add/', views.member_create, name='member_add'),
    path('member/update/<int:b_id>/', views.member_update, name='member_update'),
    path('member/delete/<int:b_id>/', views.member_delete, name='member_delete'),
    path('issue/', views.issue_book, name='issue_book'),
    path('return/<int:transaction_id>/', views.return_book, name='return_book'),
    path('search/', views.search_books, name='search_books'),
    path('import/', views.import_books, name='import_books'),
    path('transactions/', views.transaction_list, name='transaction_list'),

]