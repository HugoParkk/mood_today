from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response

from .models import User
from .serializers import UserSerializer
from rest_framework import status


class UserView(APIView):
    def get(self, request, **kwargs):
        if kwargs.get('user_email') is None:
            user_queryset = User.objects.all()
            user_queryset_serializer = UserSerializer(user_queryset, many=True)
            return Response(user_queryset_serializer.data, status=status.HTTP_200_OK)
        else:
            user_email = kwargs.get('user_email')
            user_serializer = UserSerializer(User.objects.get(email=user_email))
            return Response(user_serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        user_serializer = UserSerializer(data=request.data)  # Request의 data를 UserSerializer로 변환

        if user_serializer.is_valid():
            user_serializer.save()  # UserSerializer의 유효성 검사를 한 뒤 DB에 저장
            return Response(user_serializer.data, status=status.HTTP_201_CREATED)  # client에게 JSON response 전달
        else:
            return Response(user_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, **kwargs):
        if kwargs.get('user_email') is None:
            return Response("invalid request", status=status.HTTP_400_BAD_REQUEST)
        else:
            user_email = kwargs.get('user_email')
            user_object = User.objects.get(email=user_email)

            update_user_serializer = UserSerializer(user_object, data=request.data)
            if update_user_serializer.is_valid():
                user_object.delete()
                update_user_serializer.save()
                return Response(update_user_serializer.data, status=status.HTTP_200_OK)
            else:
                return Response("invalid request", status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, **kwargs):
        if kwargs.get('user_email') is None:
            return Response("invalid request", status=status.HTTP_400_BAD_REQUEST)
        else:
            user_email = kwargs.get('user_email')
            user_object = User.objects.get(email=user_email)
            user_object.delete()
            return Response("delete complete", status=status.HTTP_200_OK)