# Register your models here.
from django.contrib import admin

from .models import SurveyCompactResult, User, Checkin

admin.site.register(User)
admin.site.register(Checkin)
admin.site.register(SurveyCompactResult)
