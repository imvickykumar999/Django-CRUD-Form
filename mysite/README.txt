django-admin startproject mysite
# Note: `mysite` is user-defined name
cd mysite

# https://stackoverflow.com/ai/search/34258
python manage.py makemigrations
python manage.py migrate

# python manage.py createsuperuser
python manage.py createsuperuser --username imvickykumar999 --email imvickykumar999@gmail.com
# Note: `imvickykumar999` and `imvickykumar999@gmail.com` are user-defined names

python manage.py startapp home
# Note: `home` is user-defined name
python manage.py runserver
