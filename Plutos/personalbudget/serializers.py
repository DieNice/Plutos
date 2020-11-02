from rest_framework import serializers
from .models import User, Personalbudget


class PersonalbudgetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Personalbudget
        fields = ('id_user', 'balance', 'month')


class UserSerializer(serializers.ModelSerializer):
    budgets = PersonalbudgetSerializer(read_only=True, many=True)

    class Meta:
        model = User
        fields = [
            'id', 'fullname', 'login', 'password', 'mail', 'phone', 'avatar', 'budgets']
