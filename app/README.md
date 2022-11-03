## RUN DOCKER
docker-compose up  --force-recreate
## CREATE Superuser
python manage.py makemigations
python manage.py migrate
python manage.py createsuperuser
## Create default template admin
python manage.py collectstatic
