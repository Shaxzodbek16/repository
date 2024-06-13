from rest_framework import serializers
from .models import Person, Wish, Shaxzodbek


class PersonSerializer(serializers.ModelSerializer):
	class Meta:
		model = Person
		fields = '__all__'


class WishSerializer(serializers.ModelSerializer):
	class Meta:
		model = Wish
		fields = '__all__'


class ShaxzodbekSerializer(serializers.ModelSerializer):
	class Meta:
		model = Shaxzodbek
		fields = '__all__'
