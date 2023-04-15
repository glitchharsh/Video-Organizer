from django.shortcuts import render
from django.db.models import Q
from rest_framework import generics, views
from rest_framework.response import Response
from .serializers import VideoSerializer
from .models import Video

class ListVideosAPI(generics.ListAPIView):
    queryset = Video.objects.all()
    serializer_class = VideoSerializer
    filterset_fields = {'published_at':['gt','lt']}
    ordering_fields = ['published_at', 'video_title', 'description', 'channel_title']

class ListSearchResultsAPI(generics.ListAPIView):
    serializer_class = VideoSerializer
    
    def get_queryset(self):
        search = self.request.GET.get('q')
        if search:
            query = Q(video_title__icontains=search) | Q(description__icontains=search)
            return Video.objects.filter(query)
        return Video.objects.none()