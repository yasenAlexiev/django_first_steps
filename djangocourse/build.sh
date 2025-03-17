poetry install --no-root
poetry add django
poetry run django-admin startproject djangocourse .
poetry run python .\manage.py runserver
poetry run python .\manage.py migrate
poetry run python .\manage.py createsuperuser
poetry run python .\manage.py startapp app
