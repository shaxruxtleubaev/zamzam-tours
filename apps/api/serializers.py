from rest_framework.serializers import *
from apps.clients.models import Client
from apps.tours.models import Tour
from apps.videos.models import Video

class ClientSerializer(ModelSerializer):

    image_url = SerializerMethodField()

    class Meta:

        model = Client
        fields = '__all__'

    def get_image_url(self, obj):
        request = self.context.get('request')
        if obj.image:
            image_url = obj.image.url
            return request.build_absolute_uri(image_url)
        return None

class TourSerializer(ModelSerializer):

    image_url = SerializerMethodField()

    class Meta:

        model = Tour
        fields = '__all__'

    def get_image_url(self, obj):
        request = self.context.get('request')
        if obj.image:
            image_url = obj.image.url
            return request.build_absolute_uri(image_url)
        return None

class VideoSerializer(ModelSerializer):

    image_url = SerializerMethodField()

    class Meta:

        model = Video
        fields = '__all__'

    def get_image_url(self, obj):
        request = self.context.get('request')
        if obj.image:
            image_url = obj.image.url
            return request.build_absolute_uri(image_url)
        return None