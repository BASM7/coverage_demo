from rest_framework.response import Response
from rest_framework import generics, status
from login.models import KaizenUser
from login.serializers import KaizenUserCreateSerializer, KaizenUserDetailSerializer, KaizenUserVerifySerializer


class KaizenUserDetailAPIView(generics.RetrieveAPIView):
    queryset = KaizenUser.objects.all()
    serializer_class = KaizenUserDetailSerializer
    lookup_field = 'verification_code'

class KaizenUserVerifyAPIView(generics.RetrieveAPIView):
    queryset = KaizenUser.objects.all()
    serializer_class = KaizenUserVerifySerializer
    lookup_field = 'verification_code'

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.is_verified = True
        instance.save()
        return Response({
            'username': instance.username,
            'is_verified': instance.is_verified,
            'verification_code': 'EXPIRED'
        })


class KaizenUserCreateAPIView(generics.CreateAPIView):
    queryset = KaizenUser.objects.all()
    serializer_class = KaizenUserCreateSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response({
            'username': serializer.instance.username,
            'is_verified': serializer.instance.is_verified,
            'verification_code': serializer.instance.verification_code
        }, status=status.HTTP_201_CREATED, headers=headers)



