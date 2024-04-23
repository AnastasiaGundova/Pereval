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

    # def create(self, request, *args, **kwargs):
    #     serializer = PerevalAddedSerializer(data=request.data)
    #
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response({
    #             'status': status.HTTP_200_OK,
    #             'message': None,
    #             'id': serializer.data['id'],
    #         })
    #     elif status.HTTP_400_BAD_REQUEST:
    #         return Response({
    #             'status': status.HTTP_400_BAD_REQUEST,
    #             'message': 'Bad Request',
    #             'id': None,
    #         })
    #     elif status.HTTP_500_INTERNAL_SERVER_ERROR:
    #         return Response({
    #             'status': status.HTTP_500_INTERNAL_SERVER_ERROR,
    #             'message': 'Ошибка подключения к базе данных',
    #             'id': None,
    #         })


class ImageAddedViewset(viewsets.ModelViewSet):
    queryset = PerevalAdded.objects.all()
    serializer_class = ImageSerializer
