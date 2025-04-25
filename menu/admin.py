from django.contrib import admin
from .models import MenuItem

class MenuItemAdmin(admin.ModelAdmin):
    list_display = ('name', 'parent')
    list_filter = ('parent',)
    prepopulated_fields = {'url': ('name',)}

admin.site.register(MenuItem, MenuItemAdmin)

