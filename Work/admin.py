from django.contrib import admin
from Work.models import Work
# Register your models here.
#admin.site.register(Work)

@admin.register(Work)
class WorkAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'finished', 'deadline']
    list_filter = ['finished', 'deadline']
    search_fields = ['name', 'description']
    ordering = ["id"]
    date_hierarchy = 'deadline'