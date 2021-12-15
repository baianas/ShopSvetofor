# django-admin startproject shop .
# python3 manage.py startapp application_name
# python3 manage.py runserver [(5000) --> опционально]

# python3 manage.py makemigrations


"""Последовательность команд"""
# 1. Создать папку проекта и перейти в него
# 2. В папке проекта нужно создать виртуальное окружение
# 3. Создать файл requirements.txt
# 4. Установить зависимости 'pip3 install -r requirements.txt'
# 5. Создать 'django-admin startproject название .'
# 6. Создать приложения 'python3 manage.py startapp название'
# 7. Создать БД
# 8. Настроить settings.py (указать приложения в INSTALLED_APPS, указать подключение к БД и т.д.)
# 9. Создать модель пользователя
# 10. В settings.py необходимо указать AUTH_USER_MODEL
# 11. Произвести миграции:
# 'python3 manage.py makemigrations'
# 'python3 manage.py migrate'
# 12. 'python3 manage.py runserver'
# 13.


#  python3 manage.py createsuperuser  -> создание админа