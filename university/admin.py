from django.contrib import admin
from .models import Faculty, Kafedra, Group, Student, Subject, Teacher


@admin.register(Faculty)
class FacultyAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']


@admin.register(Kafedra)
class KafedraAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']


@admin.register(Group)
class GroupAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'faculty']
    list_filter = ['faculty']


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ['id', 'first_name', 'last_name', 'kafedra', 'group']
    list_filter = ['kafedra', 'group']


@admin.register(Subject)
class SubjectAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'kafedra']
    list_filter = ['kafedra']


@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    list_display = ['id', 'first_name', 'last_name', 'subject']
    list_filter = ['subject']
