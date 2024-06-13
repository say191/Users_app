from rest_framework import serializers
from users.models import User
from users.validators import PhoneValidator, PassportValidator
from rest_framework.exceptions import ValidationError


class UserSerializer(serializers.ModelSerializer):
    """Сериализатор для модели Пользователя"""

    class Meta:
        model = User
        fields = '__all__'
        validators = [PhoneValidator(field='phone'), PassportValidator(field='passport_number')]

    def validate(self, data):
        """Метод валидации данных для определения обязательных к заполнению полей
        в зависимости от http-заголовка 'X-Device'"""

        device = self.context['request'].headers['x-Device']

        if device == 'mail':
            required_fields = ['first_name', 'email']
            missing_fields = [field for field in required_fields if field not in data]

            if missing_fields:
                raise ValidationError("Имя и электронная почта являются обязательными полями к заполнению. "
                                      f"Пожалуйста заполните: {', '.join(missing_fields)}")

        elif device == 'mobile':

            if not data.get('phone'):
                raise ValidationError("Номер телефона является обязательным полем к заполнению. "
                                      "Пожалуйста заполните: phone")

        elif device == 'web':
            required_fields = ['last_name', 'first_name', 'patronymic', 'birth_date',
                               'passport_number', 'birth_place', 'phone', 'registration_address']
            missing_fields = [field for field in required_fields if field not in data]

            if missing_fields:
                raise ValidationError("Все поля являются обязательными к заполнению, за исключением электронной "
                                      "почты и адресса проживания. "
                                      f"Пожалуйста заполните: {', '.join(missing_fields)}")
        return data
