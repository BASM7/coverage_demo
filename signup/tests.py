import json
from django.contrib.auth.models import User
from signup.models import KaizenUser
from rest_framework.authtoken.models import Token
from rest_framework.test import APITestCase
from rest_framework import status
from signup.serializers import KaizenUserCreateSerializer, KaizenUserDetailSerializer, KaizenUserVerifySerializer


class SignUpTestCase(APITestCase):
    def test_signup_register(self):
        data = {'username': 'Alonso', 'email': 'alonso.moreno@mailinator.com', 'password': 'qwerty'}
        response = self.client.post('/api/create/', data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_signup_register_is_left_unverified(self):
        data = {'username': 'Alonso', 'email': 'alonso.moreno@mailinator.com', 'password': 'qwerty'}
        response = self.client.post('/api/create/', data)
        print(response)
        self.assertFalse(response.data.get('is_verified'))

    def test_signup_register_verification_code_not_empty(self):
        data = {'username': 'Alonso', 'email': 'alonso.moreno@mailinator.com', 'password': 'qwerty'}
        response = self.client.post('/api/create/', data)
        print(response)
        self.assertNotEqual(response.data.get('verification_code'), None)

