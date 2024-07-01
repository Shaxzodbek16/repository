import base64
from rest_framework import serializers
from .models import Person, Wish, Shaxzodbek, YouTube, Game


class GameSerializer(serializers.ModelSerializer):
    photo_url = serializers.SerializerMethodField()

    def get_photo_url(self, obj):
        return f"https://api.shaxzodbek.com{obj.photo.url}"

    class Meta:
        model = Game
        fields = '__all__'


class PersonSerializer(serializers.ModelSerializer):
    photo_url = serializers.SerializerMethodField()

    def get_photo_url(self, obj):
        return f"https://api.shaxzodbek.com{obj.photo.url}"

    class Meta:
        model = Person
        fields = '__all__'


class WishSerializer(serializers.ModelSerializer):
    photo_url = serializers.SerializerMethodField()

    def get_photo_url(self, obj):
        return f"https://api.shaxzodbek.com{obj.photo.url}"

    class Meta:
        model = Wish
        fields = '__all__'


class ShaxzodbekSerializer(serializers.ModelSerializer):
    photo_url = serializers.SerializerMethodField()

    def get_photo_url(self, obj):
        return f"https://api.shaxzodbek.com{obj.photo.url}"

    people = PersonSerializer(many=True)
    wish = WishSerializer()

    class Meta:
        model = Shaxzodbek
        fields = '__all__'


class YouTubeSerializer(serializers.ModelSerializer):
    class Meta:
        model = YouTube
        fields = '__all__'
