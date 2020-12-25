from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Subject(models.Model):
    subject = models.CharField(max_length=50)
    def __str__(self):
        return self.subject

class Publisher(models.Model):
    publisher = models.CharField(max_length=100)
    def __str__(self):
        return self.publisher

class BookCategory(models.Model):
    category = models.CharField(max_length=50)
    def __str__(self):
        return self.category

class Book(models.Model):
    book_name = models.CharField(max_length=100)
    publisher = models.ForeignKey(Publisher, on_delete=models.SET_NULL, null=True)
    category = models.ForeignKey(BookCategory, on_delete=models.SET_NULL, null=True)
    print_price = models.IntegerField()
    jalaram_price = models.Iprint_price = models.IntegerField()
    quantity = models.IntegerField(default=0)
    added_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    def __str__(self):
        return self.book_name

class OrderBooking(models.Model):
    booked_order = models.ForeignKey(Book, on_delete=models.CASCADE)
    quantity_booked = models.IntegerField(default=0)
    booking_user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    booking_time = models.DateTimeField(auto_now_add=True)

class BookBuying(models.Model):
    bought_book = models.ForeignKey(Book, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    purchasing_staff = models.ForeignKey(User, on_delete=models.CASCADE)
    purchasing_datetime = models.DateTimeField(auto_now_add=True)

class BookSelling(models.Model):
    sold_book = models.ForeignKey(Book, on_delete=models.CASCADE)
    selling_quantity = models.IntegerField(default=1)
    purchasing_user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='purchasing_user')
    selling_staff = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='staff')
    selling_datetime = models.DateTimeField(auto_now_add=True)
