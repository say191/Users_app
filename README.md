Описание проекта

Веб сервис для работы с учетными записями пользователей со следующей функциональностью:
1.  Создание пользователя
2.  Получение пользователя по id
3.  Поиск пользователя по одному или нескольким полям: фамилия, имя, отчество, телефон, email.
Атрибуты пользователя:
-  Id
-  фамилия
-  имя
-  отчество
-  дата рождения
-  номер паспорта (вместе с серией в формате ХХХХ ХХХХХХ)
-  место рождения
-  телефон (в формате 7ХХХХХХХХХХ)
-  емейл
-  адрес регистрации
-  адрес проживания

Пользователь может быть создан из разных приложений. В зависимости от приложения отличается логика валидации полей при создании учетной записи пользователя. Приложение определяется по обязательному для указания http-заголовку "x-Device".
Список значений http-заголовка и правила валидации полей:
•  mail - только имя и емейл обязательные
•  mobile - только номер телефона обязательный
•  web - все поля кроме емейла и адреса проживания обязательные



Инструкция для запуска приложения с использованием Docker

- Склонировать репозиторий
- Создать базу данных postgres
- Создать файл .env и заполнить его по шаблону (.end.sample) (в переменную 'POSTGRES_HOST' записать значение 'db')
- выполнить в терминале команду doker-compose build
- выполнить в терминале команду doker-compose up



Интрукция по локальному запуску

- Склонировать репозиторий
- Устанавить виртуальное окружение python3 -m venv env
- Активировать виртуальное окружение source env/bin/activate
- Установить все зависимости pip install -r requirements.txt
- Создать базу данных в postgres
- Создать файл .env и заполнить его по шаблону (.end.sample) (в переменную 'POSTGRES_HOST' записать значение 'localhost')
- Выполнить миграции python manage.py makemigrations python manage.py migrate
- Запустить проект python manage.py runserver



Технические требования Python 3.8+ Django 3+ DRF 3.10+ PostgreSQL 10+, Docker
