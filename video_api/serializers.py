from rest_framework import serializers
from .models import Video

class VideoSerializer(serializers.ModelSerializer):
    link = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Video
        fields = '__all__'
    
    def get_link(self, obj):
        return f'https://youtu.be/{obj.video_id}'