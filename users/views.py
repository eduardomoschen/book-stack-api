from rest_framework import generics
from .models import User
from .serializers import UserSerializer
from .permissions import (
    UserAdminPermissionClass,
    UserOwnerOrAdminPermissionClass
)

class UserListCreateAPIView(generics.ListCreateAPIView):
    permission_classes = (UserAdminPermissionClass,)
    queryset = User.objects.all()
    serializer_class = UserSerializer

class UserDetailView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (UserOwnerOrAdminPermissionClass,)
    queryset = User.objects.all()
    serializer_class = UserSerializer
    lookup_field = 'username'
