from django.contrib import admin
from .models import *

admin.site.register(User)
admin.site.register(Personalbudget)
admin.site.register(Income)
admin.site.register(FixedExpences)
admin.site.register(VariableExpences)
admin.site.register(ExtraordinaryExpences)
