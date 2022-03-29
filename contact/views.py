from django.contrib.auth import get_user_model
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK, HTTP_400_BAD_REQUEST
from rest_framework.views import APIView

from .serializers import ContactSerializer, UserSerializer
from rest_framework import permissions
from .models import Contact, CustomUser
from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveUpdateAPIView, RetrieveAPIView, \
    RetrieveUpdateDestroyAPIView


# Create your views here.

class ContactList(ListAPIView):
    permission_classes = (permissions.IsAdminUser,)
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer


# POST
class ContactCreate(CreateAPIView):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer


class UserList(ListAPIView):
    permission_classes = (permissions.IsAdminUser,)
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer


# POST
class UserDetail(RetrieveUpdateDestroyAPIView):
    permission_classes = (permissions.IsAdminUser,)
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer


class UserCreate(CreateAPIView):
    permission_classes = (permissions.IsAdminUser,)
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer

# class UserLoginApiView(APIView):
#     permission_classes = (permissions.AllowAny,)
#     queryset = User.objects.all()
#
#     def post(self, request, *args, **kwargs):
#         data = request.data
#         serializer = UserLoginSerializer(data=data)
#         if serializer.is_valid(raise_exception=True):
#             new_data = serializer.data
#             return Response(new_data, status=HTTP_200_OK)
#         return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)
