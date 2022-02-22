from django.shortcuts import render
from rest_framework.views import APIView
from .models import *
from .serializer import *
from rest_framework.response import Response
from rest_framework import generics

class ReactView(generics.ListCreateAPIView):
    queryset = React.objects.all()
    serializer_class = ReactSerializer

class UpdateView(generics.RetrieveUpdateDestroyAPIView):
    queryset = React.objects.all()
    serializer_class = ReactSerializer

# class ReactView(APIView):
#     def get(self,request):
#         output = [{"employee": output.employee,
#                    "department": output.department}
#                   for output in React.objects.all()]
#         return Response(output)
#
#     def post(self,request):
#         serializers = ReactSerializer(data=request.data)
#         if serializers.is_valid(raise_exception=True):
#             serializers.save()
#             return Response(serializers.data)


