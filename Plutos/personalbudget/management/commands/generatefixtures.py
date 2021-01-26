import sys
import os
import random
from faker import Faker
from django.core.management.base import BaseCommand
from personalbudget.models import *


class Command(BaseCommand):
    avatars = ['https://images.app.goo.gl/eX1scdcBa7vA4T7t9', 'https://images.app.goo.gl/yvFACDPzGwdNkXj37',
               'https://images.app.goo.gl/w7RZLwcCbaVSRs3S8', 'https://images.app.goo.gl/adS47Arsd3x3Z7rN8',
               'https://images.app.goo.gl/peiGLo5nQDpKsdq77']

    fake_data = Faker()

    def userpopulate(self):
        fullname = self.fake_data.name()
        login = self.fake_data.user_name()
        password = self.fake_data.password()
        mail = self.fake_data.email()
        is_organization = bool(random.choice([True, False]))
        phone = '89996789910'
        avatar = random.choice(self.avatars)

        User.objects.create(fullname=fullname, login=login, password=password, mail=mail, phone=phone,
                            is_organization=is_organization, avatar=avatar)

    def personalbudgetpopulate(self, max):
        id_user = self.fake_data.random_int(1, max)
        balance = float(self.fake_data.random_int(0, 50000))
        month = self.fake_data.date()
        Personalbudget.objects.create(id_user_id=id_user, balance=balance, month=month)

    def populate(self, number):
        for _ in range(0, number):
            self.userpopulate()
        for _ in range(0, number):
            self.personalbudgetpopulate(number)

    def add_arguments(self, parser):
        parser.add_argument('num_populate', type=int)

    def handle(self, *args, **options):
        number = options['num_populate']
        self.populate(number)
        self.stdout.write(self.style.SUCCESS('Successfuly generated!'))
