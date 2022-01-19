from django.contrib import admin

from ExpManager.models import ExpManager
from django.db import transaction
# Register your models here.
admin.site.site_header = '土拨鼠自动化扫描系统'  # 设置header
admin.site.site_title = '土拨鼠自动化扫描系统'          # 设置title
@admin.register(ExpManager)
class ExpManagerAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'category', 'vulnid', 'expflag', 'timestamp', 'change']
    list_filter = ['category','expflag']
    search_fields = ['name', 'vulnid']
    ordering = ["id"]
    date_hierarchy = 'timestamp'
