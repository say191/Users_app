from rest_framework.serializers import ValidationError


class PassportValidator:
    """Валидатор для поля номера паспорта. Он необходим для того, чтобы
    пользователь мог ввести номер и серию паспорта исключительно в формате ХХХХ ХХХХХХ
    состоящего из цифр"""

    def __init__(self, field):
        self.field = field

    def __call__(self, value):
        passport_number = value.get(self.field)

        if passport_number:
            passport_parts = passport_number.split(' ')

            if len(passport_parts) != 2:
                raise ValidationError("Серия и номер паспорта должны быть формата ХХХХ ХХХХХХ и состоять только из цифр")

            series, number = passport_parts

            if len(series) != 4 or not series.isdigit():
                raise ValidationError("Серия и номер паспорта должны быть формата ХХХХ ХХХХХХ и состоять только из цифр")

            if len(number) != 6 or not number.isdigit():
                raise ValidationError("Серия и номер паспорта должны быть формата ХХХХ ХХХХХХ и состоять только из цифр")


class PhoneValidator:
    """Валидатор для поля телефона, необходиммый для ввода пользователем номера телефона
    исключительно в формате 7ХХХХХХХХХХ"""

    def __init__(self, field):
        self.field = field

    def __call__(self, value):
        phone = value.get(self.field)

        if phone:
            if len(phone) != 11 or phone[0] != '7':
                raise ValidationError("Номер телефона должен быть формата 7ХХХХХХХХХХ")
