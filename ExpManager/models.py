from django.db import models

# Create your models here.
from django.db import models
from django.utils.html import format_html

from tinymce.models import HTMLField
# Create your models here.
class ExpManager(models.Model):
    id = models.AutoField(primary_key=True, db_column="id", verbose_name='序号')
    name = models.CharField(max_length=32, db_column="name", verbose_name='漏洞名称')
    vulnid = models.CharField(max_length=32, db_column="vulnid", verbose_name='漏洞编号')
    Category_Choices = (("1", "WEB漏洞"), ("2", "系统漏洞"), ("3", "其他漏洞"))
    category = models.CharField(max_length=2, choices=Category_Choices, verbose_name='漏洞类型')
    fileobj = models.FileField(upload_to='MyCMS/exp/', null=True, verbose_name="工具上传")
    command = models.TextField(db_column="command", verbose_name='执行命令', null=True)
    expflag = models.BooleanField(db_column="expflag", verbose_name="是否有EXP", default=False)
    description = HTMLField(db_column="description", verbose_name='漏洞描述')
    timestamp = models.DateField(db_column="deadline", verbose_name='创建日期')
    command = models.TextField(db_column="command", verbose_name='执行命令', null=True)
    def __str__(self):
        return self.name
    def change(self):
        btn_str = '<a class="btn btn-xs btn-danger" href="{}">' \
                    '<input name="编辑漏洞"' \
                    'type="button" id="passButton" ' \
                    'title="passButton" value="修改">' \
                    '</a>'
        return format_html(btn_str, '%s/change'%self.id)
    change.short_description = '漏洞编辑'
    class Meta:
        verbose_name = '验证工具'
        verbose_name_plural = verbose_name

