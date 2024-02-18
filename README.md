# recipe-app-api-upgrade

Project based on django rest framework with docker

# Build project with docker-compose

docker-compose build

# Create django project

docker-compose run --rm app sh -c "django-admin startproject app ."

# Run Linting

docker-compose run --rm app sh -c "flake8"

# Run Testing

docker-compose run --rm app sh -c "python manage.py test"

# Create core app

docker-compose run --rm app sh -c "python manage.py startapp core"

# Test if database is ready

docker-compose run --rm app sh -c "python manage.py wait_for_db"

# Fix flake8 erros

docker-compose run --rm app sh -c "python /app/flake8_autofix.py"

# Test if database is ready and run flake8

docker-compose run --rm app sh -c "python manage.py wait_for_db && flake8"

# Create migrations

docker-compose run --rm app sh -c "python manage.py makemigrations"

# Show migrations

docker-compose run --rm app sh -c "python manage.py sqlmigrate news 0001"

# Run migrations

docker-compose run --rm app sh -c "python manage.py wait_for_db && python manage.py migrate"

# Create super user

docker-compose run --rm app sh -c "python manage.py createsuperuser"

# Create user app

docker-compose run --rm app sh -c "python manage.py startapp user"

# Create migration for Recipe Model

docker-compose run --rm app sh -c "python manage.py makemigrations"

# Create recipe app

docker-compose run --rm app sh -c "python manage.py startapp recipe"