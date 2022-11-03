from rest_framework import status
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.response import Response

from api.user.api.serializers import UserListSerializer, UserCreateSerializer, UserDetailSerializer, \
    UserUpdateSerializer
from rest_framework.permissions import IsAuthenticated, AllowAny

from api.user.models import User


class UserView(ListCreateAPIView):
    serializer_class = UserListSerializer
    permission_classes = [AllowAny]

    def get_queryset(self):
        return User.objects.all()

    def create(self, request, *args, **kwargs):
        data = request.data
        serializer = UserCreateSerializer(data=data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(
                {
                    "data": serializer.data,
                },
                status=status.HTTP_201_CREATED,
            )


class UserDetailView(RetrieveUpdateDestroyAPIView):
    serializer_class = UserDetailSerializer
    permission_classes = [AllowAny]

    def get_object(self):
        user_id = self.kwargs["user_id"]
        try:
            return User.objects.get(id=user_id)
        except User.DoesNotExist:
            return Response(
                {
                    "message": "Not Found",
                },
                status=status.HTTP_400_BAD_REQUEST,
            )

    def put(self, request, *args, **kwargs):
        user = self.get_object()
        data = request.data
        serializer = UserUpdateSerializer(user, data=data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(
                {
                    "data": serializer.data,
                },
                status=status.HTTP_200_OK,
            )

    def delete(self, request, *args, **kwargs):
        user = self.get_object()
        user.delete()
