from django.contrib import admin
from students.models import Student,Question,Choice

# Register your models here.
admin.site.register(Student)
admin.site.register(Question)
admin.site.register(Choice)

