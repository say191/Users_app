from django.db import models

NULLABLE = {'blank': True, 'null': True}


class User(models.Model):
    """Модель для класса пользователя, в которой ряд атрибутов такие как
    номер пасспорта, телефон и электронная почта являются уникальными значениями,
    изначально все поля являются nullable, т к в дальнейшем обязательность к заполнению полей
    будет определятся в зависимости от http-заголовка 'X-Device'.
    Так же поле id в модели пользователя по умолчанию является полем первичного ключа (primary key)
    и не требует явного указания"""

    last_name = models.CharField(max_length=30, verbose_name='фамилия', **NULLABLE)
    first_name = models.CharField(max_length=30, verbose_name='имя', **NULLABLE)
    patronymic = models.CharField(max_length=30, verbose_name='отчество', **NULLABLE)
    birth_date = models.DateField(verbose_name='дата рождения', **NULLABLE)
    passport_number = models.CharField(unique=True, max_length=11, verbose_name='номер паспорта', **NULLABLE)
    birth_place = models.CharField(max_length=300, verbose_name='место рождения', **NULLABLE)
    phone = models.CharField(unique=True, max_length=11, verbose_name='телефон', **NULLABLE)
    email = models.EmailField(unique=True, verbose_name='емейл', **NULLABLE)
    registration_address = models.CharField(max_length=300, verbose_name='адрес регистрации', **NULLABLE)
    residential_address = models.CharField(max_length=300, verbose_name='адрес проживания', **NULLABLE)

    def __str__(self):
        return f"{self.last_name} {self.first_name} {self.email}"

    class Meta:
        verbose_name = 'пользователь'
        verbose_name_plural = 'пользователи'
