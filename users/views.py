from rest_framework.viewsets import generics
from users.serializers import UserSerializer
from users.models import User
from django_filters.rest_framework import DjangoFilterBackend


class UserCreateAPIView(generics.CreateAPIView):
    """Контроллер для создания пользователя"""

    serializer_class = UserSerializer


class UserRetrieveAPIView(generics.RetrieveAPIView):
    """Контроллер для получения пользователя по id"""

    serializer_class = UserSerializer
    queryset = User.objects.all()


class UserSearchApiView(generics.ListAPIView):
    """Контроллер для поиска пользователей по одному или нескольким
    полям: фамилия, имя, отчество, телефон, элетронная почта"""

    serializer_class = UserSerializer
    queryset = User.objects.all()
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ('last_name', 'first_name', 'patronymic', 'phone', 'email')
