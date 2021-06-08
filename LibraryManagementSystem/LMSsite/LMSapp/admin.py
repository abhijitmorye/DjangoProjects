from django.contrib import admin
from .models import Books, Students, BoorowedBooks

# Register your models here.
admin.site.register(Books)
admin.site.register(Students)
admin.site.register(BoorowedBooks)
