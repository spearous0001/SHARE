#!/bin/bash

rm -fv ./{*/*/*/,*/*/,}*/migrations/00*.py

python manage.py reset_db --noinput \
&& python manage.py makemigrations \
&& git checkout api/migrations \
&& git checkout share/migrations \
&& python manage.py maketriggermigrations \
&& python manage.py makeprovidermigrations \
&& python manage.py migrate \
&& python manage.py createsuperuser