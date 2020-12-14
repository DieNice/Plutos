from django.db import models
from month.models import MonthField
import month
import sys


class User(models.Model):
    fullname = models.CharField(max_length=50, null=False)
    login = models.CharField(max_length=50, null=False)
    password = models.CharField(max_length=50, null=False)
    mail = models.EmailField(null=False)
    phone = models.CharField(max_length=11, null=True)
    is_organization = models.BooleanField(null=True)
    avatar = models.ImageField(null=True)


class Personalbudget(models.Model):
    id_user = models.ForeignKey(User, related_name='budgets', on_delete=models.CASCADE)
    balance = models.FloatField(null=False)
    month = MonthField(null=True)

    def __unicode__(self):
        return str(self.month)


class Income(models.Model):
    id_personal_budget = models.ForeignKey(Personalbudget, on_delete=models.CASCADE, null=False)
    name = models.CharField(max_length=50, null=False)
    description = models.TextField(null=True)
    forecast_income = models.FloatField(null=False)
    actual_income = models.FloatField(null=False)


class Expences(models.Model):
    id_personal_budget = models.ForeignKey(Personalbudget, on_delete=models.CASCADE, null=False)
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
