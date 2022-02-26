from django.contrib import admin

from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import Group

from .models import UserAccount

admin.site.unregister(Group)

@admin.register(UserAccount)
class PromotionsAdmin(admin.ModelAdmin):
  fieldsets = (
    (None, {'fields': ('email', 'password')}),
    (('Разрешения'), {'fields': ('is_active', 'is_staff', 'is_superuser')}),
  )