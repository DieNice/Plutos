import sys

sys.path.append('/home/pda/Projects/PycharmProjects/Plutos/Plutos')

from faker import Faker

fake_data = Faker()
import random
import os
import django
import argparse

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Plutos.settings")
django.setup()
from personalbudget.models import *

avatars = ['https://images.app.goo.gl/eX1scdcBa7vA4T7t9', 'https://images.app.goo.gl/yvFACDPzGwdNkXj37',
           'https://images.app.goo.gl/w7RZLwcCbaVSRs3S8', 'https://images.app.goo.gl/adS47Arsd3x3Z7rN8',
           'https://images.app.goo.gl/peiGLo5nQDpKsdq77']


def userpopulate():
    fullname = fake_data.name()
    login = fake_data.user_name()
    password = fake_data.password()
    mail = fake_data.email()
    is_organization = bool(random.choice([True, False]))
    phone = '89246784082'
    avatar = random.choice(avatars)

    User.objects.create(fullname=fullname, login=login, password=password, mail=mail, phone=phone,
                        is_organization=is_organization, avatar=avatar)


def personalbudgetpopulate():
    id_user = fake_data.random_int(1, 50)
    balance = float(fake_data.random_int(0, 50000))
    month = fake_data.date()
    Personalbudget.objects.create(id_user_id=id_user, balance=balance, month=month)


def populate(number):
    for _ in range(0, number):
        # userpopulate()
        personalbudgetpopulate()


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Number of populate")
    parser.add_argument("--number")
    args = parser.parse_args()
    number = int(args.number)
    populate(number)
