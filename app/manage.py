#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys


def main():
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'app.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()

'''
manage.py is automatically created in each Django project. 
It does the same thing as django-admin but also sets the DJANGO_SETTINGS_MODULE environment variable 
so that it points to your project’s settings.py file.
https://docs.djangoproject.com/en/2.2/intro/tutorial01/
https://subscription.packtpub.com/book/web_development/9781787286214/1/ch01lvl1sec11/the-core-app
'''