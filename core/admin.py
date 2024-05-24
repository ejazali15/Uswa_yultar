from django.contrib import admin
from .models import Result, Blog, Admission, Certificate

# Register your models here.

admin.site.register(Result)
admin.site.register(Blog)
admin.site.register(Admission)
admin.site.register(Certificate)
admin.site.site_title = "Uswa public school yultar admin"
admin.site.site_header = "Welcome to UPSY admin panel"
