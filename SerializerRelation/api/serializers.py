from .models import Singer, Song
from rest_framework import serializers

class SongSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Song
        fields = ['id', 'title', 'url', 'singer', 'duration']

# class SongSerializer(serializers.ModelSerializer):
#     singer = serializers.StringRelatedField(read_only=True)
#     singer = serializers.PrimaryKeyRelatedField(queryset=Singer.objects.all())  # This allows you to pass singer_id in the request
#     class Meta:
#         model = Song
#         fields = ['id', 'title', 'url', 'singer', 'duration']

class SingerSerializer(serializers.ModelSerializer):
    # song = serializers.SlugRelatedField(many=True, read_only=True, slug_field='title')
    song = serializers.HyperlinkedRelatedField(many=True, read_only=True, view_name='song-detail')
    # song = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    # song = serializers.StringRelatedField(many=True, read_only=True)
    class Meta:
        model = Singer
        fields = ['id', 'name', 'gender','song']