from django.contrib import admin
from .models import WPGroup
# Register your models here.

class WPGroupAdmin(admin.ModelAdmin):
    list_display=('name','number','bolum','mail')
    search_fields=('name','numi','bolum','mail')


admin.site.register(WPGroup,WPGroupAdmin)
