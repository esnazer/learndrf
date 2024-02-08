from rest_framework import viewsets
from django.contrib.auth import authenticate
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.request import Request
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework_simplejwt.authentication import JWTAuthentication
from api.serializers import CategorialSerializer, ProductSerializer, MyTokenObtainPairSerializer


class CategorialViewSet(viewsets.ModelViewSet):
    serializer_class = CategorialSerializer
    queryset = CategorialSerializer.Meta.model.objects.all()

class ProductViewSet(viewsets.ModelViewSet):
    serializer_class = ProductSerializer
    queryset = ProductSerializer.Meta.model.objects.all()
    #authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

class login(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer

    def post(self, request, *args, **kwargs):
        username = request.data.get('username')
        password = request.data.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            login_serializer = self.serializer_class(data=request.data)
            if login_serializer.is_valid():
                return Response({
                    'token': login_serializer.validated_data.get('access'),
                    'refresh': login_serializer.validated_data.get('refresh'),
                    'username': user.username,
                    'messaje': 'Login successful'
                })
        else:
            return Response({
                'error': 'Invalid credentials'
            })