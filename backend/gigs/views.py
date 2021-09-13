from django.shortcuts import render
from rest_framework import viewsets
from .serializers import GigSerializer, UserSerializer
from .models import Gig, User

# Create your views here.
from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, world. You're at the gigs index.")

class GigView(viewsets.ModelViewSet):
    serializer_class = GigSerializer
    queryset = Gig.objects.all()

class UserView(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.all()