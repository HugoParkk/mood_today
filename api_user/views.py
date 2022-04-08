from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response

class UserView(APIView):
    def get(self, request):
        return Response('ok', status=200) # test res