import os
from random import random

from django.db import models

# Create your models here.
from django.db.models import Q
from django.db.models.signals import pre_save

from LenovoShop.utils import unique_slug_generator


def get_filename_ext(filepath):
    base_name = os.path.basename(filepath)
    name, ext = os.path.splitext(base_name)
    return name, ext


def upload_image_path(instance, filename):
    name, ext = get_filename_ext(filename)
    new_filename = random.randint(1, 123123123123)
    final_name = f"{new_filename}{ext}"
    return f"products/{final_name}"


class ProductQuerySet(models.query.QuerySet):
    def active(self):
        return self.filter(active=True)

    def featured(self):
        return self.filter(featured=True)

    def search(self, query):
        lookups = (
                Q(title__icontains=query) |
                Q(description__icontains=query) |
                Q(price__icontains=query) |
                Q(tag__title__icontains=query)
        )
        return self.filter(lookups).distinct()


class GoodsManager(models.Manager):
    def get_queryset(self):
        return

    def all(self):
        return self.get_queryset().active()

    def featured(self):
        return self.getqueryset().featured()

    def get_by_id(self, id):
        qs = self.get_queryset().filter(id=id)  # GoodsValue.objects == self.get_queryset()
        if qs.count() == 1:
            return qs.first()
        return None

    def featured(self):
        return self.get_queryset().featured()


# 创建商品种类模型
class ArticleCategory(models.Model):

    kind = models.CharField(max_length=30)  # 分类
    isDelete = models.BooleanField(default=False)  # 是否删除

    def __str__(self):
        return self.kind

    def __unicode__(self):
        return self.kind

    class Meta:
        verbose_name = "种类"
        verbose_name_plural = "种类"
        db_table = "kind"


# 创建商品属性模型
class GoodsValue(models.Model):
    slug = models.SlugField(blank=True)
    title = models.CharField(max_length=50)  # 商品名称
    image = models.ImageField(upload_to=upload_image_path, null=True, blank=True)  # 商品图片
    price = models.DecimalField(max_digits=20, decimal_places=4, default=1000)  # 商品价格
    repertory = models.IntegerField(default=0)  # 商品库存
    created_at = models.DateTimeField(auto_now_add=True)
    description = models.TextField()  # 商品描述
    isDelete = models.BooleanField(default=False)  # 是否删除
    featured = models.BooleanField(default=False)
    active = models.BooleanField(default=False)
    # 关联商品种类
    gtype = models.ForeignKey(ArticleCategory, on_delete=models.CASCADE)

    # Manager
    objects = GoodsManager()

    def __str__(self):
        return self.title

    def __unicode__(self):
        return self.title

    class Meta:
        verbose_name = "商品"
        verbose_name_plural = "商品"
        db_table = "goods"




def product_pre_save_receiver(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = unique_slug_generator(instance)
pre_save.connect(product_pre_save_receiver, sender=GoodsValue)  # Signals

