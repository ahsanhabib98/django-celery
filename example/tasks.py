from __future__ import absolute_import, unicode_literals
import random
from celery import shared_task
from django.core.mail import send_mail

from time import sleep


@shared_task
def sleepy(duration):
    sleep(duration)
    return None


@shared_task
def send_email_task():
    sleep(10)
    send_mail('Celery Task Worked!',
              'This is proof the task worked!',
              'your-mail',
              ['verepit474@demail3.com'])

    return None


@shared_task(name="sum_two_numbers")
def add(x, y):
    return x + y


@shared_task(name="multiply_two_numbers")
def mul(x, y):
    total = x * (y * random.randint(3, 100))
    return total


@shared_task(name="sum_list_numbers")
def xsum(numbers):
    return sum(numbers)
