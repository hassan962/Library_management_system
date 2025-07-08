from django.db import models

# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length=255)
    author = models.TextField()
    isbn = models.CharField(max_length=20, unique=True)
    publisher = models.CharField(max_length=255)
    num_pages = models.IntegerField()
    stock = models.PositiveIntegerField(default=1)
    def __str__(self):
        return f"{self.title} by {self.author}"
    
class Member(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    outstanding_debt = models.DecimalField(max_digits=7, decimal_places=2, default=0.00)
    def __str__(self):
        return self.name
    
class Transaction(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    member = models.ForeignKey(Member, on_delete=models.CASCADE)
    issue_date = models.DateField(auto_now_add=True)
    return_date = models.DateField(null=True, blank=True)
    rent_fee = models.DecimalField(max_digits=6, decimal_places=2, default=0.00)

    def __str__(self):
        return f"{self.book.title} issued to {self.member.name}"