from django.shortcuts import render, redirect, get_object_or_404
from .models import Book, Member, Transaction
from .forms import BookForm, MemberForm, TransactionForm
from django.db.models import Q
import requests
from django.contrib import messages
from datetime import date

# Create your views here.
# CRUD for Books

def book_list(request):
    books = Book.objects.all()
    return render(request, 'book_list.html', {'books': books})

def book_create(request):
    form = BookForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('book_list')
    return render(request, 'book_form.html', {'form': form})

def book_update(request, b_id):
    book = get_object_or_404(Book, id=b_id)
    form = BookForm(request.POST or None, instance=book)
    if form.is_valid():
        form.save()
        return redirect('book_list')
    return render(request, 'book_form.html', {'form': form})

def book_delete(request, b_id):
    book = get_object_or_404(Book, id=b_id)
    if request.method == 'POST':
        book.delete()
        return redirect('book_list')
    return render(request, 'book_delete.html', {'book': book})

#CRUD on Members

def member_list(request):
    members = Member.objects.all()
    return render(request, 'member_list.html', {'members': members})

def member_create(request):
    form = MemberForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('member_list')
    return render(request, 'member_form.html', {'form': form})

def member_update(request, b_id):
    member = get_object_or_404(Member, id=b_id)
    form = MemberForm(request.POST or None, instance=member)
    if form.is_valid():
        form.save()
        return redirect('member_list')
    return render(request, 'member_form.html', {'form': form})

def member_delete(request, b_id):
    member = get_object_or_404(Member, id=b_id)
    if request.method == 'POST':
        member.delete()
        return redirect('member_list')
    return render(request, 'member_delete.html', {'member': member})

#Issue a book
def issue_book(request):
    form = TransactionForm(request.POST or None)
    if form.is_valid():
        transaction = form.save(commit=False)
        if transaction.book.stock <= 0:
            messages.error(request, 'Book is out of stock.')
        elif transaction.member.outstanding_debt > 500:
            messages.error(request, 'Member has outstanding debt over Rs.500.')
        else:
            transaction.book.stock -= 1
            transaction.book.save()
            transaction.save()
            messages.success(request, 'Book issued successfully.')
            return redirect('transaction_list')
    return render(request, 'issue_book.html', {'form': form})


#Return a book
def return_book(request, transaction_id):
    transaction = get_object_or_404(Transaction, id=transaction_id)
    if not transaction.return_date:
        transaction.return_date = date.today()
        transaction.rent_fee = 100 
        transaction.member.outstanding_debt += transaction.rent_fee
        transaction.member.save()
        transaction.book.stock += 1
        transaction.book.save()
        transaction.save()
        messages.success(request, 'Book returned with rent fee.')
    return redirect('transaction_list')

def transaction_list(request):
    transactions = Transaction.objects.select_related('book', 'member').order_by('-issue_date')
    return render(request, 'transaction_list.html', {'transactions': transactions})


# Search Books by name and author
def search_books(request):
    query = request.GET.get('q', '')
    books = []
    if query:
        books = Book.objects.filter(Q(title__icontains=query) | Q(author__icontains=query))
    return render(request, 'book_search.html', {'books': books, 'query': query})


#Import books from API
def import_books(request):
    if request.method == 'POST':
        page = request.POST.get('page', 1)
        title = request.POST.get('title', '')
        url = f"https://frappe.io/api/method/frappe-library?page={page}&title={title}"
        res = requests.get(url)
        data = res.json().get('message', [])
        for book in data:
            Book.objects.get_or_create(
                title=book['title'],
                author=book['authors'],
                isbn=book['isbn'],
                publisher=book['publisher'],
                num_pages=book['  num_pages'] or 0,
                defaults={'stock': 1}
            )
        messages.success(request, f"Imported {len(data)} books from API.")
        return redirect('book_list')
    return render(request, 'import_books.html')