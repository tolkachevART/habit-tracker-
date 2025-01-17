# Habit Tracker

Этот проект представляет собой трекер полезных привычек, вдохновленный книгой Джеймса Клера «Атомные привычки». Он позволяет пользователям отслеживать свои привычки и получать уведомления о необходимости выполнения определенных действий.

## Установка

### Клонирование репозитория
````
https://github.com/tolkachevART/habit-tracker.git
````
### Создание зависимостей
Установить зависимости из файла pyproject.toml
````
poetry install
````
### Настройка окружения
Скопируйте файл .env.sample в .env и заполните необходимые переменные своими данными.
### Запуск Redis
Запустите Redis на вашем компьютере следующей командой:
````
redis-server
````
## Запуск проекта

Для запуска проекта выполните следующую команду в терминале:
````
python manage.py runserver
````
### Рассылка уведомлений
Celery Worker
Запустите Celery worker для обработки задач:
````
celery -A config worker -l INFO
````
Для Windows:
````
celery -A config worker -l INFO -P eventlet
````
### Celery Beat
Запустите Celery beat для планирования задач:
````
celery -A config beat -l info -S django
````
### Docker
Для запуска файла в Docker:
````
docker-compose up -d --build
````
