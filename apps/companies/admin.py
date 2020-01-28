from django.contrib import admin
from .models import Company

# Register your models here.


# admin.site.register(Company)
@admin.register(Company)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('com_name', 'com_email', 'com_website', 'com_owner')
    list_filter = ('com_name', 'com_email')
    search_fields = ('com_name',)
    ordering = ['-pub_date']