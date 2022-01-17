from django.db import models
from tinymce.models import HTMLField
# Create your models here.
class Work(models.Model):
    id = models.AutoField(primary_key=True, db_column="id", verbose_name='编号')  # 工作编号
    name = models.CharField(max_length=32, db_column="name", verbose_name='工作名称')  # 工作名称
    finished = models.BooleanField(default=False, db_column="finished", verbose_name='完成')  # 完成与否
    description = HTMLField(db_column="worklog", verbose_name='工作日志')  # 进展情况
    deadline = models.DateField(db_column="deadline", verbose_name='截止日期')  #截止日期
    class Meta:
        verbose_name = '工作项'
        verbose_name_plural = verbose_name
