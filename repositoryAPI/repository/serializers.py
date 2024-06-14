import base64

from django.core.files.base import ContentFile
from rest_framework import serializers
from .models import Person, Wish, Shaxzodbek, YouTube


class PersonSerializer(serializers.ModelSerializer):
	def get_photo(self, obj):
		if obj.photo:
			with open(obj.photo.path, 'rb') as image_file:
				return base64.b64encode(image_file.read()).decode('utf-8')  # Encode to base64
		return None

	class Meta:
		model = Person
		fields = '__all__'


class WishSerializer(serializers.ModelSerializer):
	photo = serializers.SerializerMethodField()

	def get_photo(self, obj):
		if obj.photo:
			with open(obj.photo.path, 'rb') as image_file:
				return base64.b64encode(image_file.read()).decode('utf-8')  # Encode to base64
		return None

	class Meta:
		model = Wish
		fields = '__all__'


class ShaxzodbekSerializer(serializers.ModelSerializer):
	photo = serializers.SerializerMethodField()

	def get_photo(self, obj):
		if obj.photo:
			with open(obj.photo.path, 'rb') as image_file:
				return base64.b64encode(image_file.read()).decode('utf-8')  # Encode to base64
		return None
	people = PersonSerializer(many=True)
	wish = WishSerializer()

	class Meta:
		model = Shaxzodbek
		fields = '__all__'


class YouTubeSerializer(serializers.ModelSerializer):
	class Meta:
		model = YouTube
		fields = '__all__'
