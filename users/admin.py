from django.contrib import admin
from users.models import User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    """Класс UserAdmin для отображения модели пользователя со всеми его атрибутами
    в панели администратора с возможностью поиска пользователя по нескольким полям:
    фамилия, имя, отчество, телефон и элеткронная почта"""

    list_display = [field.name for field in User._meta.fields]
    search_fields = ['last_name', 'first_name', 'patronymic', 'phone', 'email']
