from django.shortcuts import render
from .models import Teacher
from rest_framework import generics
from .serializers import TeacherSerializer
# Create your views here.


class TeacherCreate(generics.CreateAPIView):
    # API endpoint that allows creation of a new customer
    queryset = Teacher.objects.all(),
    serializer_class = TeacherSerializer


class TeacherDetail(generics.RetrieveAPIView):
    # API endpoint that returns a single customer by pk.
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer
    
    
class TeacherList(generics.ListAPIView):
    # API endpoint that allows customer to be viewed.
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer


class TeacherUpdate(generics.RetrieveUpdateAPIView):
    # API endpoint that allows a customer record to be updated.
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer


class TeacherDelete(generics.RetrieveDestroyAPIView):
    # API endpoint that allows a customer record to be deleted.
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer
    