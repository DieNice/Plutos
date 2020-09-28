from django.contrib import admin
from .models import *

admin.site.register(User)
admin.site.register(Months)
admin.site.register(PersonalBudget)
admin.site.register(Income)
admin.site.register(FixedExpences)
admin.site.register(VariableExpences)
admin.site.register(ExtraordinaryExpences)
