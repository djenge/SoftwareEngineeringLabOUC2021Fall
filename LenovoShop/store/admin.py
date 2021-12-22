from django.contrib import admin
from .models import GoodsValue
from .models import ArticleCategory

# Register your models here.
class GoodsAdmin(admin.ModelAdmin):
    list_display = ['__str__', 'slug']

    class Meta:
        model = GoodsValue

class ArticleCategoryAdmin(admin.ModelAdmin):

    class Meta:
        model = ArticleCategory

admin.site.register(GoodsValue, GoodsAdmin)
admin.site.register(ArticleCategory, ArticleCategoryAdmin)