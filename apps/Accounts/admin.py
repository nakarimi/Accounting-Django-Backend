from django.contrib import admin
from .models import Account, Type
# Register your models here.
@admin.register(Account)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('label', 'owner', 'status', 'balance')


admin.site.register(Type)
# @admin.register(Account_type)
