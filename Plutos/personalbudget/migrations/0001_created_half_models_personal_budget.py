# Generated by Django 3.1.1 on 2020-09-24 14:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Personalbudget',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('balance', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fullname', models.CharField(max_length=50)),
                ('login', models.CharField(max_length=50)),
                ('password', models.CharField(max_length=50)),
                ('mail', models.EmailField(max_length=254)),
                ('phone', models.IntegerField(max_length=11, null=True)),
                ('is_organization', models.BooleanField(null=True)),
                ('avatar', models.ImageField(null=True, upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='VariableExpences',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('description', models.TextField(null=True)),
                ('money', models.FloatField()),
                ('id_personal_budget',
                 models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='personalbudget.personalbudget')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='personalbudget',
            name='id_user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='personalbudget.user'),
        ),
        migrations.CreateModel(
            name='Income',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('description', models.TextField(null=True)),
                ('forecast_income', models.FloatField()),
                ('actual_income', models.FloatField()),
                ('id_personal_budget',
                 models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='personalbudget.personalbudget')),
            ],
        ),
        migrations.CreateModel(
            name='FixedExpences',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('description', models.TextField(null=True)),
                ('money', models.FloatField()),
                ('id_personal_budget',
                 models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='personalbudget.personalbudget')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='ExtraordinaryExpences',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('description', models.TextField(null=True)),
                ('money', models.FloatField()),
                ('id_personal_budget',
                 models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='personalbudget.personalbudget')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]