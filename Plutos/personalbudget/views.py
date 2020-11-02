from rest_framework.generics import _get_object_or_404
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import action
from .models import User, Personalbudget
from .serializers import UserSerializer, PersonalbudgetSerializer


class UserView(viewsets.ViewSet):
    """
       A simple ViewSet that for listing or retrieving users.
       """

    def list(self, request):
        queryset = User.objects.all()
        serializer = UserSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        queryset = User.objects.all()
        user = _get_object_or_404(queryset, pk=pk)
        serializer = UserSerializer(user)
        return Response(serializer.data)


class PersonalbudgetView(viewsets.ViewSet):
    """
       A simple ViewSet that for listing or retrieving users.
       """

    def list(self, request):
        queryset = Personalbudget.objects.all()
        serializer = PersonalbudgetSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        queryset = Personalbudget.objects.all()
        personalbudget = _get_object_or_404(queryset, pk=pk)
        serializer = PersonalbudgetSerializer(personalbudget)
        return Response(serializer.data)
