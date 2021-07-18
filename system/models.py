from django.db import models

# Create your models here.
class Slider(models.Model):
    name = models.CharField("名称", max_length=32)
    desc = models.CharField("描述信息", max_length=100, null=True ,blank=True)
    types = models.SmallIntegerField("展现的位置", default=10)
    img = models.ImageField("图片地址", max_length=255, upload_to="%Y%m/slider")
    reorder = models.SmallIntegerField("优先级", default=0, help_text='数字越大越靠前')
    start_time = models.DateTimeField("生效开始时间", null=True ,blank=True)
    end_time = models.DateTimeField("失效时间", null=True ,blank=True)
    target_url = models.CharField("跳转地址", max_length=255, null=True ,blank=True)
    is_valid = models.BooleanField("删除字段", default=True)
    created_at = models.DateTimeField("创建时间", auto_now_add=True)
    updated_at = models.DateTimeField("修改时间", auto_now=True)
    class Meta:
        db_table = 'system_slider'
        ordering = ['-reorder']
