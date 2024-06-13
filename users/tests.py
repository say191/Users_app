from rest_framework.test import APITestCase
from rest_framework import status
from users.models import User


class UserTestCase(APITestCase):
    """Набор тестов для проверки функциональности API пользователей"""

    def setUp(self):
        """Настройка тестовых данных с двумя начальными пользователями,
        которые необходимы для тестирования функционала по получению пользователя по id
        и поиску пользователя по ряду полей"""

        self.user1 = User.objects.create(
            first_name='Ivan',
            last_name='Ivanov',
            patronymic='Ivanovich',
            birth_date='1990-01-01',
            passport_number='1111 111111',
            birth_place='Ivanovo',
            phone='733333333',
            email='Ivan@mail.ru',
            registration_address='Ivanovo st Pushkina 1-1',
            residential_address='Ivanovo st Pushkina 1-1'
        )

        self.user2 = User.objects.create(
            first_name='Petr',
            last_name='Petrov',
            patronymic='Petrovich',
            birth_date='1991-05-05',
            passport_number='2222 222222',
            birth_place='Omsk',
            phone='74444444444',
            email='Petr@mail.ru',
            registration_address='Omsk st Brova 7-45',
            residential_address='Omsk st Brova 7-45'
        )

    def test_create_user(self):
        """Тесты создания нового пользователя с допустимыми и недопостимыми данными,
        в зависимости от http-заголовка "x-Device"""

        headers = {
            'HTTP_x-Device': 'mail'
        }

        true_data = {
            "first_name": "Igor",
            "email": "me@mail.ru"
        }

        response = self.client.post(
            '/users/create/',
            data=true_data,
            **headers
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_201_CREATED
        )

        self.assertEqual(
            response.json(),
            {
                'id': 3,
                'last_name': None,
                'first_name': 'Igor',
                'patronymic': None,
                'birth_date': None,
                'passport_number': None,
                'birth_place': None,
                'phone': None,
                'email': 'me@mail.ru',
                'registration_address': None,
                'residential_address': None
            }
        )

        wrong_data = {
            "last_name": "Baydikov",
            "phone": "79999999999"
        }

        response = self.client.post(
            '/users/create/',
            data=wrong_data,
            **headers
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_400_BAD_REQUEST
        )

        self.assertEqual(
            response.json(),
            {
                'non_field_errors': [
                    'Имя и электронная почта являются обязательными полями к заполнению. Пожалуйста заполните: '
                    'first_name, email'
                ]
            }
        )

        headers = {
            'HTTP_x-Device': 'mobile'
        }

        true_data = {
            "first_name": "Igor",
            "phone": "79999999999"
        }

        response = self.client.post(
            '/users/create/',
            data=true_data,
            **headers
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_201_CREATED
        )

        self.assertEqual(
            response.json(),
            {
                'id': 4,
                'last_name': None,
                'first_name': 'Igor',
                'patronymic': None,
                'birth_date': None,
                'passport_number': None,
                'birth_place': None,
                'phone': '79999999999',
                'email': None,
                'registration_address': None,
                'residential_address': None
            }
        )

        wrong_data = {
            "first_name": "Igor",
            "last_name": "Baydikov"
        }

        response = self.client.post(
            '/users/create/',
            data=wrong_data,
            **headers
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_400_BAD_REQUEST
        )

        self.assertEqual(
            response.json(),
            {
                'non_field_errors': [
                    'Номер телефона является обязательным полем к заполнению. '
                    'Пожалуйста заполните: phone'
                ]
            }
        )

        headers = {
            'HTTP_x-Device': 'web'
        }

        true_data = {
            "last_name": "Baydikov",
            "first_name": "Igor",
            "patronymic": "Sergeevich",
            "birth_date": "1994-01-01",
            "passport_number": "1234 123456",
            "birth_place": "Moscow",
            "phone": "79999999991",
            "registration_address": "Moscow, st Lenina 8-94"
        }

        response = self.client.post(
            '/users/create/',
            data=true_data,
            **headers
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_201_CREATED
        )

        self.assertEqual(
            response.json(),
            {
                'id': 5,
                'last_name': 'Baydikov',
                'first_name': 'Igor',
                'patronymic': 'Sergeevich',
                'birth_date': '1994-01-01',
                'passport_number': '1234 123456',
                'birth_place': 'Moscow',
                'phone': '79999999991',
                'email': None,
                'registration_address': 'Moscow, st Lenina 8-94',
                'residential_address': None
            }
        )

        wrong_data = {
            "last_name": "Baydikov",
            "first_name": "Igor"
        }

        response = self.client.post(
            '/users/create/',
            data=wrong_data,
            **headers
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_400_BAD_REQUEST
        )

        self.assertEqual(
            response.json(),
            {
                'non_field_errors': [
                    'Все поля являются обязательными к заполнению, за исключением электронной '
                    'почты и адресса проживания. Пожалуйста заполните: patronymic, birth_date, '
                    'passport_number, birth_place, phone, registration_address'
                ]
            }
        )

    def test_get_user(self):
        """Тесты получения пользователя по его id"""

        response = self.client.get(
            '/users/6/'
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )

        self.assertEqual(
            response.json(),
            {
                'id': 6,
                'last_name': 'Ivanov',
                'first_name': 'Ivan',
                'patronymic': 'Ivanovich',
                'birth_date': '1990-01-01',
                'passport_number': '1111 111111',
                'birth_place': 'Ivanovo',
                'phone': '733333333',
                'email': 'Ivan@mail.ru',
                'registration_address': 'Ivanovo st Pushkina 1-1',
                'residential_address': 'Ivanovo st Pushkina 1-1'
            }
        )

        response = self.client.get(
            '/users/100/'
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_404_NOT_FOUND
        )

    def test_search_user(self):
        """Тесты поиска пользователей по одному или нескольким полям:
        фамилия, имя, отчество, телефон, электронная почта"""

        response = self.client.get(
            '/users/search/?first_name=Ivan&email=Ivan@mail.ru'
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )

        self.assertEqual(
            response.json(),
            [
                {
                    'id': 8,
                    'last_name': 'Ivanov',
                    'first_name': 'Ivan',
                    'patronymic': 'Ivanovich',
                    'birth_date': '1990-01-01',
                    'passport_number': '1111 111111',
                    'birth_place': 'Ivanovo',
                    'phone': '733333333',
                    'email': 'Ivan@mail.ru',
                    'registration_address': 'Ivanovo st Pushkina 1-1',
                    'residential_address': 'Ivanovo st Pushkina 1-1'
                }
            ]
        )

        response = self.client.get(
            '/users/search/?last_name=Petrov&patronymic=Petrovich&phone=74444444444'
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )

        self.assertEqual(
            response.json(),
            [
                {
                    'id': 9,
                    'last_name': 'Petrov',
                    'first_name': 'Petr',
                    'patronymic': 'Petrovich',
                    'birth_date': '1991-05-05',
                    'passport_number': '2222 222222',
                    'birth_place': 'Omsk',
                    'phone': '74444444444',
                    'email': 'Petr@mail.ru',
                    'registration_address': 'Omsk st Brova 7-45',
                    'residential_address': 'Omsk st Brova 7-45'
                }
            ]
        )

        response = self.client.get(
            '/users/search/?first_name=Test'
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )

        self.assertEqual(
            response.json(),
            []
        )
