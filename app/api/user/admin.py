from django.contrib import admin

from api.user.models import User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ['id', 'fullname', 'email', 'phone', 'avatar']
    search_fields = ['email']


