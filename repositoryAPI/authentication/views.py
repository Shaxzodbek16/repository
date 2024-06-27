from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import AuthenticationSerializer


class AuthenticationApiView(APIView):
    def get(self, request, pk=None):
        serializer = AuthenticationSerializer(request.user)
        return Response(serializer.data)


