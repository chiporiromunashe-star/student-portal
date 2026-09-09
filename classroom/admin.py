from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User, Student, StudentMarks, Teacher, StudentsInClass

# Prevent "AlreadyRegistered" error for User
try:
    admin.site.unregister(User)
except admin.sites.NotRegistered:
    pass

# Register Custom or Default User
admin.site.register(User, UserAdmin)

# Register School Models
admin.site.register(Student)
admin.site.register(StudentMarks)
admin.site.register(Teacher)
admin.site.register(StudentsInClass)
