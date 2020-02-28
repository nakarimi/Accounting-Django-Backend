from django.contrib import admin
from .models import Bill
# Register your models here.
admin.site.register(Bill)
# @admin.register(Company)
# class Bill(admin.ModelAdmin):
    # list_display = ('com_name', 'com_email', 'com_website', 'com_owner')
#     list_filter = ('com_name', 'com_email')
#     search_fields = ('com_name',)
#     ordering = ['-pub_date']