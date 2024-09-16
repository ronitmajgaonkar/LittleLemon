from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework import generics
from rest_framework import permissions, viewsets
from rest_framework.permissions import IsAuthenticated
from .models import Menu, Booking
from .serializers import menuSerializer, bookingSerializer, UserSerializer


# Create your views here.

def index(request):
    return render(request, 'index.html', {})

class MenuItemView(generics.ListCreateAPIView):
    queryset = Menu.objects.all()
    serializer_class = menuSerializer
    permission_classes = [permissions.IsAuthenticated]

class SingleMenuItemView(generics.RetrieveUpdateAPIView):
    queryset = Menu.objects.all()
    serializer_class = menuSerializer
    permission_classes = [permissions.IsAuthenticated]

class BookingViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Booking.objects.all()
    serializer_class = bookingSerializer

class UserViewSet(viewsets.ModelViewSet):
    queryset = User
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]