#!/bin/bash
echo "Trying----------------------------- to synch"
python manage.py syncdb --noinput
echo "Finish manage.py synchdb ----------------------------"
echo "from django.contrib.auth.models import User; User.objects.create_superuser('sudhanshu', 'sudhanshuccp@gmail.com', 'admin')" | python manage.py shell
echo "Finish creating super user ----------------------------"