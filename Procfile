release: python manage.py makemigrations && python manage.py migrate
web: gunicorn tasks_api.wsgi