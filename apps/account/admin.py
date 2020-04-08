from django.contrib import admin
from .models import Account
# Register your models here.
@admin.register(Account)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('label', 'owner', 'status', 'balance')
