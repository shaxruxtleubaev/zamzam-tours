from rest_framework.serializers import *
from apps.clients.models import Client
from apps.tours.models import Tour
from apps.videos.models import Video

class ClientSerializer(ModelSerializer):

    class Meta:

        model = Client
        fields = '__all__'

class TourSerializer(ModelSerializer):

    class Meta:

        model = Tour
        fields = '__all__'

class VideoSerializer(ModelSerializer):

    class Meta:

        model = Video
        fields = '__all__'