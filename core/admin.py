from django.contrib import admin
from .models import Result, Blog, Admission, Certificate

# Register your models here.

admin.site.register(Result)
admin.site.register(Blog)
admin.site.register(Admission)
admin.site.register(Certificate)
