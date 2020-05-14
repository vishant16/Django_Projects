from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.generics import ListCreateAPIView
from rest_framework import status
from rest_framework.response import Response
# Create your views here.
from .models import UserDetails
from .serializers import UserDetailsSerializer

class UserDetailsList(ListCreateAPIView):

    queryset = UserDetails.objects.all()
    serializer_class=UserDetailsSerializer

    def get(self, request):
        stocks = UserDetails.objects.all()
        serializers = self.serializer_class(stocks, many=True)
        return Response(serializers.data)

    def post(self, request,format=None):

        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self,request,pk=None):
        """updating objects"""
        return Response({'method':'PUT'})

    def patch(self,request,pk=None):
        """ updating objects partially """  # if we have first name and last name we have raise to change the last name so it will change last name only
        return Response({'method':'PATCH'})

    def delete(self,request,pk=None):
        """Deleting objects"""
        return Response({'method':'DELETE'})
