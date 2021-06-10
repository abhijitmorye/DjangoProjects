from django.shortcuts import render, redirect
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


def updateBook(request, book_id):
    if request.method == 'POST':
        bookname_f = request.POST.get('bookname')
        bookPrice_f = request.POST.get('bookPrice')
        bookState_f = request.POST.get('bookState')
        book = Books.objects.get(bookID=request.POST.get('bookID'))
        oldbookname = book.bookname
        oldbookprice = book.bookPrice
        oldbookState = book.bookState
        if bookname_f == '':
            book.bookname = oldbookname
        else:
            book.bookname = bookname_f
        if bookPrice_f == '':
            book.bookPrice = oldbookprice
        else:
            book.bookPrice = bookPrice_f
        if bookState_f == '':
            book.bookState = oldbookState
        else:
            book.bookState = bookState_f
        book.save()
        return redirect('/viewbook')

    book = Books.objects.get(bookID=book_id)
    if book.bookState == 'available':
        bookSelected = True
    else:
        bookSelected = False
    context = {
        'book': book,
        'bookSelected': bookSelected
    }
    return render(request, 'LMSapp/updatebook.html', context=context)


def bookReturn(request):
    if request.method == 'POST':
        studentemailid_f = request.POST.get('studentEmailID')
        try:
            studentExists = Students.objects.get(studentEmailID=studentEmailID)
        except:
            studentExists = False

        if studentExists is not None:
            borrowedBooks = []
            allBorrowedBooks = BoorowedBooks.objects.all()
            for book in allBorrowedBooks:
                if book.stduent.studentEmailID == studentemailid_f:
                    borrowedBooks.append(book.book)
            if len(borrowedBooks) > 0:
                context = {
                    'flag': True,
                    'borrowedBooks': borrowedBooks,
                    'Bookflag': True,
                    'studentExist': True,
                    'msg': ""
                }
                return render(request, 'LMSapp/returnbook.html', context=context)
            else:
                context = {
                    'flag': True,
                    'borrowedBooks': borrowedBooks,
                    'Bookflag': False,
                    'studentExist': True,
                    'msg': " Student has not borrowed any books from libabry"
                }
                return render(request, 'LMSapp/returnbook.html', context=context)
        else:
            context = {
                'flag': True,
                'borrowedBooks': [],
                'Bookflag': False,
                'NoBookFlag': False,
                'studentExist': False,
                'msg': " Student does exists"
            }
            return render(request, 'LMSapp/returnbook.html', context=context)

    context = {
        'flag': False,
        'borrowedBooks': [],
        'Bookflag': False,
        'studentExist': False,
        'msg': ""

    }
    return render(request, 'LMSapp/returnbook.html', context=context)


def returnSucc(request, book_id):
    try:
        print(book_id)
        bookBorrowed = Books.objects.get(bookID=book_id)
        bookBorrowed.bookState = 'available'
        bookBorrowed.save()
        borrowedBooks = BoorowedBooks.objects.all()
        print(borrowedBooks)
        for book in borrowedBooks:
            if book.book.bookID == bookBorrowed.bookID:
                book.delete()
            else:
                return HttpResponse("Something went wrong")
    except:
        book = None
        return HttpResponse("Something went wrong")

    return redirect('/returnbook')


def updateMember(request, member_id):
    if request.method == 'POST':
        studentName_f = request.POST.get('studentName')
        studentEmailID_f = request.POST.get('studentEmailID')
        student = Students.objects.get(studentID=member_id)
        oldstudentName = student.studentName
        oldstudentEmailID = student.studentEmailID
        if studentName_f == '':
            student.studentName = oldstudentName
        else:
            student.studentName = studentName_f
        if studentEmailID_f == '':
            student.studentEmailID = oldstudentEmailID
        else:
            student.studentEmailID = studentEmailID_f
        student.save()
        return redirect('/viewmembers')

    student = Students.objects.get(studentID=member_id)
    if member is not None:
        context = {
            'student': student
        }
        return render(request, 'LMSapp/updateMember.html', context=context)
