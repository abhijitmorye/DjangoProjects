from django.shortcuts import render
from HMapp.models import RoomType, RoomStatus, Room, Guest, Reservation
from rest_framework import generics
from .serializers import RoomTypeSerializer, RoomStatusSerializer, RoomSerializer, GuestSerializer, ReservationSerializer


# Create your views here.

class ListRoomTypeListView(generics.ListCreateAPIView):
    queryset = RoomType.objects.all()
    serializer_class = RoomTypeSerializer


class UpdateRoomTypeListView(generics.RetrieveUpdateDestroyAPIView):
    queryset = RoomType.objects.all()
    serializer_class = RoomTypeSerializer


class ListRoomStatusView(generics.ListCreateAPIView):
    queryset = RoomStatus.objects.all()
    serializer_class = RoomStatusSerializer


class UpdateRoomStatus(generics.RetrieveUpdateDestroyAPIView):
    queryset = RoomStatus.objects.all()
    serializer_class = RoomStatusSerializer


class ListGuests(generics.ListCreateAPIView):
    queryset = Guest.objects.all()
    serializer_class = GuestSerializer


class UpdateGuestProfile(generics.RetrieveUpdateDestroyAPIView):
    queryset = Guest.objects.all()
    serializer_class = GuestSerializer


class ListRoomsView(generics.ListCreateAPIView):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer


class UpdateRoomView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer


class ListReservations(generics.ListCreateAPIView):
    queryset = Reservation.objects.all()
    serializer_class = ReservationSerializer


class UpdateReservation(generics.RetrieveUpdateDestroyAPIView):
    queryset = Reservation.objects.all()
    serializer_class = ReservationSerializer
