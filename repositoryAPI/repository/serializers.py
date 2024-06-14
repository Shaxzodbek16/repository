from rest_framework import serializers
from .models import Person, Wish, Shaxzodbek, YouTube


class PersonSerializer(serializers.ModelSerializer):
	class Meta:
		model = Person
		fields = '__all__'


class WishSerializer(serializers.ModelSerializer):
	class Meta:
		model = Wish
		fields = '__all__'


class ShaxzodbekSerializer(serializers.ModelSerializer):
	person = PersonSerializer(many=True)
	wish = WishSerializer(many=True)

	class Meta:
		model = Shaxzodbek
		fields = '__all__'


class YouTubeSerializer(serializers.ModelSerializer):
	class Meta:
		model = YouTube
		fields = '__all__'
