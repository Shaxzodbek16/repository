import base64
from rest_framework import serializers
from .models import Person, Wish, Shaxzodbek, YouTube, Game


class GameSerializer(serializers.ModelSerializer):
	photo = serializers.SerializerMethodField()

	def get_photo(self, obj):
		if obj.photo:
			with open(obj.photo.path, 'rb') as image_file:
				return base64.b64encode(image_file.read()).decode('utf-8')  # Encode to base64
		return None
	class Meta:
		model = Game
		fields = '__all__'


class PersonSerializer(serializers.ModelSerializer):
	photo = serializers.SerializerMethodField()

	def get_photo(self, obj):
		if obj.photo:
			with open(obj.photo.path, 'rb') as image_file:
				return base64.b64encode(image_file.read()).decode('utf-8')  # Encode to base64
		return None
	game = GameSerializer(many=True, read_only=True)

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


