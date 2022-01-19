import os
from django.contrib import admin, messages
from django.http import JsonResponse

from Work.models import Work
from ExpManager.models import ExpManager
from django.db import transaction

@admin.register(Work)
class WorkAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'ipdst', 'port', 'exp', 'change']
    list_filter = ['ipdst', 'port', 'exp']
    search_fields = ['name', 'ipdst', 'port']
    ordering = ["id"]
    date_hierarchy = 'timestamp'
    @transaction.atomic
    def scan(self, request, queryset):
        workid = request.POST.get("_selected_action")
        taskname = Work.objects.filter(id=workid).values_list("name")[0][0]
        expid = Work.objects.filter(id=workid).values_list("exp_id")[0][0]
        vulnid = ExpManager.objects.filter(id=expid).values_list("vulnid")[0][0]
        ipaddress = Work.objects.filter(id=workid).values_list("ipdst")[0][0]
        path = ExpManager.objects.filter(id=expid).values_list("fileobj")[0][0]
        filepath = str(os.getcwd())+"/"+str(path)
        port = Work.objects.filter(id=workid).values_list("port")[0][0]
        command_string = ExpManager.objects.filter(id=expid).values_list("command")[0][0]
        command = command_string%(str(filepath), str(workid), str(taskname), str(vulnid), str(ipaddress), str(port))
        os.system(command)
        messages.add_message(request, messages.SUCCESS, '开始扫描%s'%str())

    scan.short_description = "启动扫描"
    scan.icon = 'fa fa-rocket'
    scan.style = 'color:white;'
    scan.type = 'danger'
    scan.confirm = '您确定要启动扫描吗？'
    actions = [scan, ]

