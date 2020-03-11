from django.contrib.auth import get_user_model
from django.http import Http404
from rest_framework import permissions, generics
from rest_framework import response, decorators, permissions, status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken

from apps.users.models import UserProfile
from .serializers import UserCreateSerializer, UserSerializer, UserProfileSerializer

User = get_user_model()


@decorators.api_view(["POST"])
@decorators.permission_classes([permissions.AllowAny])
def registration(request):
    serializer = UserCreateSerializer(data=request.data)
    if not serializer.is_valid():
        return response.Response(serializer.errors, status.HTTP_400_BAD_REQUEST)
    user = serializer.save()
    refresh = RefreshToken.for_user(user)
    res = {
        "refresh": str(refresh),
        "access": str(refresh.access_token),
    }
    return response.Response(res, status.HTTP_201_CREATED)


class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserProfileList(APIView):
    serializer_class = UserProfileSerializer
    queryset = UserProfile.objects.all()

    def get(self, request, format=None):
        products = UserProfile.objects.all()
        serializer = UserProfileSerializer(products, many=True)
        return Response(serializer.data)


# class UserProfileDetail(generics.RetrieveAPIView):
#     queryset = UserProfile.objects.all()
#     serializer_class = UserProfileSerializer

class UserProfileDetail(APIView):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer
    """
    Retrieve, update or delete a snippet instance.
    """
    def get_object(self, pk):
        try:
            return UserProfile.objects.get(pk=pk)
        except UserProfile.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        snippet = self.get_object(pk)
        serializer = UserProfileSerializer(snippet)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        product = self.get_object(pk)
        serializer = UserProfileSerializer(product, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        product = self.get_object(pk)
        product.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)