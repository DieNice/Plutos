from django.db import models
import sys


class User(models.Model):
    fullname = models.CharField(max_length=50, null=False)
    login = models.CharField(max_length=50, null=False)
    password = models.CharField(max_length=50, null=False)
    mail = models.EmailField(null=False)
    phone = models.CharField(max_length=11, null=True)
    is_organization = models.BooleanField(null=True)
    avatar = models.ImageField(null=True)

    def __str__(self):
        '''String for representation the Model User'''
        return self.fullname

    def get_login(self):
        return self.login

    def get_password(self):
        return self.password

    def get_mail(self):
        return self.mail

    def get_phone(self):
        return self.phone

    def is_personal(self):
        return self.is_personal

    def is_orgnanization(self):
        return self.is_organization

    def get_ava(self):
        return self.avatar


class Months(models.Model):
    name = models.CharField(max_length=20, null=False)


class PersonalBudget(models.Model):
    id_user = models.ForeignKey(User, on_delete=models.CASCADE)
    balance = models.FloatField(null=False)
    id_month = models.OneToOneField(Months, on_delete=models.DO_NOTHING)


class Income(models.Model):
    id_personal_budget = models.ForeignKey(PersonalBudget, on_delete=models.CASCADE, null=False)
    name = models.CharField(max_length=50, null=False)
    description = models.TextField(null=True)
    forecast_income = models.FloatField(null=False)
    actual_income = models.FloatField(null=False)


class Expences(models.Model):
    id_personal_budget = models.ForeignKey(PersonalBudget, on_delete=models.CASCADE, null=False)
    name = models.CharField(max_length=50, null=False)
    description = models.TextField(null=True)
    money = models.FloatField(null=False)

    class Meta:
        abstract = True


class FixedExpences(Expences):
    pass


class VariableExpences(Expences):
    pass


class ExtraordinaryExpences(Expences):
    pass
