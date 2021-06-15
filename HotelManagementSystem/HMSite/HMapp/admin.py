from django.contrib import admin
from .models import RoomType, RoomStatus, Room, Guest, Reservation

# Register your models here.

admin.site.register(RoomType)
admin.site.register(RoomStatus)
admin.site.register(Room)
admin.site.register(Guest)
admin.site.register(Reservation)
