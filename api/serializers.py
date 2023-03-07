from rest_framework import serializers
from api.models import Comic, Publisher


class ComicSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comic
        fields = ('__all__')


class PublisherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Publisher
        fields = ('__all__')