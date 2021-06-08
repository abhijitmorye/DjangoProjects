from django.shortcuts import render
from django.http import HttpResponse
from .models import Books, Students, BoorowedBooks
# Create your views here.


def index(request):

    return render(request, 'LMSapp/index.html')


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
        studentExist = Students.objects.get(studentEmailID=studentEmailID_new)
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
