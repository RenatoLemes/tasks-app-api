release: python manage.py makemigrations && python manage.py migrate
web: gunicorn tasks_app_api.wsgi