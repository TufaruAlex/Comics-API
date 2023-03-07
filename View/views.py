from rest_framework import generics
from api.models import Comic, Publisher
from api.serializers import ComicSerializer, PublisherSerializer
from django.shortcuts import render


def homeView(request):
    return render(request, "templates.html")


class ComicList(generics.ListCreateAPIView):
    serializer_class = ComicSerializer

    def get_queryset(self):
        queryset = Comic.objects.all()
        publisher = self.request.query_params.get('publisher')
        if publisher is not None:
            queryset = queryset.filter(comicPublisher=publisher)
        return queryset


class ComicDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ComicSerializer
    queryset = Comic.objects.all()


class PublisherList(generics.ListCreateAPIView):
    serializer_class = PublisherSerializer
    queryset = Publisher.objects.all()


class PublisherDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = PublisherSerializer
    queryset = Publisher.objects.all()
