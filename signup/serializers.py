from rest_framework import serializers
from signup.models import KaizenUser


class KaizenUserCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = KaizenUser
        fields = [
            'username',
            'email',
            'password'
        ]


class KaizenUserDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = KaizenUser
        fields = [
            'username',
            'email',
            'is_verified'
        ]

class KaizenUserVerifySerializer(serializers.ModelSerializer):
    class Meta:
        model = KaizenUser
        fields = []