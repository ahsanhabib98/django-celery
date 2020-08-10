### Follow command to get started

````
1. pip install -r requirements.txt
2. python manage.py runserver
3. celery -A djangoCelery beat -l info (another Terminal window)
4. celery -A djangoCelery worker -l info (another Terminal window)
5. python manage.py runserver