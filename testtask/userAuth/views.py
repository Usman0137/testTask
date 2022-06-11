from rest_framework import generics, status, views
from rest_framework.generics import RetrieveUpdateDestroyAPIView, ListCreateAPIView
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken

from .utils import Util
from .models import User
from django.contrib.sites.shortcuts import get_current_site
from .serializers import RegisterSerializer, LoginSerializer
import jwt
from django.conf import settings
import random
import string


from django.contrib.sites.shortcuts import get_current_site
from django.urls import reverse


class RegisterView(generics.GenericAPIView):
    serializer_class = RegisterSerializer

    def post(self, request):
        user = request.data
        serializer = self.serializer_class(data=user)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        user_data = serializer.data
        email = user_data['email']
        user = User.objects.get(email=user_data['email'])
        length = 10
        lower = string.ascii_lowercase
        upper = string.ascii_uppercase
        num = string.digits
        symbols = string.punctuation
        all = lower + upper + num + symbols
        temp = random.sample(all, length)
        password = "".join(temp)
        print(password)
        user.set_password(password)
        user.save()
        email_body = 'Hi ' + user.firstName + ' welcome use below password to login \n Email: ' + email + '\n Password: '+str(password)
        data = {'email_body': email_body, 'to_email': user.email, 'email_subject': 'Your account credentials'}
        Util.send_email(data)

        return Response(user_data,
                        status=status.HTTP_201_CREATED)


class LoginAPIView(generics.GenericAPIView):
    serializer_class = LoginSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
