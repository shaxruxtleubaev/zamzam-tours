from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.pagination import *
from rest_framework.status import *
from .serializers import (
    ClientSerializer,
    TourSerializer,
    VideoSerializer,
)
from apps.clients.models import Client
from apps.tours.models import Tour
from apps.videos.models import Video

class ClientAPIView(APIView):

    def post(self, request):
        serializer = ClientSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(
                serializer.data,
                status=HTTP_201_CREATED
            )
        return Response(
            serializer.errors,
            status=HTTP_400_BAD_REQUEST
        )
    
class TourAPIView(APIView):

    def get(self, request):
        tours = Tour.objects.all()
        serializer = TourSerializer(tours, many=True)
        return Response(serializer.data)
    
class VideoAPIView(APIView):

    def get(self, request):
        videos = Video.objects.all()
        serializer = VideoSerializer(videos, many=True)
        return Response(serializer.data)