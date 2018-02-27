from django.contrib import admin

from .models import Book
from .models import Category
from .models import Author, Rates

admin.site.register(Book)
admin.site.register(Category)
admin.site.register(Author)
admin.site.register(Rates)