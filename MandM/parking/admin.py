
from .models import Vehicle,Category
from django.contrib import admin
from django.contrib.auth.models import Group

admin.site.site_header = "ADMIN MANAGEMENT"


class usr(admin.ModelAdmin):
    list_display = ( 'category', 'regno', 'intime', 'outtime','parkingcharge','status')
    list_filter = ('category', 'status')
    search_fields = ['regno' ]
    list_editable = ['status']


admin.site.register(Vehicle, usr)
admin.site.register(Category)


# Register your models here.
