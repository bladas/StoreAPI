import jwt
from django.http import Http404
from rest_framework import generics, status
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from .serializers import CartObjectListSerializer
from .models import CartItem, Cart


class CartObjectListView(APIView):
    serializer_class = CartObjectListSerializer
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        pass

    def get(self, request, format=None):
        user = self.request.user
        print(user.id)
        cart = Cart.objects.filter(user=user)[0]
        print(cart)
        products_in_cart = CartItem.objects.filter(cart=cart)
        print(products_in_cart)
        serializer = CartObjectListSerializer(products_in_cart, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = CartObjectListSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# class ProductDetailView(APIView):
#     queryset = CartItem.objects.all()
#     serializer_class = ProductSerializer
#     """
#     Retrieve, update or delete a snippet instance.
#     """
#     def get_object(self, pk):
#         try:
#             return CartItem.objects.get(pk=pk)
#         except CartItem.DoesNotExist:
#             raise Http404
#
#     def get(self, request, pk, format=None):
#         snippet = self.get_object(pk)
#         serializer = ProductSerializer(snippet)
#         return Response(serializer.data)
#
#     def put(self, request, pk, format=None):
#         product = self.get_object(pk)
#         serializer = ProductSerializer(product, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#     def delete(self, request, pk, format=None):
#         product = self.get_object(pk)
#         product.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)
