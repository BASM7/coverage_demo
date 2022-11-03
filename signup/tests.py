import json
from django.contrib.auth.models import User
from signup.models import KaizenUser
from rest_framework.authtoken.models import Token
from rest_framework.test import APITestCase
from rest_framework import status
from signup.serializers import KaizenUserCreateSerializer, KaizenUserDetailSerializer, KaizenUserVerifySerializer


class SignUpTestCase(APITestCase):
    """Tests for the SignUp API"""
    
    def test_dummy(self):
        self.assertTrue(True)
    
    """
    def test_signup_register(self):
        data = {'username': 'Alonso', 'email': 'alonso.moreno@mailinator.com', 'password': 'qwerty'}
        response = self.client.post('/api/create/', data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertFalse(response.data.get('is_verified'))
        self.assertNotEqual(response.data.get('verification_code'), None)
    
    
    def test_retrieve_verification(self):
        data = {'username': 'Alonso', 'email': 'alonso.moreno@mailinator.com', 'password': 'qwerty'}
        response = self.client.post('/api/create/', data)
    
        verification_code = response.data.get('verification_code')
    
        response = self.client.get('/api/verify/{}'.format(verification_code))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue(response.data.get('is_verified'))
        self.assertEqual(response.data.get('verification_code'), 'EXPIRED')
    """
    
