from rest_framework import serializers
from HMapp.models import RoomType, RoomStatus, Room, Guest, Reservation


class RoomTypeSerializer(serializers.ModelSerializer):

    roomTypeImage = serializers.ImageField(max_length=None, use_url=True)

    class Meta:
        model = RoomType
        fields = ['roomTypeID', 'roomTypeName', 'roomTypeImage', 'roomPrice']


class RoomStatusSerializer(serializers.ModelSerializer):

    class Meta:
        model = RoomStatus
        fields = ['roomStatusID', 'roomStatus']


class RoomSerializer(serializers.ModelSerializer):

    class Meta:
        model = Room
        fields = ['roomID', 'roomType', 'roomStatus']


class GuestSerializer(serializers.ModelSerializer):

    guestProfileImage = serializers.ImageField(use_url=True, max_length=None)

    class Meta:
        model = Guest
        fields = ['guestID', 'guestFirstName', 'guestLastName',
                  'guestAddess', 'guestEmailID', 'guestPhone', 'guestProfileImage']


class ReservationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reservation
        fields = ['reservationID', 'guest',
                  'room', 'checkINDate', 'checkOutDate', 'noOfAdults', 'noOfChildren', 'totolPrice']
