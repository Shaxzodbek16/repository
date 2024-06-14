from django.shortcuts import render
from rest_framework import filters
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import status, permissions
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Shaxzodbek, Person, Wish, YouTube
from .serializers import ShaxzodbekSerializer, PersonSerializer, WishSerializer, YouTubeSerializer


def terms(request):
	return render(request, 'terms.html')


def _404(request):
	return render(request, '404.html')


class ShaxzodbekApiView(APIView):
	permission_classes = [permissions.AllowAny]
	filter_backends = [filters.SearchFilter, filters.OrderingFilter]
	ordering_fields = ['-category']
	search_fields = ['category']

	def get_queryset(self):
		return Shaxzodbek.objects.all()

	def get(self, request, pk=None):
		if pk:
			try:
				category = Shaxzodbek.objects.get(pk=pk)
				serializer = ShaxzodbekSerializer(category)
				return Response(serializer.data)
			except Shaxzodbek.DoesNotExist:
				return Response(status=status.HTTP_404_NOT_FOUND)
		else:
			categories = Shaxzodbek.objects.all()
			serializer = ShaxzodbekSerializer(categories, many=True)
			return Response(serializer.data)

	def post(self, request):
		serializer = ShaxzodbekSerializer(data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data, status=status.HTTP_201_CREATED)
		else:
			return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

	def put(self, request, pk=None):
		try:
			category = Shaxzodbek.objects.get(pk=pk)
		except Shaxzodbek.DoesNotExist:
			return Response({"error": " not found"}, status=status.HTTP_404_NOT_FOUND)

		serializer = ShaxzodbekSerializer(category, data=request.data, partial=True)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

	def delete(self, request, pk=None):
		try:
			category = Shaxzodbek.objects.get(pk=pk)
			category.delete()
			return Response({"message": "successfully deleted"}, status=status.HTTP_204_NO_CONTENT)
		except Shaxzodbek.DoesNotExist:
			return Response({"error": " not found"}, status=status.HTTP_404_NOT_FOUND)


class PersonApiView(APIView):
	permission_classes = [permissions.AllowAny]

	def get(self, request, pk=None):
		if pk:
			try:
				category = Person.objects.get(pk=pk)
				serializer = PersonSerializer(category)
				return Response(serializer.data)
			except Person.DoesNotExist:
				return Response(status=status.HTTP_404_NOT_FOUND)
		else:
			categories = Person.objects.all()
			serializer = PersonSerializer(categories, many=True)
			return Response(serializer.data)

	def post(self, request):
		serializer = PersonSerializer(data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data, status=status.HTTP_201_CREATED)
		else:
			return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

	def put(self, request, pk=None):
		try:
			category = Person.objects.get(pk=pk)
		except Person.DoesNotExist:
			return Response({"error": "Person not found"}, status=status.HTTP_404_NOT_FOUND)

		serializer = PersonSerializer(category, data=request.data, partial=True)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

	def delete(self, request, pk=None):
		try:
			category = Person.objects.get(pk=pk)
			category.delete()
			return Response({"message": "Person successfully deleted"}, status=status.HTTP_204_NO_CONTENT)
		except Person.DoesNotExist:
			return Response({"error": "Person not found"}, status=status.HTTP_404_NOT_FOUND)


class WishApiView(APIView):
	permission_classes = [permissions.AllowAny]

	def get(self, request, pk=None):
		if pk:
			try:
				category = Wish.objects.get(pk=pk)
				serializer = WishSerializer(category)
				return Response(serializer.data)
			except Wish.DoesNotExist:
				return Response(status=status.HTTP_404_NOT_FOUND)
		else:
			categories = Wish.objects.all()
			serializer = WishSerializer(categories, many=True)
			return Response(serializer.data)

	def post(self, request):
		serializer = WishSerializer(data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data, status=status.HTTP_201_CREATED)
		else:
			return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

	def put(self, request, pk=None):
		try:
			category = Wish.objects.get(pk=pk)
		except Wish.DoesNotExist:
			return Response({"error": "Wish not found"}, status=status.HTTP_404_NOT_FOUND)

		serializer = WishSerializer(category, data=request.data, partial=True)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

	def delete(self, request, pk=None):
		try:
			category = Wish.objects.get(pk=pk)
			category.delete()
			return Response({"message": "Wish successfully deleted"}, status=status.HTTP_204_NO_CONTENT)
		except Wish.DoesNotExist:
			return Response({"error": "Wish not found"}, status=status.HTTP_404_NOT_FOUND)


class YouTubeApiView(APIView):
	permission_classes = [permissions.AllowAny]

	def get(self, request, pk=None):
		if pk:
			try:
				category = YouTube.objects.get(pk=pk)
				serializer = YouTubeSerializer(category)
				return Response(serializer.data)
			except YouTube.DoesNotExist:
				return Response(status=status.HTTP_404_NOT_FOUND)
		else:
			categories = YouTube.objects.all()
			serializer = YouTubeSerializer(categories, many=True)
			return Response(serializer.data)

	def post(self, request):
		serializer = YouTubeSerializer(data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data, status=status.HTTP_201_CREATED)
		else:
			return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

	def put(self, request, pk=None):
		try:
			category = YouTube.objects.get(pk=pk)
		except YouTube.DoesNotExist:
			return Response({"error": "YouTube not found"}, status=status.HTTP_404_NOT_FOUND)

		serializer = YouTubeSerializer(category, data=request.data, partial=True)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

	def delete(self, request, pk=None):
		try:
			category = YouTube.objects.get(pk=pk)
			category.delete()
			return Response({"message": "YouTube successfully deleted"}, status=status.HTTP_204_NO_CONTENT)
		except YouTube.DoesNotExist:
			return Response({"error": "YouTube not found"}, status=status.HTTP_404_NOT_FOUND)
