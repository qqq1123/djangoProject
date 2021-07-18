from django.db import models

# Create your models here.


class Sight(models.Model):
    """景点基础信息"""
    name = models.CharField("名称", max_length=32)
    desc = models.CharField("描述信息", max_length=100, null=True, blank=True)
    main_img = models.ImageField("主图", max_length=256, upload_to="%Y%m/slider")
    banner_img = models.ImageField("详情页主图", max_length=256, upload_to="%Y%m/slider")
    content = models.TextField("详情")
    score = models.FloatField("评分", default=5)
    province = models.CharField("省份", max_length=32, null=True)
    city = models.CharField("市区", max_length=32, null=True)
    area = models.CharField("区/县", max_length=32)
    town = models.CharField("乡镇", max_length=32)
    min_price = models.FloatField("最低价格", default=0)
    is_top = models.BooleanField("是否为精选", default=False)
    is_hot = models.BooleanField("是否为热门", default=False)
    is_valid = models.BooleanField("是否为热门", default=True)
    created_at = models.DateTimeField("是否为热门", auto_now_add=True)
    undated_at = models.DateTimeField("是否为热门", auto_now=True)

    class Meta():
        db_table = "sight"
        ordering = ["-undated_at"]





