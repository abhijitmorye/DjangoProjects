from django.shortcuts import render
from django.http import HttpResponse
from .models import Books, Students, BoorowedBooks
# Create your views here.


def index(request):
    allBooks = Books.objects.all()
    allStudents = Students.objects.all()
    if request.method == 'POST':
        studentemailid_f = request.POST.get('studentEmailID')
        # print(request.POST.get('studentEmailID'))
        try:
            studentExists = Students.objects.get(
                studentEmailID=studentemailid_f)
            # print(studentExists.studentName)
        except:
            studentExists = None
        if studentExists is not None:
            bookid_f = request.POST.get('bookID')
            # print(request.POST.get('bookID'))
            try:
                isBookAvailable = Books.objects.get(bookID=bookid_f)
                # print(isBookAvailable.bookname)
            except:
                isBookAvailable = None
            if isBookAvailable is not None:
                if isBookAvailable.bookState == "available":
                    boorowedBook = BoorowedBooks(
                        stduent=studentExists, book=isBookAvailable)
                    boorowedBook.save()
                    isBookAvailable.bookState = "notavailable"
                    isBookAvailable.save()
                    context = {
                        'books': allBooks,
                        'students': allStudents,
                        'flag': True,
                        'msg': 'Book is assigned successfully to {}'.format(studentExists.studentName)
                    }
                    return render(request, 'LMSapp/index.html', context=context)
                else:
                    context = {
                        'books': allBooks,
                        'students': allStudents,
                        'flag': True,
                        'msg': 'Book is already assigned'
                    }
                    return render(request, 'LMSapp/index.html', context=context)
            else:
                context = {
                    'books': allBooks,
                    'students': allStudents,
                    'flag': True,
                    'msg': 'Book is not available'
                }
                return render(request, 'LMSapp/index.html', context=context)
        else:
            context = {
                'books': allBooks,
                'students': allStudents,
                'flag': True,
                'msg': 'Verify student mail id'
            }
            return render(request, 'LMSapp/index.html', context=context)
    context = {
        'books': allBooks,
        'students': allStudents,
        'flag': False,
        'msg': ''
    }

    return render(request, 'LMSapp/index.html', context=context)


def addBook(request):
    if request.method == 'POST':
        bookName = request.POST.get('bookname')
        bookPrice = request.POST.get('bookPrice')
        bookState = request.POST.get('bookState')
        book = Books(bookname=bookName, bookPrice=bookPrice,
                     bookState=bookState)
        book.save()
        context = {'flag': True}
        return render(request, 'LMSapp/addbook.html', context=context)
    context = {'flag': False}
    return render(request, 'LMSapp/addbook.html', context=context)


def addMember(request):
    if request.method == 'POST':
        studentName = request.POST.get('studentName')
        studentEmailID_new = request.POST.get('studentEmailID')
        try:
            studentExist = Students.objects.get(
                studentEmailID=studentEmailID_new)
        except:
            studentExist = None
        if studentExist is not None:
            context = {'flag': True, 'msg': "Student is already registered"}
            return render(request, 'LMSapp/addMember.html', context=context)
        else:
            student = Students(studentName=studentName,
                               studentEmailID=studentEmailID_new)
            student.save()
            context = {'flag': True, 'msg': "Student registered succesfully"}
            return render(request, 'LMSapp/addMember.html', context=context)
    context = {'flag': False, 'msg': "First Time"}
    return render(request, 'LMSapp/addMember.html', context=context)


def viewBooks(request):
    try:
        allBooks = Books.objects.all()
    except:
        allBooks = None
    if allBooks is not None:
        for book in allBooks:
            print(book.bookname)
        context = {'flag': False, 'msg': "", 'data': allBooks}
        return render(request, 'LMSapp/viewbooks.html', context=context)
    else:
        context = {'flag': False, 'msg': "No books found", 'data': allBooks}
        return render(request, 'LMSapp/viewbooks.html', context=context)


def viewMembers(request):

    try:
        allMembers = Students.objects.all()
    except:
        allMembers = None
    if allMembers is not None:
        context = {'flag': False, 'msg': '', 'data': allMembers}
        return render(request, 'LMSapp/viewmembers.html', context=context)
    else:
        context = {'flag': False,
                   'msg': 'No Members are registered here', 'data': allMembers}
        return render(request, 'LMSapp/viewmembers.html', context=context)
