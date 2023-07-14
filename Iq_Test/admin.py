from django.contrib import admin
from .models import *
# Register your models here.

admin.site.register(IQQuestion)
admin.site.register(UserIQResponse)
admin.site.register(UserScore)

