from users.apps import UsersConfig
from django.urls import path
from users.views import UserCreateAPIView, UserRetrieveAPIView, UserSearchApiView

app_name = UsersConfig.name

urlpatterns = [
    path('create/', UserCreateAPIView.as_view(), name='create_user'),
    path('<int:pk>/', UserRetrieveAPIView.as_view(), name='get_user'),
    path('search/', UserSearchApiView.as_view(), name='search_user')
]
