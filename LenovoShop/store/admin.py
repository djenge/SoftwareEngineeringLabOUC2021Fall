from django.contrib import admin
# Register your models here.
from store.models import GoodsValue, ArticleCategory


class GoodsAdmin(admin.ModelAdmin):
    list_display = ['__str__', 'slug']

    class Meta:
        model = GoodsValue

class ArticleCategoryAdmin(admin.ModelAdmin):

    class Meta:
        model = ArticleCategory


admin.site.register(GoodsValue, GoodsAdmin)
admin.site.register(ArticleCategory, ArticleCategoryAdmin)
