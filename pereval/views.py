from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status, viewsets

from .models import PerevalAdded
from .serializers import PerevalAddedSerializer, UserSerializer, CoordSerializer, LevelSerializer, ImageSerializer


class UserAddedViewset(viewsets.ModelViewSet):
    queryset = PerevalAdded.objects.all()
    serializer_class = UserSerializer


class CoordAddedViewset(viewsets.ModelViewSet):
    queryset = PerevalAdded.objects.all()
    serializer_class = CoordSerializer


class LevelAddedViewset(viewsets.ModelViewSet):
    queryset = PerevalAdded.objects.all()
    serializer_class = LevelSerializer


class PerevalAddedViewset(viewsets.ModelViewSet):
    queryset = PerevalAdded.objects.all()
    serializer_class = PerevalAddedSerializer


class ImageAddedViewset(viewsets.ModelViewSet):
    queryset = PerevalAdded.objects.all()
    serializer_class = ImageSerializer
