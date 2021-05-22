from django.shortcuts import redirect, render
from django.http import HttpResponse
from .models import Book
from .forms import BookForm


# Create your views here.

# views in django are nothing but an functions that accepts requests
# apply view with particular url pattern
def index(request):
    books = Book.objects.all() # this is an context
    print(books)
    context = {
        'books': books
    }
    return render(request, 'MyApp/index.html', context)


def products(request):
    books = Book.objects.all() # this is an context
    print(books)
    context = {
        'books': books
    }
    return render(request, 'MyApp/index.html', context)




def details(request, book_id):

    books_details = Book.objects.get(id=book_id)
    context = {
        "books_details": books_details
    }
    return render(request, 'MyApp/details.html', context)



def add_book(request):

    if request.method == "POST":
        name = request.POST.get('name',)
        genre = request.POST.get('genre',)
        price = request.POST.get('price',)
        book_image = request.FILES['book_image']

        book = Book(name=name, genre=genre, price=price, book_image=book_image)
        book.save()

    return render(request, 'MyApp/add_book.html')



def update(request,book_id):
    book = Book.objects.get(id=book_id)
    # creating form object and passing request.POST or None, FILES if any and instance of book object which is to be updated
    form = BookForm(request.POST or None, request.FILES, instance=book)
    if form.is_valid():
        form.save()
        return redirect('/products/')    
    return render(request, 'MyApp/update.html', {'form': form, 'book': book})


def delete(request,book_id):

    if request.method == "POST":

        book = Book.objects.get(id=book_id)
        result = book.delete()
        if result[0] == 1:
            return redirect('/products/')

    return render(request, "Myapp/delete.html")



