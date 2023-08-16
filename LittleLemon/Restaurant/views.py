from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
from .serializers import MenuItemSerializer, BookingSerializer
from .models import MenuItem, Booking
from rest_framework import generics
from rest_framework.viewsets import ModelViewSet 
from rest_framework.permissions import IsAuthenticated

# Create your views here.
def index(request: HttpRequest) -> HttpResponse:
    return render(request, "index.html", {})

# create menu view
class MenuItemsView(generics.ListCreateAPIView):
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer

class SingleMenuItemView(generics.RetrieveUpdateAPIView, 
                         generics.DestroyAPIView):
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer

class BookingViewSet(ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer 
    permission_classes = [IsAuthenticated]