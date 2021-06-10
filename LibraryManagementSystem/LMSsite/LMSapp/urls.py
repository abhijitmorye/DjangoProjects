from django.contrib import admin
from django.urls import path, include
from LMSapp import views

app_name = 'LMSapp'
urlpatterns = [
    path('', views.index, name='index'),
    path('addbook', views.addBook, name='addbook'),
    path('addmember', views.addMember, name='addmember'),
    path('viewbook', views.viewBooks, name='viewbook'),
    path('viewmembers', views.viewMembers, name='viewmembers'),
    path('updatebook/<int:book_id>', views.updateBook, name='updatebook'),
    path('returnbook', views.bookReturn, name='returnbook'),
    path('return/<int:book_id>', views.returnSucc, name='returnsuc'),
    path('updatemember/<int:member_id>',
         views.updateMember, name='updatemember'),
]
