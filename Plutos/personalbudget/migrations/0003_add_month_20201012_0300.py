# Generated by Django 3.1.1 on 2020-10-12 03:00

from django.db import migrations
import month.models


class Migration(migrations.Migration):
    dependencies = [
        ('personalbudget', '0002_change_phone_field_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='personalbudget',
            name='month',
            field=month.models.MonthField(null=True),
        )
    ]
