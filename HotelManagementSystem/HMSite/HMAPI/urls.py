from django.contrib import admin
from django.urls import path
from .views import ListRoomsView, ListRoomTypeListView, UpdateRoomTypeListView, ListRoomStatusView, ListGuests, UpdateGuestProfile, UpdateRoomView, ListReservations, UpdateReservation

urlpatterns = [
    path('listroom',  ListRoomsView.as_view(), name='listrooms'),
    path('updateroom/<int:pk>', UpdateRoomView.as_view(), name='updateroom'),
    path('listroomtypes', ListRoomTypeListView.as_view(), name='listroomtype'),
    path('updateroomtype/<int:pk>',
         UpdateRoomTypeListView.as_view(), name='updateroomtype'),
    path('listroomstatus', ListRoomStatusView.as_view(), name='listroomstatus'),
    path('listguests', ListGuests.as_view(), name='listguests'),
    path('updateprofile/<int:pk>',
         UpdateGuestProfile.as_view(), name='updateprofile'),
    path('listreservations', ListReservations.as_view(), name='listreservations'),
    path('updatereservations/<int:pk>',
         UpdateReservation.as_view(), name='updatereservaations'),
]
